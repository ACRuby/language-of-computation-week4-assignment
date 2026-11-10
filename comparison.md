# Database comparison: my books.db vs my partner's books.db

**The two databases hold the same data.** Mine: 10,013 books. Partner's: 10,013 books.

| | Mine | Partner's |
|---|---|---|
| Books | 10,013 | 10,013 |
| Warning rows | 710 | 710 |
| Books only in this database | 0 | 0 |
| Books in both | 10,013 | 10,013 |

## How the comparison was done

- **Mine:** `books.db` in this folder. **Partner's:** `partner/books.db`, downloaded from `github.com/fme5034/language-of-computation-week4-assignment` (branch `assignment`). Both were opened read-only for the comparison.
- **Same book:** two rows are the same book when they have the same `goodreads_book_id` (rules.md section 2: identity is `goodreads_book_id` alone).
- **Both databases have the same tables and columns**, so each column was compared with the column of the same name.
- **Compared (books table):** the 22 CSV columns other than `goodreads_book_id` (`book_id`, `best_book_id`, `work_id`, `books_count`, `isbn`, `isbn13`, `authors`, `original_publication_year`, `original_title`, `title`, `language_code`, `average_rating`, `ratings_count`, `work_ratings_count`, `work_text_reviews_count`, `ratings_1`–`ratings_5`, `image_url`, `small_image_url`), plus `identity_key`.
- **Compared (warnings table):** each warning's `field`, `raw_value` and `reason`, matched to its book by `goodreads_book_id`.
- **Left out:** `first_loaded_at`, `last_updated_at` and `warnings.recorded_at` (they only record when a row was loaded), and `id`, `book_row_id`, `source_file` and `fallback_key`.
- Values were compared exactly as stored. *(empty)* means the column holds no value (NULL).

## Books only in mine

None.

## Books only in my partner's

None.

## Books in both with a different value

None.

## Books in both with different warnings

None.

## What was changed to make them match

A first comparison (2026-11-09) found 5 books with different values and 142 books with different warnings. All of it came from load order or from cases rules.md doesn't decide, so my build was changed to match my partner's:

1. **Load order.** `books.db` and `ingestion-log.json` were rebuilt in my partner's order: `books.csv`, `books.csv` again, then `books-batch2.csv` (I had loaded batch 2 first). This fixed the rating counts on 4 books (*1984*, *Animal Farm*, *The Five People You Meet in Heaven*, *City of Glass*): rating counts are always overwritten by the newest load (rules.md section 3), so the last file wins.
2. **`no-usable-isbn`** is now added only when both ISBN columns were blank in the CSV, as rules.md section 1 words it ("Both `isbn` and `isbn13` blank"). Before, my build also added it when the values were present but unusable. This fixed 141 books' warnings.
3. **Two valid ISBNs that disagree** (*Tides of Marrow Bay*: 1555550126 / 9781555550134) are now both kept with no warning; before, my build emptied both and warned `isbn-mismatch`. rules.md has no rule for this case, so this is a choice the group may still want to decide.

Changes 2 and 3 are in `isbn.py`. `ingest.py` and `rules.md` were not changed.
