# language-of-computation-week4-assignment

This is my Module 4 assignment for MSAI-5523 (Language of Computation).

Partners: Kristina and Anthony.

## Running the tests and the program

Type these commands in **Windows PowerShell**. Always use `py -3.13`, not
`python3`: on Windows, `python3` opens the Microsoft Store instead of
running Python.

### 1. Go to the project folder

```bash
cd ~\workspace\language-of-computation\week4-assignment
```

Do this first every time you open a new PowerShell window.

### 2. Install what the tests need (once)

The tests need **pytest**. Everything else they use comes with Python.

```bash
py -3.13 -m pip install pytest
```

Check that it worked:

```bash
py -3.13 -m pytest --version
```

You should see `pytest 9.2.0` or a later version.

### 3. Run the tests

The tests that check `ingest.py` against `rules.md` (22 tests):

```bash
py -3.13 -m pytest tests/test_rules.py -v
```

Every test (the 22 above plus the 43 brought over from week 3, 65 in all):

```bash
py -3.13 -m pytest -v
```

The tests never touch `books.db` or `ingestion-log.json`. Each test uses its
own `test.db` and log in a temporary folder and deletes them when it
finishes, whether it passed or failed.

### 4. Run ingest.py

These commands **do** change the real `books.db` and add one entry to
`ingestion-log.json` each time.

Load `books.csv`:

```bash
py -3.13 ingest.py
```

Load `books.csv` again (the same command). Every book is already saved and
unchanged, so they are all **skipped** and no duplicates are created:

```bash
py -3.13 ingest.py
```

Load `books-batch2.csv`. `ingest.py` has no command-line options (the file
name is fixed in the program), so this line tells it which file to use:

```bash
py -3.13 -c "import ingest; print(ingest.summary_line(ingest.run(ingest.HERE / 'books-batch2.csv')))"
```

Each command prints one summary line, for example:

```
status=COMPLETED WITH ISSUES rows_read=10000 loaded=0 updated=0 skipped=10000 rejected=0 rows_with_warning=703
```

To see the details of every run, open `report.html` in your web browser and
choose `ingestion-log.json`.
