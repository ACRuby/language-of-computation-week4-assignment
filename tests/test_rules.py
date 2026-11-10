"""pytest suite: does ingest.py do what rules.md says?

rules.md is the only source of truth. Every test names the rule it comes from,
and nothing here checks behaviour that rules.md doesn't state.

Files: each test works in its own new temporary folder, with the database
named test.db and the log named test-log.json. The `workspace` fixture deletes
that folder and everything in it when the test ends, whether it passed or
failed. The books.db and ingestion-log.json in the project folder are never
used: every call to ingest.run() is given the test.db and test-log.json paths.

Run with:  py -3.13 -m pytest tests/test_rules.py -v
"""
import csv
import json
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import ingest  # noqa: E402

# rules.md section 5: the 23 fields from the source CSV, in the CSV's order.
HEADER = ["book_id", "goodreads_book_id", "best_book_id", "work_id", "books_count", "isbn", "isbn13",
          "authors", "original_publication_year", "original_title", "title", "language_code",
          "average_rating", "ratings_count", "work_ratings_count", "work_text_reviews_count",
          "ratings_1", "ratings_2", "ratings_3", "ratings_4", "ratings_5", "image_url", "small_image_url"]

# One real book, checked by hand: ISBN-10 0439023483 <-> ISBN-13 9780439023481.
ISBN10 = "0439023483"
ISBN13 = "9780439023481"

FIXED_TIME = datetime(2026, 11, 9, 12, 0, 0, tzinfo=timezone.utc)


def book(gid, isbn="", isbn13="", **fields):
    """One CSV row as a dict. Only the ISBN fields matter to most tests."""
    row = {
        "book_id": gid, "goodreads_book_id": gid, "best_book_id": gid, "work_id": f"9{gid}",
        "books_count": "10", "isbn": isbn, "isbn13": isbn13, "authors": "Test Author",
        "original_publication_year": "2008.0", "original_title": f"Book {gid}", "title": f"Book {gid}",
        "language_code": "eng", "average_rating": "4.1", "ratings_count": "100",
        "work_ratings_count": "110", "work_text_reviews_count": "12", "ratings_1": "1", "ratings_2": "2",
        "ratings_3": "10", "ratings_4": "40", "ratings_5": "57",
        "image_url": "https://example.com/i.jpg", "small_image_url": "https://example.com/s.jpg",
    }
    row.update(fields)
    return row


class Workspace:
    """A throwaway folder holding test.db, test-log.json and the test's CSV files."""

    def __init__(self, folder: Path):
        self.folder = folder
        self.db = folder / "test.db"
        self.log = folder / "test-log.json"
        self._n = 0

    def csv(self, rows, extra_lines=()):
        """Writes the rows (plus any raw extra lines) to a new CSV file and returns its path."""
        self._n += 1
        path = self.folder / f"input{self._n}.csv"
        with path.open("w", encoding="utf-8", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=HEADER)
            writer.writeheader()
            writer.writerows(rows)
            for raw in extra_lines:
                fh.write(raw + "\r\n")
        return path

    def run(self, csv_path, now=None):
        """One ingestion run against test.db / test-log.json. Returns the log entry the run wrote."""
        kwargs = {"now": (lambda: now)} if now else {}
        ingest.run(csv_path, self.db, self.log, **kwargs)
        return self.log_entries()[-1]

    def log_entries(self):
        return json.loads(self.log.read_text(encoding="utf-8"))

    def query(self, sql, params=()):
        conn = sqlite3.connect(self.db)
        conn.row_factory = sqlite3.Row
        try:
            return [dict(r) for r in conn.execute(sql, params).fetchall()]
        finally:
            conn.close()

    def stored(self, gid):
        """The saved books row for this goodreads_book_id, or None if it wasn't saved."""
        rows = self.query("SELECT * FROM books WHERE goodreads_book_id = ?", (gid,))
        assert len(rows) <= 1
        return rows[0] if rows else None

    def warnings_for(self, gid, field=None):
        sql = ("SELECT w.* FROM warnings w JOIN books b ON b.id = w.book_row_id "
               "WHERE b.goodreads_book_id = ?")
        params = [gid]
        if field:
            sql += " AND w.field = ?"
            params.append(field)
        return self.query(sql, params)


@pytest.fixture
def workspace():
    folder = Path(tempfile.mkdtemp(prefix="ingest-rules-test-"))
    try:
        yield Workspace(folder)
    finally:
        # Teardown runs whether the test passed or failed: test.db, test-log.json,
        # the CSV files and the folder itself are all removed.
        shutil.rmtree(folder, ignore_errors=True)
        assert not folder.exists(), f"teardown could not remove {folder}"


def reasons(warning_row):
    """rules.md section 1: a warning's reason is one or more comma-separated codes."""
    return set(warning_row["reason"].split(","))


def load_one(ws, **isbn_fields):
    """Loads a single book (goodreads_book_id 1) and returns its saved row."""
    entry = ws.run(ws.csv([book("1", **isbn_fields)]))
    assert entry["counts"]["rejected"] == 0, "a bad or missing ISBN never rejects the row (section 1)"
    saved = ws.stored("1")
    assert saved is not None, "the row is always loaded (section 1)"
    return saved


def assert_loaded_with_warning(ws, saved, field, raw):
    """section 1 'Load with a warning; null the field': loaded, field empty, warning keeps the raw value."""
    assert saved[field] in (None, ""), f"{field} should be nulled"
    warns = ws.warnings_for("1", field)
    assert warns, f"expected a warning on {field}"
    assert raw in [w["raw_value"] for w in warns], "the original value is kept for audit (section 5)"


# ---------------------------------------------------------------------------------------------
# rules.md section 1 table: one test per row, in the table's order.
# ---------------------------------------------------------------------------------------------

def test_1_already_valid_loads_with_no_warning(workspace):
    """Already a valid ISBN-10 or ISBN-13 -> Load, no warning."""
    saved = load_one(workspace, isbn=ISBN10, isbn13=ISBN13)
    assert (saved["isbn"], saved["isbn13"]) == (ISBN10, ISBN13)
    assert workspace.warnings_for("1") == []


def test_2_hyphens_and_spaces_are_stripped(workspace):
    """Valid, but formatted with hyphens/spaces -> Repair: strip separators."""
    saved = load_one(workspace, isbn="0-439-02348-3", isbn13="978 0 439 02348 1")
    assert (saved["isbn"], saved["isbn13"]) == (ISBN10, ISBN13)


def test_3_stripped_leading_zero_is_padded(workspace):
    """isbn with leading zero(s) stripped (7-9 digits) -> Repair: zero-pad to 10 if it then passes."""
    saved = load_one(workspace, isbn="439023483", isbn13=ISBN13)
    assert saved["isbn"] == ISBN10


def test_4_stripped_978_check_digit_is_recomputed(workspace):
    """10-digit isbn fails its checksum but 978 + it passes ISBN-13 -> Repair: recompute the ISBN-10
    check digit. 0439023481 fails as an ISBN-10; 978 + 0439023481 = 9780439023481 is valid."""
    saved = load_one(workspace, isbn="0439023481")
    assert saved["isbn"] == ISBN10


def test_5_scientific_notation_isbn13_derived_from_valid_isbn(workspace):
    """isbn13 stored as scientific notation, row has a valid isbn -> Repair: derive isbn13 from isbn."""
    saved = load_one(workspace, isbn=ISBN10, isbn13="9.78043902348e+12")
    assert saved["isbn13"] == ISBN13


def test_6_blank_isbn13_derived_from_valid_isbn(workspace):
    """isbn13 simply blank, row has a valid isbn -> Repair: derive isbn13 from isbn."""
    saved = load_one(workspace, isbn=ISBN10, isbn13="")
    assert saved["isbn13"] == ISBN13


def test_7_blank_isbn_derived_from_isbn13_but_not_from_979(workspace):
    """isbn blank, isbn13 is a valid 978 ISBN-13 -> Repair: derive isbn from isbn13.
    979-prefixed ISBN-13s have no ISBN-10 form and are left blank."""
    workspace.run(workspace.csv([book("1", isbn="", isbn13=ISBN13),
                                 book("2", isbn="", isbn13="9791090102934")]))
    first, second = workspace.stored("1"), workspace.stored("2")
    assert first["isbn"] == ISBN10
    assert second["isbn13"] == "9791090102934"
    assert second["isbn"] in (None, "")


def test_8_scientific_notation_isbn13_with_no_isbn_is_warned_and_nulled(workspace):
    """isbn13 as scientific notation, no usable isbn -> Load with a warning; null isbn13;
    keep the raw text in an audit column."""
    saved = load_one(workspace, isbn="", isbn13="9.78043902348e+12")
    assert_loaded_with_warning(workspace, saved, "isbn13", "9.78043902348e+12")


def test_9_wrong_check_digit_with_no_repair_is_warned_and_nulled(workspace):
    """Right length/characters, wrong check digit, no repair applies -> Load with a warning; null.
    0439023480 fails as an ISBN-10, and 9780439023480 fails as an ISBN-13 too."""
    saved = load_one(workspace, isbn="0439023480")
    assert_loaded_with_warning(workspace, saved, "isbn", "0439023480")


def test_10_invalid_character_is_warned_and_nulled(workspace):
    """A letter where only a digit/trailing X belongs -> Load with a warning; null the field."""
    saved = load_one(workspace, isbn="04390X3483")
    assert_loaded_with_warning(workspace, saved, "isbn", "04390X3483")


def test_11_wrong_length_is_warned_and_nulled(workspace):
    """Wrong length that isn't a leading-zero case -> Load with a warning; null the field."""
    saved = load_one(workspace, isbn="04390234831")      # 11 digits
    assert_loaded_with_warning(workspace, saved, "isbn", "04390234831")


def test_12_valid_checksum_but_bad_prefix_is_warned_and_nulled(workspace):
    """13 digits, valid checksum, prefix not 978/979 -> Load with a warning; null the field."""
    saved = load_one(workspace, isbn13="9770439023482")
    assert_loaded_with_warning(workspace, saved, "isbn13", "9770439023482")


def test_13_isbn13_in_the_isbn_column_is_moved(workspace):
    """A valid ISBN-13 in the isbn column -> Repair: move it into isbn13, null isbn; then the
    reverse-derivation row (test 7) re-populates isbn, since this ISBN-13 is 978-prefixed."""
    saved = load_one(workspace, isbn=ISBN13, isbn13="")
    assert saved["isbn13"] == ISBN13
    assert saved["isbn"] == ISBN10


def test_14_both_blank_loads_with_no_usable_isbn_warning(workspace):
    """Both isbn and isbn13 blank -> Load, with a warning (no-usable-isbn)."""
    saved = load_one(workspace, isbn="", isbn13="")
    assert saved["isbn"] in (None, "") and saved["isbn13"] in (None, "")
    assert any("no-usable-isbn" in reasons(w) for w in workspace.warnings_for("1"))


def test_15_isbn_already_belonging_to_another_book_is_rejected(workspace):
    """A valid ISBN already belongs to a different goodreads_book_id on file -> Reject (isbn-collision)."""
    workspace.run(workspace.csv([book("1", isbn=ISBN10, isbn13=ISBN13)]))
    entry = workspace.run(workspace.csv([book("2", isbn=ISBN10, isbn13=ISBN13)]))
    assert workspace.stored("2") is None
    assert entry["counts"]["rejected"] == 1
    assert [r["reason"] for r in entry["needs_attention"]] == ["isbn-collision"]


def test_16_unparseable_value_is_warned_and_nulled(workspace):
    """A completely unparseable value (letters only, symbols, garbage) -> Load with a warning; null."""
    saved = load_one(workspace, isbn="@@##!!")
    assert_loaded_with_warning(workspace, saved, "isbn", "@@##!!")


def test_17_every_applicable_reason_is_listed(workspace):
    """A field with more than one problem -> list every reason, comma-separated
    (e.g. bad-prefix,bad-checksum). 9770439023483: 977 prefix and a wrong check digit."""
    saved = load_one(workspace, isbn13="9770439023483")
    assert_loaded_with_warning(workspace, saved, "isbn13", "9770439023483")
    warning = workspace.warnings_for("1", "isbn13")[0]
    assert {"bad-prefix", "bad-checksum"} <= reasons(warning)


def test_18_row_that_fails_to_parse_as_csv_is_rejected(workspace):
    """The row itself fails to parse as CSV (wrong field count) -> Reject the row, reason recorded."""
    broken = book("2", isbn=ISBN10, isbn13=ISBN13)
    extra = ",".join(broken[c] for c in HEADER) + ",one-field-too-many"     # 24 fields, header has 23
    entry = workspace.run(workspace.csv([book("1")], extra_lines=[extra]))
    assert workspace.stored("2") is None
    assert entry["counts"]["rejected"] == 1
    assert entry["needs_attention"][0]["reason"], "a reason is recorded"


# ---------------------------------------------------------------------------------------------
# Whole-run rules
# ---------------------------------------------------------------------------------------------

def sample_file(ws):
    """A small file mixing clean loads, repairs and warnings."""
    return ws.csv([
        book("1", isbn=ISBN10, isbn13=ISBN13),
        book("2", isbn="", isbn13="9791090102934"),
        book("3", isbn="0-306-40615-2"),
        book("4", isbn="", isbn13=""),
        book("5", isbn="04390X3483", isbn13="9.78043902348e+12"),
    ])


def test_running_the_same_file_twice_creates_no_duplicates(workspace):
    """Section 2: identity is goodreads_book_id alone. Section 3: nothing different -> Skip."""
    path = sample_file(workspace)
    workspace.run(path)
    second = workspace.run(path)
    ids = [r["goodreads_book_id"] for r in workspace.query("SELECT goodreads_book_id FROM books")]
    assert sorted(ids) == ["1", "2", "3", "4", "5"]
    assert (second["counts"]["loaded"], second["counts"]["skipped"]) == (0, 5)


def test_every_run_appends_to_the_log_without_overwriting(workspace):
    """Section 4: every run appends one entry to the log; no prior entry is ever overwritten."""
    path = sample_file(workspace)
    seen = []
    for _ in range(3):
        workspace.run(path)
        entries = workspace.log_entries()
        assert len(entries) == len(seen) + 1
        assert entries[:len(seen)] == seen, "earlier entries must be unchanged"
        seen = entries


def test_loaded_updated_skipped_rejected_add_up_to_rows_read(workspace):
    """Section 4 headline counts: rows read, loaded, updated, skipped, rejected.
    The second file has one row of each outcome: skipped (1, unchanged), updated (2, new rating),
    loaded (6, new book), rejected (7, ISBN already belongs to book 1)."""
    workspace.run(workspace.csv([book("1", isbn=ISBN10, isbn13=ISBN13), book("2", average_rating="3.0")]))
    workspace.run(workspace.csv([
        book("1", isbn=ISBN10, isbn13=ISBN13),
        book("2", average_rating="3.5"),
        book("6"),
        book("7", isbn=ISBN10),
    ]))
    for entry in workspace.log_entries():
        c = entry["counts"]
        assert c["loaded"] + c["updated"] + c["skipped"] + c["rejected"] == c["rows_read"]
    last = workspace.log_entries()[-1]["counts"]
    assert (last["rows_read"], last["loaded"], last["updated"], last["skipped"], last["rejected"]) == (4, 1, 1, 1, 1)


def dump(db_path):
    """Every row of both tables (section 5), in id order."""
    conn = sqlite3.connect(db_path)
    try:
        return {t: conn.execute(f"SELECT * FROM {t} ORDER BY id").fetchall() for t in ("books", "warnings")}
    finally:
        conn.close()


def test_same_file_on_an_empty_database_gives_the_same_database(workspace):
    """Operational details: no randomness; the same input file always produces the same result.
    Both runs get the same fixed clock, so every column, timestamps included, must match."""
    path = sample_file(workspace)
    workspace.run(path, now=FIXED_TIME)
    first = dump(workspace.db)
    workspace.db.unlink()                        # back to an empty database
    workspace.run(path, now=FIXED_TIME)
    second = dump(workspace.db)
    assert first["books"], "the run should have loaded something"
    assert first == second
