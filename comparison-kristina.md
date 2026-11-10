# Database comparison: my books.db vs Kristina's books.db

**The two databases hold the same books, but they do not hold the same data.** Both have **10,013 books** and **710 warning rows**, and every book is in both. But **2,142 books have at least one different value** (3,137 values in all), and **706 books have warnings that differ** (1,416 warning rows).

Almost all of it is about *how* things are stored, not *what* was stored: 3,136 of the 3,137 value differences are a missing value stored two different ways, and every warning difference is the same problem filed under a different name or column. Only **1 value** differs in content (an ISBN check character's case).

This comparison only reports differences. Nothing was changed to make the databases match.

| | Mine | Kristina's |
|---|---|---|
| Books | 10,013 | 10,013 |
| Warning rows | 710 | 710 |
| Books only in this database | 0 | 0 |
| Books in both | 10,013 | 10,013 |
| Books with a different value | 2,142 | |
| Books with different warnings | 706 | |

## How the comparison was done

- **Mine:** `books.db` in this folder. **Kristina's:** `partner-kristina/books.db`, downloaded from `github.com/winegarkr/languageofcomputation-week4-assignment` (branch `assignment`, commit `cca89fc`). Both were opened read-only; neither database was changed.
- **Same book:** same `goodreads_book_id` (rules.md section 2).
- **Both databases have the same tables and columns**, so each column was compared with the column of the same name.
- **Compared (books table):** the 22 CSV columns other than `goodreads_book_id`, plus `identity_key`, the same columns as the comparison with my other partner (`comparison.md`).
- **Compared (warnings table):** each warning's `field`, `raw_value` and `reason`, matched to its book by `goodreads_book_id`.
- **Left out:** `first_loaded_at`, `last_updated_at`, `warnings.recorded_at`, `id`, `book_row_id`, `source_file` and `fallback_key`.
- Values were compared exactly as stored. *(empty)* means the column holds no value (NULL); *(blank text)* means it holds text with nothing in it (`''`).
- Both were loaded in the same order (`books.csv`, `books.csv` again, `books-batch2.csv`), and no rating counts differ, so load order is not a cause here.

## Books only in mine

None.

## Books only in Kristina's

None.

## Books in both with a different value

### 1. A missing value is stored differently (3,131 values, 2,138 books)

When the CSV cell is blank, or an ISBN is thrown out, my build stores **no value** (NULL). Kristina's stores **blank text** (`''`). Either way the book has no value there. rules.md says a bad ISBN "nulls" the field (section 1) but doesn't say how other blank cells are stored.

| Column | Values |
|---|---|
| `language_code` | 1,084 |
| `isbn` | 708 |
| `isbn13` | 707 |
| `original_title` | 585 |
| `original_publication_year` | 21 |
| `image_url` | 13 |
| `small_image_url` | 13 |

### 2. A title that is only a space (5 values)

The CSV's `original_title` is a single space. My build trims it and stores no value; Kristina's keeps the space.

| goodreads_book_id | Book | Column | My value | Kristina's value |
|---|---|---|---|---|
| 9549 | Shadows of the Empire (Star Wars) | `original_title` | *(empty)* | *(1 space)* |
| 92871 | Brothers Majere (Dragonlance: Preludes, #3) | `original_title` | *(empty)* | *(1 space)* |
| 111220 | Eleanor of Aquitaine: A Life  | `original_title` | *(empty)* | *(1 space)* |
| 239107 | Sea of Swords (Forgotten Realms: Paths of Darkness, #4; Legend of Drizzt, #13) | `original_title` | *(empty)* | *(1 space)* |
| 826582 | If You Take a Mouse to School | `original_title` | *(empty)* | *(1 space)* |

### 3. Different content (1 value)

The ISBN-10 check character `X` is uppercase in mine and lowercase in Kristina's. Both are the same valid ISBN; rules.md doesn't say which case to store.

| goodreads_book_id | Book | Column | My value | Kristina's value |
|---|---|---|---|---|
| 90010004 | Winter Orchard | `isbn` | `031200009X` | `031200009x` |

## Books in both with different warnings

706 books, 1,416 warning rows. Both databases warn about **the same books for the same problems**, so the warning counts match (710 each). The differences are in what each warning is called and which column it is filed under. rules.md names only a few codes (`no-usable-isbn`, `isbn-collision`, `duplicate-unchanged`, `identity-field-conflict`), so each build named the rest its own way.

| Books | My warning | Kristina's warning | What's different |
|---|---|---|---|
| 566 | `isbn13`: `no-usable-isbn` | `isbn`: `no-usable-isbn` | Same code, different column: I file it under `isbn13`, Kristina under `isbn`. |
| 111 | `isbn13`: `lost-precision` | `isbn13`: `float-precision-lost` | Different name for the same problem (scientific notation, digits lost). |
| 25 | `isbn13`: `lost-precision,bad-prefix` | `isbn13`: `float-precision-lost` | Different name; mine also lists `bad-prefix` (the value doesn't start with 978/979), Kristina's lists only the lost digits. |
| 2 | `isbn`: `bad-checksum`<br>`isbn13`: `lost-precision` | `isbn`: `wrong-length`<br>`isbn13`: `float-precision-lost` | A 9-digit `isbn`: mine zero-pads it, then calls it a bad check digit; Kristina's calls it the wrong length. Plus the name difference for the lost-digit `isbn13`. |
| 1 | `isbn`: `bad-characters` | `isbn`: `invalid-characters` | Different name for a letter inside an ISBN. |
| 1 | `isbn`: `bad-length` | `isbn`: `wrong-length` | Different name for an ISBN that's the wrong length. |

Every book in each group:

<details><summary>566 book(s): mine no-usable-isbn / Kristina's no-usable-isbn</summary>

| goodreads_book_id | Book | Original value(s) |
|---|---|---|
| 353 | Time Enough for Love | *(blank text)* |
| 7190 | The Three Musketeers | *(blank text)* |
| 7604 | Lolita | *(blank text)* |
| 10374 | Hard-Boiled Wonderland and the End of the World | *(blank text)* |
| 10975 | The Sound and the Fury | *(blank text)* |
| 15055 | Oranges Are Not the Only Fruit | *(blank text)* |
| 17660 | The Tommyknockers | *(blank text)* |
| 17716 | Waiting for Godot | *(blank text)* |
| 30013 | Prelude to Foundation | *(blank text)* |
| 34511 | Monstrous Regiment (Discworld, #31; Industrial Revolution, #3) | *(blank text)* |
| 49552 | The Stranger | *(blank text)* |
| 59978 | Sin City, Vol. 4: That Yellow Bastard (Sin City, #4) | *(blank text)* |
| 71458 | Stupeur et tremblements | *(blank text)* |
| 95558 | Solaris | *(blank text)* |
| 114170 | Then Came You (The Gamblers, #1) | *(blank text)* |
| 140302 | Poirot Investiga (Hércules Poirot, #3) | *(blank text)* |
| 153785 | Page (Protector of the Small, #2) | *(blank text)* |
| 153795 | Squire (Protector of the Small, #3) | *(blank text)* |
| 153800 | Lady Knight (Protector of the Small, #4) | *(blank text)* |
| 313256 | Dark Challenge (Dark, #5) | *(blank text)* |
| 356373 | Experiencing God: Knowing and Doing the Will of God, Workbook | *(blank text)* |
| 364826 | سینوهه | *(blank text)* |
| 434229 | Cape Fear | *(blank text)* |
| 536790 | Trumps of Doom (The Chronicles of Amber, #6) | *(blank text)* |
| 581552 | In the Penal Colony | *(blank text)* |
| 606818 | Holy Blood, Holy Grail | *(blank text)* |
| 646462 | The Qur'an / القرآن الكريم | *(blank text)* |
| 682745 | The Basketball Diaries | *(blank text)* |
| 716696 | رباعيات خيام | *(blank text)* |
| 769658 | Battlefield Earth: A Saga of the Year 3000 | *(blank text)* |
| 887201 | Faeries | *(blank text)* |
| 1268479 | Warbreaker (Warbreaker, #1) | *(blank text)* |
| 1499952 | Daddy-Long-Legs (Daddy-Long-Legs, #1) | *(blank text)* |
| 1772910 | White Nights | *(blank text)* |
| 1876770 | Chrzest ognia (Saga o Wiedźminie, #5) | *(blank text)* |
| 1923820 | Holy Bible: King James Version | *(blank text)* |
| 2122216 | Special A, Vol. 1 (Special A, #1) | *(blank text)* |
| 2548866 | James Potter and the Hall of Elders' Crossing (James Potter, #1) | *(blank text)* |
| 2678349 | استمتع بحياتك | *(blank text)* |
| 2750180 | لا تحزن | *(blank text)* |
| 3243517 | رأيت رام الله | *(blank text)* |
| 3331756 | عائد إلى حيفا | *(blank text)* |
| 3338544 | رحلتي من الشك إلى الإيمان | *(blank text)* |
| 3491072 | حول العالم في 200 يوم | *(blank text)* |
| 3554772 | عزازيل | *(blank text)* |
| 3831279 | ڤيرتيجو | *(blank text)* |
| 4502877 | Midnight Sun (Twilight, #1.5) | *(blank text)* |
| 4527502 | The Scarecrow (Jack McEvoy, #2) | *(blank text)* |
| 4653511 | رجال في الشمس | *(blank text)* |
| 5048174 | 2BR02B | *(blank text)* |
| 5061675 | A Game of Thrones / A Clash of Kings (A Song of Ice and Fire, #1-2) | *(blank text)* |
| 5153799 | Father Mine (Black Dagger Brotherhood, #6.5) | *(blank text)* |
| 5295735 | الحرافيش | *(blank text)* |
| 5607622 | قمر على سمرقند | *(blank text)* |
| 5664022 | حوار مع صديقي الملحد | *(blank text)* |
| 5883777 | The Holy Bible: English Standard Version | *(blank text)* |
| 6251012 | UR | *(blank text)* |
| 6324090 | Alice's Adventures in Wonderland | *(blank text)* |
| 6357022 | Club Shadowlands (Masters of the Shadowlands, #1) | *(blank text)* |
| 6387565 | Witch & Wizard (Witch & Wizard, #1) | *(blank text)* |
| 6388558 | The Warlord Wants Forever (Immortals After Dark #1) | *(blank text)* |
| 6395833 | Guts | *(blank text)* |
| 6506085 | Food Inc.: A Participant Guide: How Industrial Food is Making Us Sicker, Fatter, and Poorer-And What You Can Do About It | *(blank text)* |
| 6604887 | أنت لي | *(blank text)* |
| 6614886 | زغازيغ | *(blank text)* |
| 6630751 | First to Kill (Nathan McBride, #1) | *(blank text)* |
| 7704143 | تراب الماس | *(blank text)* |
| 7743783 | The Unidentified Redhead (Redhead, #1) | *(blank text)* |
| 7785207 | The Mating  (Law of the Lycans, #2) | *(blank text)* |
| 7897478 | The Bedwetter: Stories of Courage, Redemption, and Pee | *(blank text)* |
| 7913305 | The Immortals of Meluha (Shiva Trilogy, #1) | *(blank text)* |
| 7981206 | Dead Reckoning (Sookie Stackhouse, #11) | *(blank text)* |
| 8113940 | Witches of East End (The Beauchamp Family, #1) | *(blank text)* |
| 8135807 | Rock Me (Ross Siblings, #2) | *(blank text)* |
| 8152697 | Wishin' and Hopin' | *(blank text)* |
| 8177526 | Fate (My Blood Approves, #2) | *(blank text)* |
| 8428984 | Half Way Home | *(blank text)* |
| 8575295 | Wisdom (My Blood Approves, #4) | *(blank text)* |
| 8593026 | Hostile Witness (Witness Series, #1) | *(blank text)* |
| 9279734 | Forever Mine (The Moreno Brothers, #1) | *(blank text)* |
| 9305362 | Captive Prince (Captive Prince, #1) | *(blank text)* |
| 9409469 | The Gray Wolf Throne (Seven Realms, #3) | *(blank text)* |
| 9418327 | Bossypants | *(blank text)* |
| 9496240 | The Hangman's Daughter (The Hangman's Daughter, #1) | *(blank text)* |
| 9635657 | Tales from a Not-So-Talented Pop Star (Dork Diaries, #3) | *(blank text)* |
| 9722217 | رغم الفراق | *(blank text)* |
| 9832370 | BookRags Summary:  A Storm of Swords | *(blank text)* |
| 9858714 | The Mind Readers (Mind Readers, #1) | *(blank text)* |
| 9915707 | Endure (Need, #4) | *(blank text)* |
| 9925913 | Shock Wave (Virgil Flowers, #5) | *(blank text)* |
| 10295484 | Heart on a Chain | *(blank text)* |
| 10586539 | Wake (Watersong #1) | *(blank text)* |
| 10599302 | Head Over Heels (Lucky Harbor, #3) | *(blank text)* |
| 10664113 | A Dance with Dragons (A Song of Ice and Fire, #5) | *(blank text)* |
| 10776793 | War Brides | *(blank text)* |
| 10790376 | A Modern Witch (A Modern Witch, #1) | *(blank text)* |
| 10813469 | Rock Chick Renegade (Rock Chick, #4) | *(blank text)* |
| 10813480 | For You (The 'Burg, #1) | *(blank text)* |
| 10830444 | Guilty Wives | *(blank text)* |
| 11096647 | Flat-Out Love (Flat-Out Love, #1) | *(blank text)* |
| 11227040 | Sweet Dreams (Colorado Mountain, #2) | *(blank text)* |
| 11227041 | The Gamble (Colorado Mountain, #1) | *(blank text)* |
| 11227043 | Rock Chick Revenge (Rock Chick, #5) | *(blank text)* |
| 11237412 | Six's Legacy (Lorien Legacies: The Lost Files, #1) | *(blank text)* |
| 11262424 | Between the Lines (Between the Lines, #1) | *(blank text)* |
| 11324166 | Timeless (Parasol Protectorate, #5) | *(blank text)* |
| 11350430 | The Mystery Knight (The Tales of Dunk and Egg, #3) | *(blank text)* |
| 11408650 | The Unbecoming of Mara Dyer (Mara Dyer, #1) | *(blank text)* |
| 11450591 | The Mill River Recluse | *(blank text)* |
| 11479285 | Breathe (Sea Breeze, #1) | *(blank text)* |
| 11505797 | Beautiful Disaster (Beautiful, #1) | *(blank text)* |
| 11561469 | Reason to Breathe (Breathing, #1) | *(blank text)* |
| 11665750 | At Peace (The 'Burg, #2) | *(blank text)* |
| 11757975 | The Look of Love (San Francisco Sullivans, #1; The Sullivans, #1) | *(blank text)* |
| 11784281 | Take This Regret (Take This Regret, #1) | *(blank text)* |
| 11821514 | Long Time Coming | *(blank text)* |
| 11851522 | The Complete Works of H.P. Lovecraft | *(blank text)* |
| 11913681 | The Boyfriend Thief (Stolen Kiss, #1) | *(blank text)* |
| 11947156 | Prince of Wolves (The Grey Wolves, #1) | *(blank text)* |
| 11970096 | Twenty-Eight and a Half Wishes (Rose Gardner Mystery, #1) | *(blank text)* |
| 11970747 | The Hedge Knight (The Tales of Dunk and Egg, #1) | *(blank text)* |
| 11981168 | The One You Love (Emma Holden Suspense Mystery, #1) | *(blank text)* |
| 11985631 | The Sworn Sword (The Tales of Dunk and Egg, #2) | *(blank text)* |
| 12067972 | Where You Are (Between the Lines, #2) | *(blank text)* |
| 12191246 | Second Son (Jack Reacher, #15.5) | *(blank text)* |
| 12254379 | 1Q84 #1-2 (1Q84, #1-2) | *(blank text)* |
| 12287209 | Wool (Wool, #1) | *(blank text)* |
| 12299419 | Mystery Man (Dream Man, #1) | *(blank text)* |
| 12326627 | The White Princess (The Plantagenet and Tudor Novels, #5) | *(blank text)* |
| 12341557 | The Wind Through the Keyhole (The Dark Tower, #4.5) | *(blank text)* |
| 12390650 | Wildest Dreams (Fantasyland, #1) | *(blank text)* |
| 12458287 | The Golden Dynasty (Fantasyland, #2) | *(blank text)* |
| 12583975 | The Billionaire Wins the Game (Billionaire Bachelors, #1) | *(blank text)* |
| 12602078 | The Tycoon's Revenge (Baby for the Billionaire, #1) | *(blank text)* |
| 12647642 | Love Unrehearsed (Love, #2) | *(blank text)* |
| 12652457 | The Broken Eye (Lightbringer, #3) | *(blank text)* |
| 12667194 | Accordance (Significance, #2) | *(blank text)* |
| 12675109 | Great by Choice: Uncertainty, Chaos, and Luck--Why Some Thrive Despite Them All | *(blank text)* |
| 12706435 | Defiance (Significance, #3) | *(blank text)* |
| 12716010 | Rapture (Fallen, #4) | *(blank text)* |
| 12760903 | The Vision (Fallen Star, #3) | *(blank text)* |
| 12799058 | Summerland | *(blank text)* |
| 12842134 | Just One Year (Just One Day, #2) | *(blank text)* |
| 12881141 | Wild Man (Dream Man, #2) | *(blank text)* |
| 12900174 | The Vincent Boys (The Vincent Boys, #1) | *(blank text)* |
| 12902549 | An Invisible Thread: The True Story of an 11-Year-Old Panhandler, a Busy Sales Executive, and an Unlikely Meeting with Destiny | *(blank text)* |
| 12922320 | Criminal (Will Trent, #6) | *(blank text)* |
| 12958487 | Lady Luck (Colorado Mountain, #3) | *(blank text)* |
| 13051316 | The Misremembered Man (Tailorstown #1) | *(blank text)* |
| 13065142 | Rock Chick Reckoning (Rock Chick, #6) | *(blank text)* |
| 13070346 | Blood Rites (The Grey Wolves, #2) | *(blank text)* |
| 13132816 | Emmy & Oliver | *(blank text)* |
| 13146214 | Because of Low (Sea Breeze, #2) | *(blank text)* |
| 13151283 | بضع ساعات في يوم ما | *(blank text)* |
| 13151637 | طه الغريب | *(blank text)* |
| 13178410 | Proper Gauge (Wool, #2) | *(blank text)* |
| 13184572 | The Next Best Thing | *(blank text)* |
| 13184992 | Rock Chick Regret (Rock Chick, #7) | *(blank text)* |
| 13188676 | Ignite Me (Shatter Me, #3) | *(blank text)* |
| 13223520 | Existence (Existence Trilogy, #1) | *(blank text)* |
| 13312527 | The Opportunist (Love Me with Lies, #1) | *(blank text)* |
| 13323842 | Predestined (Existence Trilogy, #2) | *(blank text)* |
| 13363270 | Just One Drop (The Grey Wolves, #3) | *(blank text)* |
| 13369678 | The Vincent Brothers (The Vincent Boys, #2) | *(blank text)* |
| 13372690 | Slammed (Slammed, #1) | *(blank text)* |
| 13402447 | UnEnchanted (An Unfortunate Fairy Tale, #1) | *(blank text)* |
| 13412515 | Law Man (Dream Man, #3) | *(blank text)* |
| 13415554 | The Assassin and the Pirate Lord (Throne of Glass, #0.1) | *(blank text)* |
| 13419891 | The Assassin and the Desert (Throne of Glass, #0.3) | *(blank text)* |
| 13431827 | The Remaining (The Remaining, #1) | *(blank text)* |
| 13453029 | Wool Omnibus (Silo, #1) | *(blank text)* |
| 13489517 | 28 حرف | *(blank text)* |
| 13496084 | Point of Retreat (Slammed, #2) | *(blank text)* |
| 13496738 | While It Lasts (Sea Breeze, #3) | *(blank text)* |
| 13502963 | Indebted (The Premonition, #3) | *(blank text)* |
| 13507011 | Low Pressure | *(blank text)* |
| 13522957 | Feral Sins (The Phoenix Pack, #1) | *(blank text)* |
| 13546173 | The Assassin and the Underworld (Throne of Glass, #0.4) | *(blank text)* |
| 13565676 | The Assassin and the Empire (Throne of Glass, #0.5) | *(blank text)* |
| 13565914 | Knight (Unfinished Hero, #1) | *(blank text)* |
| 13568619 | The Shadowhunter's Codex | *(blank text)* |
| 13569581 | Blood Song (Raven's Shadow, #1) | *(blank text)* |
| 13573795 | Ceaseless (Existence Trilogy, #3) | *(blank text)* |
| 13580846 | My Life with the Walter Boys (My Life with the Walter Boys #1) | *(blank text)* |
| 13600318 | Reckless (Thoughtless, #3) | *(blank text)* |
| 13601550 | Accidentally on Purpose (Accidentally on Purpose, #1) | *(blank text)* |
| 13603717 | First Shift: Legacy (Shift, #1) | *(blank text)* |
| 13612739 | Seduced in the Dark (The Dark Duet, #2) | *(blank text)* |
| 13624367 | Checkmate (Neighbor from Hell, #3) | *(blank text)* |
| 13634927 | A Leaf on the Wind of All Hallows (Outlander, #8.5) | *(blank text)* |
| 13638570 | Out of Breath (Breathing, #3) | *(blank text)* |
| 13643567 | The Evolution of Mara Dyer (Mara Dyer, #2) | *(blank text)* |
| 13765729 | Abducted (Lizzy Gardner #1) | *(blank text)* |
| 14060046 | Obsession | *(blank text)* |
| 14165516 | The Marriage Trap (Marriage to a Billionaire, #2) | *(blank text)* |
| 14740588 | Notorious Nineteen (Stephanie Plum, #19) | *(blank text)* |
| 14745338 | Fairest (An Unfortunate Fairy Tale, #2) | *(blank text)* |
| 15059301 | Captured (The Captive, #1) | *(blank text)* |
| 15062217 | 14 | *(blank text)* |
| 15704001 | Seduction and Snacks (Chocolate Lovers, #1) | *(blank text)* |
| 15717721 | If I Were You (Inside Out, #1) | *(blank text)* |
| 15722284 | Saint Odd (Odd Thomas, #7) | *(blank text)* |
| 15723286 | Curtsies & Conspiracies (Finishing School, #2) | *(blank text)* |
| 15724654 | The Mighty Storm (The Storm, #1) | *(blank text)* |
| 15728921 | Don't Let Me Go | *(blank text)* |
| 15729261 | The Marriage Mistake (Marriage to a Billionaire, #3) | *(blank text)* |
| 15730101 | The Call of Cthulhu | *(blank text)* |
| 15734464 | 12th of Never (Women's Murder Club, #12) | *(blank text)* |
| 15738951 | Deep Down (Jack Reacher, #16.5) | *(blank text)* |
| 15739018 | Taking Chances (Taking Chances, #1) | *(blank text)* |
| 15748335 | Leave Me Breathless (Ross Siblings, #3) | *(blank text)* |
| 15749186 | To All the Boys I've Loved Before (To All the Boys I've Loved Before, #1) | *(blank text)* |
| 15760001 | On Dublin Street (On Dublin Street, #1) | *(blank text)* |
| 15761241 | The Wild Ones (The Wild Ones, #1) | *(blank text)* |
| 15762975 | Wrong Bed, Right Guy (Come Undone, #1) | *(blank text)* |
| 15768536 | Fall From Grace (Mad World, #1) | *(blank text)* |
| 15771862 | Wave | *(blank text)* |
| 15776904 | The Beggar King (The Hangman's Daughter, #3) | *(blank text)* |
| 15778138 | Just for Now (Sea Breeze, #4) | *(blank text)* |
| 15783307 | The Perfect Game (The Perfect Game, #1) | *(blank text)* |
| 15784909 | This Girl (Slammed, #3) | *(blank text)* |
| 15828714 | Sometimes It Lasts (Sea Breeze, #5) | *(blank text)* |
| 15832316 | Dirty Red (Love Me with Lies, #2) | *(blank text)* |
| 15852756 | Naked (The Blackstone Affair, #1) | *(blank text)* |
| 16001443 | All In (The Blackstone Affair, #2) | *(blank text)* |
| 16045855 | Crush (Crush, #1) | *(blank text)* |
| 16047244 | Rock the Heart (Black Falcon, #1) | *(blank text)* |
| 16053316 | Wethering the Storm (The Storm, #2) | *(blank text)* |
| 16056862 | The Unwanted Wife (Unwanted, #1) | *(blank text)* |
| 16066586 | The Cellar (The Cellar, #1) | *(blank text)* |
| 16068905 | Fangirl | *(blank text)* |
| 16070521 | Come Away with Me (With Me in Seattle, #1) | *(blank text)* |
| 16070903 | Fallen Too Far (Rosemary Beach, #1; Too Far, #1) | *(blank text)* |
| 16079228 | Beautifully Damaged (Beautifully Damaged, #1) | *(blank text)* |
| 16081202 | Open Road Summer | *(blank text)* |
| 16081754 | Find You in the Dark (Find You in the Dark, #1) | *(blank text)* |
| 16084702 | Fifty Shades Duo: Fifty Shades Darker / Fifty Shades Freed (Fifty Shades, #2-3) | *(blank text)* |
| 16090636 | Fight with Me (With Me in Seattle, #2) | *(blank text)* |
| 16090981 | Thief (Love Me with Lies, #3) | *(blank text)* |
| 16093188 | Up to Me (The Bad Boys, #2) | *(blank text)* |
| 16096873 | Revealed (House of Night, #11) | *(blank text)* |
| 16102880 | Bad Rep (Bad Rep, #1) | *(blank text)* |
| 16113791 | The Coincidence of Callie & Kayden (The Coincidence, #1) | *(blank text)* |
| 16117182 | Broken Silence (Silence, #2) | *(blank text)* |
| 16117804 | The Proposal (The Proposition, #2) | *(blank text)* |
| 16122643 | Eyes Wide Open (The Blackstone Affair, #3) | *(blank text)* |
| 16124019 | Waking Up Married (Waking Up, #1) | *(blank text)* |
| 16130986 | An Innocent Client | *(blank text)* |
| 16131484 | The Infinite Sea (The 5th Wave, #2) | *(blank text)* |
| 16134551 | Fallen Crest High (Fallen Crest High, #1) | *(blank text)* |
| 16134782 | In Flight (Up in the Air, #1) | *(blank text)* |
| 16136959 | Mile High (Up in the Air, #2) | *(blank text)* |
| 16139641 | Grounded (Up in the Air, #3) | *(blank text)* |
| 16140036 | This Man (This Man, #1) | *(blank text)* |
| 16143347 | We Were Liars | *(blank text)* |
| 16148398 | Saga #1 | *(blank text)* |
| 16148938 | Second Shift: Order (Shift, #2) | *(blank text)* |
| 16150119 | Wired (Wired, #1) | *(blank text)* |
| 16150996 | Convicted (Consequences, #3) | *(blank text)* |
| 16151178 | The Sea of Tranquility | *(blank text)* |
| 16163690 | Own the Wind (Chaos, #1) | *(blank text)* |
| 16174197 | Knight & Play (Knight, #1) | *(blank text)* |
| 16175040 | Endless Knight (The Arcana Chronicles, #2) | *(blank text)* |
| 16233105 | Someone to Love (Someone to Love, #1) | *(blank text)* |
| 16299256 | The Game Changer (The Perfect Game, #2) | *(blank text)* |
| 16299991 | A Quest of Heroes (The Sorcerer's Ring, #1) | *(blank text)* |
| 16301111 | Always You (Best Friend, #1) | *(blank text)* |
| 16429619 | The Kiss of Deception (The Remnant Chronicles, #1) | *(blank text)* |
| 16704759 | Knight & Stay (Knight, #2) | *(blank text)* |
| 17158513 | Captive Prince: Volume Two (Captive Prince, #2) | *(blank text)* |
| 17158596 | Collide (Collide, #1) | *(blank text)* |
| 17166702 | True Love Story | *(blank text)* |
| 17181905 | The Arrangement: The Ferro Family (The Arrangement, #1) | *(blank text)* |
| 17191012 | Fallen Crest Family (Fallen Crest High, #2) | *(blank text)* |
| 17200687 | Rule (Marked Men, #1) | *(blank text)* |
| 17201110 | Safe with Me (With Me in Seattle, #5) | *(blank text)* |
| 17204568 | Crazy Little Thing (Bell Harbor, #1) | *(blank text)* |
| 17204860 | Jet (Marked Men, #2) | *(blank text)* |
| 17228280 | Better off Friends | *(blank text)* |
| 17235347 | Life Before Legend: Stories of the Criminal and the Prodigy (Legend, #0.5) | *(blank text)* |
| 17255265 | This Man Confessed (This Man, #3) | *(blank text)* |
| 17257484 | Trouble | *(blank text)* |
| 17257990 | Fire Inside (Chaos, #2) | *(blank text)* |
| 17257993 | Raid (Unfinished Hero, #3) | *(blank text)* |
| 17267122 | Pulse (Collide, #2) | *(blank text)* |
| 17286162 | Forever Black (Forever, #1) | *(blank text)* |
| 17306293 | Shift (Silo, #2) | *(blank text)* |
| 17314410 | Beauty from Surrender (Beauty, #2) | *(blank text)* |
| 17317675 | Epilogue (The Dark Duet, #3) | *(blank text)* |
| 17333880 | Twisted Perfection (Rosemary Beach, #5; Perfection, #1) | *(blank text)* |
| 17337562 | Forever Too Far (Rosemary Beach, #3; Too Far, #3) | *(blank text)* |
| 17340050 | Losing Hope (Hopeless, #2) | *(blank text)* |
| 17375956 | Reaper's Property (Reapers MC, #1) | *(blank text)* |
| 17377032 | Bad Things (Tristan & Danika, #1) | *(blank text)* |
| 17401198 | Only the Innocent (DCI Tom Douglas #1) | *(blank text)* |
| 17404452 | Forever You (Forever, #2) | *(blank text)* |
| 17406847 | Defy (Defy, #1) | *(blank text)* |
| 17407233 | The Submissive (Submissive, #1) | *(blank text)* |
| 17449417 | Simple Perfection (Rosemary Beach, #6; Perfection, #2) | *(blank text)* |
| 17455541 | Happy, Happy, Happy | *(blank text)* |
| 17455585 | White Hot Kiss (The Dark Elements, #1) | *(blank text)* |
| 17455815 | Stone Cold Touch (The Dark Elements, #2) | *(blank text)* |
| 17504320 | Taking Shots (Assassins, #1) | *(blank text)* |
| 17524166 | نادي السيارات | *(blank text)* |
| 17557143 | The Billionaire's Obsession ~ Simon (The Billionaire's Obsession, #1) | *(blank text)* |
| 17558817 | Be with Me (Wait for You, #2) | *(blank text)* |
| 17560674 | The Bet (The Bet, #1) | *(blank text)* |
| 17563080 | Murder of Crows (The Others, #2) | *(blank text)* |
| 17563539 | The Egg | *(blank text)* |
| 17570538 | The Blood Mirror (Lightbringer, #4) | *(blank text)* |
| 17667452 | When I Found You | *(blank text)* |
| 17667561 | The Shadow Throne (The Ascendance Trilogy, #3) | *(blank text)* |
| 17673307 | Neanderthal Seeks Human (Knitting in the City, #1) | *(blank text)* |
| 17729712 | Beautiful Broken Rules (Broken, #1) | *(blank text)* |
| 17733861 | A Shade of Blood (A Shade of Vampire, #2) | *(blank text)* |
| 17788401 | Ugly Love | *(blank text)* |
| 17792606 | Mine (Real, #2) | *(blank text)* |
| 17794657 | The Lake (The Lake Trilogy #1) | *(blank text)* |
| 17798233 | Rome (Marked Men, #3) | *(blank text)* |
| 17798287 | Driven (Driven, #1) | *(blank text)* |
| 17825503 | Leo | *(blank text)* |
| 17830559 | Remy (Real, #3) | *(blank text)* |
| 17831614 | Beautiful Player (Beautiful Bastard, #3) | *(blank text)* |
| 17831616 | Beautiful Bitch (Beautiful Bastard, #1.5) | *(blank text)* |
| 17831617 | Beautiful Bombshell (Beautiful Bastard, #2.5) | *(blank text)* |
| 17831619 | Beautiful Beginning (Beautiful Bastard, #3.5) | *(blank text)* |
| 17833099 | Price of a Kiss (Forbidden Men, #1) | *(blank text)* |
| 17835351 | Nikola Tesla: Imagination and the Man That Invented the 20th Century | *(blank text)* |
| 17835766 | One More Chance (Rosemary Beach, #8; Chance, #2) | *(blank text)* |
| 17835773 | Misbehaving (Sea Breeze, #6) | *(blank text)* |
| 17860217 | Trust in Me (Wait for You, #1.5) | *(blank text)* |
| 17880708 | Fueled (Driven, #2) | *(blank text)* |
| 17880714 | Crashed (Driven, #3) | *(blank text)* |
| 17925397 | A Castle of Sand (A Shade of Vampire, #3) | *(blank text)* |
| 17927395 | A Court of Mist and Fury (A Court of Thorns and Roses, #2) | *(blank text)* |
| 17950614 | UnDivided (Unwind, #4) | *(blank text)* |
| 17970255 | Into the Deep (Into the Deep, #1) | *(blank text)* |
| 17973653 | Shine Not Burn (Shine Not Burn, #1) | *(blank text)* |
| 17977710 | Twisted (Tangled, #2) | *(blank text)* |
| 17985262 | CyberStorm | *(blank text)* |
| 17989312 | The Sisterhood | *(blank text)* |
| 17999892 | The Atlantis Gene (The Origin Mystery, #1) | *(blank text)* |
| 18045473 | Last Train to Istanbul | *(blank text)* |
| 18053782 | Take a Chance (Rosemary Beach, #7; Chance, #1) | *(blank text)* |
| 18071296 | Willing Captive | *(blank text)* |
| 18076876 | Reaper's Legacy (Reapers MC, #2) | *(blank text)* |
| 18080889 | Worth the Fight (MMA Fighter, #1) | *(blank text)* |
| 18089551 | Tall, Tatted and Tempting (The Reed Brothers, #1) | *(blank text)* |
| 18104607 | Beautiful Oblivion (The Maddox Brothers, #1) | *(blank text)* |
| 18105011 | Sweet Home (Sweet Home, #1) | *(blank text)* |
| 18108281 | The King (Black Dagger Brotherhood, #12) | *(blank text)* |
| 18108795 | High Heat (Jack Reacher #17.5) | *(blank text)* |
| 18108877 | Timebound (The Chronos Files, #1) | *(blank text)* |
| 18110808 | Fallen Crest Public (Fallen Crest High, #3) | *(blank text)* |
| 18115061 | Before Jamaica Lane (On Dublin Street, #3) | *(blank text)* |
| 18129852 | Rival (Fall Away, #2) | *(blank text)* |
| 18134249 | Ruin (Ruin, #1) | *(blank text)* |
| 18138755 | Forever with You (Fixed, #3) | *(blank text)* |
| 18149927 | Beneath This Man (This Man, #2) | *(blank text)* |
| 18163646 | Falling into Place | *(blank text)* |
| 18191814 | A Blaze of Sun (A Shade of Vampire, #5) | *(blank text)* |
| 18211536 | Rush Too Far (Rosemary Beach, #4; Too Far, #4) | *(blank text)* |
| 18221931 | Carter Reed (Carter Reed, #1) | *(blank text)* |
| 18243828 | Jake Undone (Jake, #1) | *(blank text)* |
| 18244799 | Hardwired (Hacker, #1) | *(blank text)* |
| 18246727 | Mud Vein | *(blank text)* |
| 18282800 | The Ladies' Room | *(blank text)* |
| 18285151 | More Than This (More Than, #1) | *(blank text)* |
| 18297707 | Tangled (Tangled, #1) | *(blank text)* |
| 18323154 | المرحوم | *(blank text)* |
| 18331807 | Vain (The Seven Deadly, #1) | *(blank text)* |
| 18336965 | My Heart and Other Black Holes | *(blank text)* |
| 18340482 | Until Trevor (Until, #2) | *(blank text)* |
| 18341046 | Until November (Until, #1) | *(blank text)* |
| 18363068 | حبيبتي بكماء | *(blank text)* |
| 18387597 | 2 ضباط | *(blank text)* |
| 18405221 | Queen of Fire (Raven's Shadow, #3) | *(blank text)* |
| 18461986 | Deep (Stage Dive, #4) | *(blank text)* |
| 18500665 | End of Days (Penryn & the End of Days, #3) | *(blank text)* |
| 18607805 | Kindle Paperwhite User's Guide | *(blank text)* |
| 18668485 | The Initiate (Divergent, #0.2) | *(blank text)* |
| 18680106 | Hard as It Gets (Hard Ink, #1) | *(blank text)* |
| 18718848 | Mosquitoland | *(blank text)* |
| 18739426 | The Bands of Mourning (Mistborn, #6) | *(blank text)* |
| 18781543 | Until Nico (Until, #4) | *(blank text)* |
| 18799585 | Hidden (Bone Secrets. #1) | *(blank text)* |
| 18800655 | Terms of Enlistment (Frontlines #1) | *(blank text)* |
| 18806240 | Bone Gap | *(blank text)* |
| 18813530 | A Shadow of Light (A Shade of Vampire, #4) | *(blank text)* |
| 18815695 | The Pecan Man | *(blank text)* |
| 18819296 | Hidden | *(blank text)* |
| 18867685 | The Atlantis Plague (The Origin Mystery, #2) | *(blank text)* |
| 18892134 | The Son (Divergent, #0.3) | *(blank text)* |
| 18906484 | The Husband's Secret Free Preview | *(blank text)* |
| 18943009 | Rock Bottom (Tristan & Danika, #2) | *(blank text)* |
| 18982011 | The Line (Witching Savannah, #1) | *(blank text)* |
| 19030845 | Batman: The Dark Knight Returns #1 | *(blank text)* |
| 19095025 | Play (Stage Dive, #2) | *(blank text)* |
| 19103097 | The Magician's Land (The Magicians, #3) | *(blank text)* |
| 19351043 | Nimona | *(blank text)* |
| 19351490 | Grimm's Fairy Tales | *(blank text)* |
| 19549841 | Seraphina (Seraphina, #1) | *(blank text)* |
| 19747756 | House | *(blank text)* |
| 20317106 | هيبتا | *(blank text)* |
| 20329634 | Lines of Departure (Frontlines, #2) | *(blank text)* |
| 20423680 | The Last Town (Wayward Pines, #3) | *(blank text)* |
| 20438825 | Vanished (Callahan & McLane #1) | *(blank text)* |
| 20439328 | How to Be Both | *(blank text)* |
| 20509356 | Sand Omnibus (Sand, #1-5) | *(blank text)* |
| 20525628 | How to Build a Girl | *(blank text)* |
| 20559676 | Killing Sarai (In the Company of Killers, #1) | *(blank text)* |
| 20603820 | The Will (Magdalene, #1) | *(blank text)* |
| 20613920 | Under Locke | *(blank text)* |
| 20620995 | Take Me with You | *(blank text)* |
| 20639274 | Archer's Voice | *(blank text)* |
| 20646604 | Night Owl (Night Owl, #1) | *(blank text)* |
| 20797535 | A Better World (Brilliance Saga, #2) | *(blank text)* |
| 20803953 | Bully (Fall Away, #1) | *(blank text)* |
| 20803962 | Until You (Fall Away, #1.5) | *(blank text)* |
| 20829994 | Percy Jackson's Greek Gods (A Percy Jackson and the Olympians Guide) | *(blank text)* |
| 20874139 | I Am Livia | *(blank text)* |
| 20886354 | Skin Deep (Legion, #2) | *(blank text)* |
| 20894857 | Sleep Tight | *(blank text)* |
| 20980373 | Reasonable Doubt: Volume 2 (Reasonable Doubt, #2) | *(blank text)* |
| 21104828 | The Lake House | *(blank text)* |
| 21219083 | The One That Got Away | *(blank text)* |
| 21411058 | Bad Romeo (Starcrossed, #1) | *(blank text)* |
| 21414439 | Truthwitch (The Witchlands, #1) | *(blank text)* |
| 21418017 | The Space Between (Outlander, #7.5) | *(blank text)* |
| 21420473 | The Fixed Trilogy (Fixed, #1-3) | *(blank text)* |
| 21473305 | Dominic (Slater Brothers, #1) | *(blank text)* |
| 21518647 | Axel (Corps Security, #1) | *(blank text)* |
| 21518679 | Cage (Corps Security, #2) | *(blank text)* |
| 21849362 | The Shadows (Black Dagger Brotherhood, #13) | *(blank text)* |
| 21857294 | Reasonable Doubt: Volume 3 (Reasonable Doubt, #3) | *(blank text)* |
| 21956060 | Monster in His Eyes (Monster in His Eyes, #1) | *(blank text)* |
| 22020052 | It Ain't Me, Babe (Hades Hangmen, #1) | *(blank text)* |
| 22027055 | One Lavender Ribbon | *(blank text)* |
| 22027459 | The Atlantis World (The Origin Mystery, #3) | *(blank text)* |
| 22131009 | Where There's Smoke | *(blank text)* |
| 22296542 | Addicted to You (Addicted, #1) | *(blank text)* |
| 22299763 | Crooked Kingdom (Six of Crows, #2) | *(blank text)* |
| 22319275 | Yellow Crocus | *(blank text)* |
| 22381326 | Half a War (Shattered Sea, #3) | *(blank text)* |
| 22381892 | Killing Patton: The Strange Death of World War II's Most Audacious General | *(blank text)* |
| 22428828 | Welcome to Shadowhunter Academy (Tales from the Shadowhunter Academy, #1) | *(blank text)* |
| 22443261 | The Rithmatist (The Rithmatist, #1) | *(blank text)* |
| 22457201 | Hardpressed (Hacker, #2) | *(blank text)* |
| 22471294 | Black Lies | *(blank text)* |
| 22474626 | Hard Limit (Hacker, #4) | *(blank text)* |
| 22600903 | Where I Belong (Alabama Summer, #1) | *(blank text)* |
| 22611920 | The Hook Up (Game On, #1) | *(blank text)* |
| 22738563 | We Should All Be Feminists | *(blank text)* |
| 22744701 | My Sister's Grave (Tracy Crosswhite #1) | *(blank text)* |
| 22816087 | Seveneves | *(blank text)* |
| 22840421 | My Lady Jane (The Lady Janies, #1) | *(blank text)* |
| 22857396 | Sweet Addiction (Sweet Addiction, #1) | *(blank text)* |
| 22886612 | Nemesis Games (The Expanse, #5) | *(blank text)* |
| 22895264 | Wicked (A Wicked Saga, #1) | *(blank text)* |
| 22914448 | The Dead Key | *(blank text)* |
| 22915460 | The Glassblower | *(blank text)* |
| 22918050 | The Heir (The Selection, #4) | *(blank text)* |
| 22923997 | Overruled (The Legal Briefs, #1) | *(blank text)* |
| 22931009 | Kindle User's Guide | *(blank text)* |
| 23122175 | The Friend Zone (Game On, #2) | *(blank text)* |
| 23158207 | How Google Works | *(blank text)* |
| 23207027 | Three Dark Crowns (Three Dark Crowns, #1) | *(blank text)* |
| 23212667 | All the Missing Girls | *(blank text)* |
| 23252517 | The Law of Moses (The Law of Moses, #1) | *(blank text)* |
| 23355069 | Hero (Hero, #1) | *(blank text)* |
| 23481669 | Maude | *(blank text)* |
| 23485372 | The Master Magician (The Paper Magician Trilogy, #3) | *(blank text)* |
| 23492288 | Hidden Bodies (You, #2) | *(blank text)* |
| 23545800 | Kaleidoscope Hearts (Hearts, #1) | *(blank text)* |
| 23587984 | Maybe Not (Maybe, #1.5) | *(blank text)* |
| 23675858 | Departure | *(blank text)* |
| 23692271 | Sapiens: A Brief History of Humankind | *(blank text)* |
| 23714532 | Beautiful Sacrifice (The Maddox Brothers, #3) | *(blank text)* |
| 23714544 | Beautiful Burn (The Maddox Brothers, #4) | *(blank text)* |
| 23743603 | Miramont's Ghost | *(blank text)* |
| 23745132 | Wreckage | *(blank text)* |
| 23745189 | The Mermaid's Sister | *(blank text)* |
| 24044596 | Kulti | *(blank text)* |
| 24228353 | Trail of Broken Wings | *(blank text)* |
| 24378015 | Never Never (Never Never, #1) | *(blank text)* |
| 24429934 | The Einstein Prophecy | *(blank text)* |
| 24445517 | Maybe Someday (Maybe, #1) | *(blank text)* |
| 24473465 | The English Spy (Gabriel Allon, #15) | *(blank text)* |
| 24473763 | Radiance (Wraith Kings, #1) | *(blank text)* |
| 24488476 | The Fate of Ten (Lorien Legacies, #6) | *(blank text)* |
| 24631990 | Silent Scream (D.I. Kim Stone, #1) | *(blank text)* |
| 24859245 | Stranger Child (DCI Tom Douglas, #4) | *(blank text)* |
| 24920901 | The Deal (Off-Campus, #1) | *(blank text)* |
| 24937499 | Her Final Breath (Tracy Crosswhite, #2) | *(blank text)* |
| 24961498 | The Midwife's Revolt (The Midwife Series, #1) | *(blank text)* |
| 24961531 | The Color of Secrets | *(blank text)* |
| 25041504 | After You (Me Before You, #2) | *(blank text)* |
| 25056528 | Sincerely, Carter (Sincerely Carter, #1) | *(blank text)* |
| 25104491 | The Prettiest One | *(blank text)* |
| 25153134 | Follow You Home | *(blank text)* |
| 25228579 | The Perfect Son | *(blank text)* |
| 25316313 | A Dark Lure | *(blank text)* |
| 25451852 | Dawn of Wonder (The Wakening, #1) | *(blank text)* |
| 25454883 | Never Never: Part Three (Never Never, #3) | *(blank text)* |
| 25507925 | Binge | *(blank text)* |
| 25564446 | The Air He Breathes (Elements, #1) | *(blank text)* |
| 25624089 | Killing Reagan: The Violent Assault That Changed a Presidency | *(blank text)* |
| 25690958 | Year of Yes: How to Dance It Out, Stand In the Sun and Be Your Own Person | *(blank text)* |
| 25693079 | Crooked Little Lies | *(blank text)* |
| 25711641 | Tyrant (King, #2) | *(blank text)* |
| 25801299 | After Anna | *(blank text)* |
| 25802884 | Hollywood Dirt (Hollywood Dirt, #1) | *(blank text)* |
| 25828204 | F*ck Love | *(blank text)* |
| 25837338 | The Girl from Krakow | *(blank text)* |
| 25837341 | The Good Neighbor | *(blank text)* |
| 25866725 | Broken Grace | *(blank text)* |
| 25883848 | The Hating Game | *(blank text)* |
| 25899336 | When Breath Becomes Air | *(blank text)* |
| 25912358 | A Thousand Boy Kisses | *(blank text)* |
| 26061591 | Extreme Prey (Lucas Davenport, #26) | *(blank text)* |
| 26158341 | The Girl With No Past | *(blank text)* |
| 26214866 | In the Clearing (Tracy Crosswhite, #3) | *(blank text)* |
| 26224667 | Wrong (Wrong, #1) | *(blank text)* |
| 26583370 | Life and Other Near-Death Experiences | *(blank text)* |
| 27152124 | Dirty English (English, #1) | *(blank text)* |
| 27207654 | Blood Defense (Samantha Brinkman, #1) | *(blank text)* |
| 27239265 | The Short Drop (Gibson Vaughn, #1) | *(blank text)* |
| 27252717 | The Score (Off-Campus, #3) | *(blank text)* |
| 27362503 | It Ends with Us | *(blank text)* |
| 27401883 | When I'm Gone | *(blank text)* |
| 27406436 | The Baller: A Down and Dirty Football Novel | *(blank text)* |
| 27419654 | The Last Girl (The Dominion Trilogy, #1) | *(blank text)* |
| 27423283 | The Moonlit Garden | *(blank text)* |
| 27810589 | A Death in Sweden | *(blank text)* |
| 27824826 | The Dry (Aaron Falk, #1) | *(blank text)* |
| 27868677 | The House by the Lake | *(blank text)* |
| 28233082 | The Girl In The Ice (Detective Erika Foster, #1) | *(blank text)* |
| 28240855 | The Girl You Lost | *(blank text)* |
| 28477789 | Stuck-Up Suit | *(blank text)* |
| 28678119 | Paper Princess (The Royals, #1) | *(blank text)* |
| 28698036 | Secret History (Mistborn, #3.5) | *(blank text)* |
| 28802599 | The Light of the Fireflies | *(blank text)* |
| 28959148 | We're All Damaged | *(blank text)* |
| 29103028 | The Queen's Poisoner (Kingfountain, #1) | *(blank text)* |
| 29104680 | Punk 57 | *(blank text)* |
| 29354916 | The Whistler | *(blank text)* |
| 29367958 | The Wall of Winnipeg and Me | *(blank text)* |
| 29610595 | Too Late | *(blank text)* |
| 29632984 | The Things We Wish Were True | *(blank text)* |
| 29639736 | Everything We Keep (Everything We Keep, #1) | *(blank text)* |
| 29925715 | The Sister | *(blank text)* |
| 29981261 | The Butterfly Garden (The Collector #1) | *(blank text)* |
| 29991719 | Royally Screwed (Royally, #1) | *(blank text)* |
| 30002998 | Two By Two | *(blank text)* |
| 30065028 | Fantastic Beasts and Where to Find Them: The Original Screenplay | *(blank text)* |
| 30253700 | Anti-Stepbrother | *(blank text)* |
| 30314465 | No Man's Land (John Puller, #4) | *(blank text)* |
| 30364931 | Neighbor Dearest | *(blank text)* |
| 30831912 | Norse Mythology | *(blank text)* |
| 30839185 | Vicious (Sinners of Saint, #1) | *(blank text)* |
| 31140847 | Bossman | *(blank text)* |
| 31176886 | The Chemist | *(blank text)* |
| 31194270 | Evelyn, After | *(blank text)* |
| 31538647 | Hogwarts: An Incomplete and Unreliable Guide (Pottermore Presents, #3) | *(blank text)* |
| 33288638 | Wait for It | *(blank text)* |
| 90010010 | Untitled Manuscript | *(blank text)* |

</details>

<details><summary>111 book(s): mine lost-precision / Kristina's float-precision-lost</summary>

| goodreads_book_id | Book | Original value(s) |
|---|---|---|
| 4865 | How to Win Friends and Influence People | `9.78067172365e+12` |
| 7194 | The Club Dumas | `9.78015603283e+12` |
| 8732 | The Red Pony | `9.78014196282e+12` |
| 8952 | Killers of the Dawn (Cirque Du Freak, #9) | `9.78031601667e+12` |
| 8957 | Tunnels of Blood (Cirque Du Freak, #3) | `9.78031690573e+12` |
| 8965 | The Vampire's Assistant (Cirque Du Freak, #2) | `9.78031690572e+12` |
| 17810 | In the Miso Soup | `9.7801430357e+12` |
| 18130 | A Wind in the Door (A Wrinkle in Time Quintet, #2) | `9.78044048762e+12` |
| 19000 | The Constant Gardener | `9.7807432872e+12` |
| 19494 | The Spy Who Came In from the Cold | `9.78074344253e+12` |
| 24019 | The New Best Recipe | `9.78093618475e+12` |
| 24766 | The Secret Hour (Midnighters, #1) | `9.78006051954e+12` |
| 32423 | Watchers | `9.7804251888e+12` |
| 43325 | Nothing Lasts Forever | `9.78044635474e+12` |
| 49245 | His Needs, Her Needs: Building an Affair-Proof Marriage | `9.78080071789e+12` |
| 56674 | Empire of the Sun (Empire of the Sun, #1) | `9.78074326523e+12` |
| 61915 | Falling Free (Vorkosigan Saga, #4) | `9.78188677854e+12` |
| 82817 | Zoya | `9.78987566161e+12` |
| 84525 | What Got You Here Won't Get You There: How Successful People Become Even More Successful | `9.78178125156e+12` |
| 105189 | The Story of a Shipwrecked Sailor | `9.78014015755e+12` |
| 114954 | The Opal Deception  (Artemis Fowl, #4) | `9.781423104e+12` |
| 128711 | The Yacoubian Building | `9.78006087814e+12` |
| 168571 | Shadow Prey (Lucas Davenport, #2) | `9.78042520885e+12` |
| 181077 | Sadako and the Thousand Paper Cranes | `9.78069811803e+12` |
| 190361 | Obsidian Butterfly (Anita Blake, Vampire Hunter, #9) | `9.78051513451e+12` |
| 204479 | Spying in High Heels (High Heels, #1) | `9.7809848574e+12` |
| 262731 | The Definitive Book of Body Language | `9.78055380472e+12` |
| 266904 | The Penderwicks: A Summer Tale of Four Sisters, Two Rabbits, and a Very Interesting Boy (The Penderwicks #1) | `9.78044042048e+12` |
| 337058 | Jacob Have I Loved | `9.78006440369e+12` |
| 374233 | If on a Winter's Night a Traveler | `9.78008861945e+12` |
| 1464757 | Edensor (Tetralogi Laskar Pelangi, #3) | `9.78979122702e+12` |
| 2501453 | عابر سرير | `9.78995389059e+12` |
| 2501455 | فوضى الحواس | `9.78995389058e+12` |
| 2501458 | ذاكرة الجسد | `9.78995389053e+12` |
| 2804776 | One Fifth Avenue | `9.78140139027e+12` |
| 3301759 | The Murders in the Rue Morgue | `9.7814961664e+12` |
| 3320520 | The 3 Mistakes of My Life | `9.78812911373e+12` |
| 3692091 | 1/4 جرام | `9.78977175496e+12` |
| 4212386 | Maryamah Karpov: Mimpi-mimpi Lintang (Tetralogi Laskar Pelangi, #4) | `9.78979122745e+12` |
| 4566934 | Winter in Tokyo | `9.78979223984e+12` |
| 4634266 | NARUTO -ナルト- 巻ノ四十三 | `9.78408874553e+12` |
| 5557442 | ظل الأفعى | `9.78977092281e+12` |
| 6145711 | The Walking Dead, Vol. 10: What We Become | `9.78160706076e+12` |
| 6621287 | com نسيان | `9.78995389122e+12` |
| 6686671 | Electric Daisy, Vol. 1 (Dengeki Daisy, #1) | `9.78979233558e+12` |
| 6688121 | Negeri 5 Menara (Negeri 5 Menara, #1) | `9.78979224862e+12` |
| 6765740 | Perahu Kertas | `9.78979122778e+12` |
| 6891433 | Panserhjerte (Harry Hole, #8) | `9.78820319552e+12` |
| 7119070 | أحببتك أكثر مما ينبغي | `9.78995371806e+12` |
| 7147831 | Min kamp 1 (Min kamp #1) | `9.78825257459e+12` |
| 7352220 | Black Butler, Vol. 3 (Black Butler, #3) | `9.78979276087e+12` |
| 7701043 | الجزار | `9.78977778055e+12` |
| 7824768 | ليتها تقرأ | `9.7899537151e+12` |
| 8239301 | الطنطورية | `9.78977092829e+12` |
| 8343444 | Daun Yang Jatuh Tak Pernah Membenci Angin | `9.78979225781e+12` |
| 8407173 | Jasper Jones | `9.78174237262e+12` |
| 8542839 | Fire Burn and Cauldron Bubble (Jolie Wilkins, #1) | `9.78145236586e+12` |
| 8635145 | Embrace (The Violet Eden Chapters, #1) | `9.78073441185e+12` |
| 9086994 | Aleph | `9.78857542577e+12` |
| 9666241 | النبطي | `9.78977092938e+12` |
| 10088913 | مخطوطة بن إسحاق: مدينة الموتى | `9.78977629706e+12` |
| 10169662 | Never Knowing | `9.78031259568e+12` |
| 10706934 | بيكاسو وستاربكس | `9.78995356624e+12` |
| 11382346 | That Boy (That Boy, #1) | `9.78061540899e+12` |
| 11808919 | Maid for Love (Gansett Island Series, #1) | `9.78098347544e+12` |
| 11942408 | شاب كشك في رحلة البحث عن الجادون | `9.78977633759e+12` |
| 11995136 | محال | `9.78977093092e+12` |
| 12288282 | Gunmetal Magic (Kate Daniels, #5.5) | `9.78110158519e+12` |
| 12351649 | Perfection (Neighbor from Hell, #2) | `9.78098321255e+12` |
| 12415695 | كخه يا بابا | `9.78995356618e+12` |
| 13345975 | Avoiding Commitment (Avoiding, #1) | `9.78147627142e+12` |
| 13448656 | Motorcycle Man (Dream Man, #4) | `9.78147624895e+12` |
| 13502970 | Incendiary (The Premonition, #4) | `9.78147920712e+12` |
| 13640229 | Creed (Unfinished Hero, #2) | `9.78130116082e+12` |
| 15742039 | Breathe (Colorado Mountain, #4) | `9.78147614539e+12` |
| 15752757 | Rock Chick Revolution (Rock Chick, #8) | `9.78130189562e+12` |
| 15981894 | Devoured (Devoured, #1) | `9.7813001603e+12` |
| 16001893 | Down to You (The Bad Boys, #1) | `9.78130171672e+12` |
| 16031620 | الفيل الأزرق | `9.78977093155e+12` |
| 16042305 | Love Left Behind | `9.78098847441e+12` |
| 16076787 | السنجة | `9.78999219574e+12` |
| 16081961 | الأسود يليق بك | `9.7899532672e+12` |
| 16114861 | Unbeautifully (Undeniable, #2) | `9.78130134567e+12` |
| 16114862 | Unattainable (Undeniable, #3) | `9.7813019853e+12` |
| 16170522 | صانع الظلام | `9.78999219576e+12` |
| 16170625 | المانيفستو | `9.78999219584e+12` |
| 16279715 | Connected (Connections, #1) | `9.78098894191e+12` |
| 17167042 | Fighting for Flight (Fighting, #1) | `9.78130112018e+12` |
| 17190226 | Surrender Your Love (Surrender Your Love, #1) | `9.7814823343e+12` |
| 17339590 | "حكايات فرغلي المستكاوي "حكايتى مع كفر السحلاوية | `9.7897748813e+12` |
| 17800786 | Damaged 2 (Damaged, #2) | `9.78098554735e+12` |
| 17903381 | Diary ng Panget | `9.78971057365e+12` |
| 17930773 | Found in You (Fixed, #2) | `9.7816270402e+12` |
| 18111281 | A Long Way Home | `9.78067007704e+12` |
| 18301124 | Making Faces | `9.78130167387e+12` |
| 18337259 | A Game of Thrones: Comic Book, Issue 1 | `9.78034553615e+12` |
| 18478222 | Twelve Years a Slave | `9.7809897948e+12` |
| 18711993 | فلتغفري | `9.78614432065e+12` |
| 18781540 | Until Lilly (Until, #3) | `9.78131050159e+12` |
| 20316309 | في قلبي أنثى عبرية | `9.78977637644e+12` |
| 20348781 | Loving Mr. Daniels | `9.78069222191e+12` |
| 21394850 | أقوم قيلا | `9.7860301506e+12` |
| 21456940 | 1919 | `9.78977093293e+12` |
| 21843117 | Scoring Wilder | `9.7809904904e+12` |
| 22009741 | The Woman Who Stole My Life | `9.78071815535e+12` |
| 22669832 | Bright Side (Bright Side, #1) | `9.78099114022e+12` |
| 23357188 | Bound by Honor (Born in Blood Mafia Chronicles, #1) | `9.78131173642e+12` |
| 23844390 | The Pact | `9.78150572452e+12` |
| 24480276 | The Versions of Us | `9.78147460016e+12` |
| 25558608 | A Torch Against the Night (An Ember in the Ashes, #2) | `9.78000825045e+12` |
| 27864391 | The Danish Girl | `9.78147460157e+12` |

</details>

<details><summary>25 book(s): mine lost-precision,bad-prefix / Kristina's float-precision-lost</summary>

| goodreads_book_id | Book | Original value(s) |
|---|---|---|
| 2508854 | تاكسي: حواديت المشاوير | `6.22110201718e+12` |
| 3240691 | واحة الغروب | `6.22110201942e+12` |
| 8793878 | The Keeping (Law of the Lycans, #3) | `2.94001108065e+12` |
| 10468258 | The Finding (Law of the Lycans, #5) | `2.94001119121e+12` |
| 10801027 | Cross My Heart (Cross My Heart, #1) | `1.2300000055e+12` |
| 11201007 | Hearts in Darkness (Hearts in Darkness, #1) | `2.94001266893e+12` |
| 11239856 | Maid for the Billionaire (Legacy Collection, #1) | `2.94001248214e+12` |
| 12513614 | Captive in the Dark (The Dark Duet, #1) | `2.94001144494e+12` |
| 12755792 | A Hidden Fire (Elemental Mysteries, #1) | `2.94001328325e+12` |
| 13489518 | Out of the Dark (The Grey Wolves, #4) | `2.94001474615e+12` |
| 13649056 | Try Me (One Night with Sole Regret, #1) | `2.94001463181e+12` |
| 15757434 | Crash (Crash, #1) | `2.94001497963e+12` |
| 15762657 | Seducing Cinderella (Fighting for Love, #1) | `2.94001497768e+12` |
| 15835685 | Clash (Crash, #2) | `2.94001513629e+12` |
| 15993374 | Charade (Games, #1) | `2.94001549587e+12` |
| 16109563 | Undeniable (Undeniable, #1) | `2.94004498098e+12` |
| 17032328 | If You Stay (Beautifully Broken, #1) | `2.94001624931e+12` |
| 17201095 | Play with Me (With Me in Seattle, #3) | `2.94001631951e+12` |
| 17201104 | Rock with Me (With Me in Seattle, #4) | `2.94001655433e+12` |
| 17314430 | Wait for You (Wait for You, #1) | `2.94001623192e+12` |
| 17316075 | Second Chance Boyfriend (One Week Girlfriend, #2) | `2.94001648708e+12` |
| 17448960 | Falling into You (Falling, #1) | `2.94001635694e+12` |
| 17948485 | Friend-Zoned (Friend-Zoned, #1) | `2.94004447015e+12` |
| 18468559 | Raw (RAW Family, #1) | `2.94014886112e+12` |
| 20761374 | Reasonable Doubt: Volume 1 (Reasonable Doubt, #1) | `2.94014954334e+12` |

</details>

<details><summary>2 book(s): mine bad-checksum, lost-precision / Kristina's wrong-length, float-precision-lost</summary>

| goodreads_book_id | Book | Original value(s) |
|---|---|---|
| 7603 | Reading Lolita in Tehran | `812971060`, `9.78081297106e+12` |
| 11436 | Rejoice (Redemption, #4) | `84386874`, `9.78084238688e+12` |

</details>

<details><summary>1 book(s): mine bad-characters / Kristina's invalid-characters</summary>

| goodreads_book_id | Book | Original value(s) |
|---|---|---|
| 90010008 | The Glass Aviary | `04390A3483` |

</details>

<details><summary>1 book(s): mine bad-length / Kristina's wrong-length</summary>

| goodreads_book_id | Book | Original value(s) |
|---|---|---|
| 90010009 | Borrowed Light | `15287463097` |

</details>

<details><summary>Every missing-value difference (section 1 above)</summary>

| goodreads_book_id | Book | Column |
|---|---|---|
| 8 | Harry Potter Boxed Set, Books 1-5 (Harry Potter, #1-5) | `original_title` |
| 36 | The Lord of the Rings: Weapons and Warfare | `original_publication_year` |
| 231 | I am Charlotte Simmons | `original_title` |
| 353 | Time Enough for Love | `isbn` |
| 353 | Time Enough for Love | `isbn13` |
| 424 | Slouching Towards Bethlehem | `language_code` |
| 621 | The Automatic Millionaire: A Powerful One-Step Plan to Live and Finish Rich | `language_code` |
| 952 | The Five Love Languages of Children | `language_code` |
| 1052 | The Richest Man in Babylon | `original_title` |
| 1191 | Giada's Family Dinners | `language_code` |
| 1192 | Everyday Italian: 125 Simple and Delicious Recipes | `language_code` |
| 1303 | The 48 Laws of Power | `language_code` |
| 1305 | Gates of Fire: An Epic Novel of the Battle of Thermopylae | `language_code` |
| 1540 | The Oedipus Cycle: Oedipus Rex/Oedipus at Colonus/Antigone (The Theban Plays, #1–3) | `original_title` |
| 1635 | Execution: The Discipline of Getting Things Done | `original_title` |
| 1846 | Wild at Heart: Discovering the Secret of a Man's Soul | `original_title` |
| 1897 | Eiger Dreams: Ventures Among Men and Mountains | `language_code` |
| 2002 | Harry Potter Schoolbooks Box Set: Two Classic Books from the Library of Hogwarts School of Witchcraft and Wizardry | `original_title` |
| 2142 | Blink | `language_code` |
| 2615 | The Innovator's Dilemma: The Revolutionary Book that Will Change the Way You Do Business (Collins Business Essentials) | `language_code` |
| 2743 | The Lost Boy (Dave Pelzer #2) | `original_title` |
| 2915 | The River (Brian's Saga, #2) | `language_code` |
| 2978 | Lost Horizon | `language_code` |
| 3028 | Economics in One Lesson: The Shortest & Surest Way to Understand Basic Economics | `language_code` |
| 3049 | Sir Gawain and the Green Knight  | `language_code` |
| 3379 | All Families are Psychotic | `language_code` |
| 3431 | The Five People You Meet in Heaven | `language_code` |
| 3579 | The Complete Anne of Green Gables Boxed Set (Anne of Green Gables, #1-8) | `language_code` |
| 3586 | The Complete Sherlock Holmes, Vol 2 | `language_code` |
| 3648 | The Emperor's Children | `language_code` |
| 3882 | Rachael Ray 365: No Repeats: A Year of Deliciously Different Dinners | `language_code` |
| 3885 | The Taste of Home Cookbook | `language_code` |
| 3888 | The America's Test Kitchen Family Cookbook | `language_code` |
| 4031 | Lunar Park | `language_code` |
| 4076 | In Search of Excellence: Lessons from America's Best-Run Companies | `language_code` |
| 4214 | Life of Pi | `language_code` |
| 4268 | How to Be Good | `language_code` |
| 4507 | Sickened: The Memoir of a Munchausen by Proxy Childhood | `language_code` |
| 4538 | The View from Saturday | `language_code` |
| 4633 | Islands in the Stream | `language_code` |
| 4652 | In Our Time | `language_code` |
| 4657 | The Water-Method Man | `language_code` |
| 4659 | A Widow for One Year | `language_code` |
| 4708 | The Beautiful and Damned | `language_code` |
| 4865 | How to Win Friends and Influence People | `isbn` |
| 4865 | How to Win Friends and Influence People | `isbn13` |
| 4898 | Blue Ocean Strategy: How To Create Uncontested Market Space And Make The Competition Irrelevant | `language_code` |
| 5052 | Code to Zero | `language_code` |
| 5068 | Last Orders | `language_code` |
| 5181 | Jewel | `language_code` |
| 5198 | Paradise | `original_title` |
| 5326 | A Christmas Carol | `language_code` |
| 5348 | The Testament | `language_code` |
| 5350 | The Partner | `language_code` |
| 5354 | The Brethren | `language_code` |
| 5369 | The Amber Room | `language_code` |
| 5508 | Anne Frank: Beyond the Diary - A Photographic Remembrance | `language_code` |
| 5517 | A Raisin in the Sun | `language_code` |
| 5552 | QED: The Strange Theory of Light and Matter | `language_code` |
| 5697 | The Complete Short Novels | `original_title` |
| 5946 | In the Skin of a Lion | `language_code` |
| 6193 | Life and Times of Michael K | `language_code` |
| 6328 | Revolting Rhymes | `language_code` |
| 6520 | My Friend Leonard | `language_code` |
| 6554 | Darkness | `language_code` |
| 6596 | The Four Agreements: A Practical Guide to Personal Freedom | `language_code` |
| 6613 | Four Blondes | `language_code` |
| 6670 | The Magic Finger (Young Puffin Developing Reader) | `original_title` |
| 6687 | Charlie and the Great Glass Elevator (Charlie Bucket, #2) | `language_code` |
| 6690 | Danny the Champion of the World | `language_code` |
| 6697 | Little Altars Everywhere | `language_code` |
| 6709 | Practicing the Power of Now: Essential Teachings, Meditations, and Exercises from the Power of Now | `language_code` |
| 6750 | The Broom of the System | `language_code` |
| 6820 | number9dream | `language_code` |
| 6862 | Amsterdam | `language_code` |
| 6882 | Papillon | `language_code` |
| 7073 | A Son of the Circus | `language_code` |
| 7184 | Twenty Years After (The D'Artagnan Romances, #2) | `language_code` |
| 7190 | The Three Musketeers | `isbn` |
| 7190 | The Three Musketeers | `isbn13` |
| 7190 | The Three Musketeers | `language_code` |
| 7194 | The Club Dumas | `isbn` |
| 7194 | The Club Dumas | `isbn13` |
| 7201 | As the Crow Flies | `language_code` |
| 7329 | Unfinished Tales of Númenor and Middle-Earth | `language_code` |
| 7389 | Runaways, Vol. 1: Pride and Joy (Runaways, #1) | `original_title` |
| 7433 | Messenger of Truth (Maisie Dobbs, #4) | `language_code` |
| 7455 | Sex and the City | `language_code` |
| 7603 | Reading Lolita in Tehran | `isbn` |
| 7603 | Reading Lolita in Tehran | `isbn13` |
| 7604 | Lolita | `isbn` |
| 7604 | Lolita | `isbn13` |
| 7628 | The Good Soldier | `language_code` |
| 7670 | The Andromeda Strain | `language_code` |
| 7673 | Eaters of the Dead | `language_code` |
| 7675 | Disclosure | `language_code` |
| 7682 | The Great Train Robbery | `language_code` |
| 7707 | Pygmalion & My Fair Lady | `language_code` |
| 7742 | Ahab's Wife, or The Star-Gazer | `original_title` |
| 7769 | Dr. Seuss's ABC: An Amazing Alphabet Book! (Bright and Early Board Books) | `original_title` |
| 7770 | One Fish, Two Fish, Red Fish, Blue Fish | `language_code` |
| 7780 | The Secret Art of Dr. Seuss | `language_code` |
| 7788 | The Cat in the Hat and Other Dr. Seuss Favorites | `language_code` |
| 7882 | On the Banks of Plum Creek  (Little House, #4) | `original_title` |
| 7882 | On the Banks of Plum Creek  (Little House, #4) | `language_code` |
| 7973 | Enchantment | `language_code` |
| 7979 | The Bellmaker (Redwall, #7) | `language_code` |
| 7980 | Pearls of Lutra (Redwall, #9) | `language_code` |
| 7981 | The Long Patrol (Redwall, #10) | `language_code` |
| 7987 | The Legend of Luke (Redwall, #12) | `language_code` |
| 7993 | Mariel of Redwall (Redwall, #4) | `language_code` |
| 7999 | Marlfox (Redwall, #11) | `language_code` |
| 8248 | By the Shores of Silver Lake  (Little House, #5) | `language_code` |
| 8252 | Farmer Boy (Little House, #3) | `language_code` |
| 8282 | The Long Winter (Little House, #6) | `language_code` |
| 8676 | Unlimited Power : The New Science Of Personal Achievement | `language_code` |
| 8696 | Last Chance to See | `language_code` |
| 8732 | The Red Pony | `isbn` |
| 8732 | The Red Pony | `isbn13` |
| 8732 | The Red Pony | `language_code` |
| 8914 | The First World War | `language_code` |
| 8948 | Sons of Destiny (Cirque Du Freak, #12) | `language_code` |
| 8951 | The Lake of Souls (Cirque Du Freak, #10) | `language_code` |
| 8952 | Killers of the Dawn (Cirque Du Freak, #9) | `isbn` |
| 8952 | Killers of the Dawn (Cirque Du Freak, #9) | `isbn13` |
| 8952 | Killers of the Dawn (Cirque Du Freak, #9) | `language_code` |
| 8957 | Tunnels of Blood (Cirque Du Freak, #3) | `isbn` |
| 8957 | Tunnels of Blood (Cirque Du Freak, #3) | `isbn13` |
| 8957 | Tunnels of Blood (Cirque Du Freak, #3) | `language_code` |
| 8962 | A Living Nightmare (Cirque Du Freak, #1) | `language_code` |
| 8963 | Hunters of the Dusk (Cirque Du Freak, #7) | `language_code` |
| 8965 | The Vampire's Assistant (Cirque Du Freak, #2) | `isbn` |
| 8965 | The Vampire's Assistant (Cirque Du Freak, #2) | `isbn13` |
| 8965 | The Vampire's Assistant (Cirque Du Freak, #2) | `language_code` |
| 8966 | Allies of the Night (Cirque du Freak, #8) | `language_code` |
| 8967 | Trials of Death (Cirque Du Freak, #5) | `language_code` |
| 8968 | The Vampire Prince (Cirque Du Freak, #6) | `language_code` |
| 9010 | I Hope They Serve Beer in Hell (Tucker Max, #1) | `language_code` |
| 9300 | Watermelon (Walsh Family, #1) | `language_code` |
| 9302 | The Other Side of the Story | `language_code` |
| 9370 | Skinny Legs and All | `language_code` |
| 9375 | Fried Green Tomatoes at the Whistle Stop Cafe | `language_code` |
| 9522 | Persepolis, Volume 1 | `original_title` |
| 9526 | Embroideries | `original_title` |
| 9567 | Half Asleep in Frog Pajamas | `language_code` |
| 9569 | Villa Incognito | `language_code` |
| 9589 | Hocus Pocus | `language_code` |
| 9593 | Galápagos | `language_code` |
| 9650 | Burmese Days | `language_code` |
| 9762 | Loving What Is: Four Questions That Can Change Your Life | `language_code` |
| 9822 | Mrs. Frisby and the Rats of NIMH (Rats of NIMH, #1) | `language_code` |
| 9854 | The End of Poverty | `original_title` |
| 9854 | The End of Poverty | `language_code` |
| 10058 | Flags of Our Fathers | `language_code` |
| 10092 | Sea of Silver Light (Otherland, #4) | `language_code` |
| 10155 | The Lost World (Professor Challenger, #1) | `language_code` |
| 10365 | Where the Red Fern Grows | `language_code` |
| 10374 | Hard-Boiled Wonderland and the End of the World | `isbn` |
| 10374 | Hard-Boiled Wonderland and the End of the World | `isbn13` |
| 10395 | How Soccer Explains the World | `language_code` |
| 10506 | The Island of the Day Before | `language_code` |
| 10538 | The Life and Times of the Thunderbolt Kid | `language_code` |
| 10592 | Carrie | `language_code` |
| 10618 | Apt Pupil | `original_title` |
| 10907 | The Pursuit of Happyness | `language_code` |
| 10913 | Keeping Faith | `language_code` |
| 10975 | The Sound and the Fury | `isbn` |
| 10975 | The Sound and the Fury | `isbn13` |
| 11312 | Over Sea, Under Stone (The Dark Is Rising, #1) | `language_code` |
| 11318 | Trouble Is My Business | `original_publication_year` |
| 11413 | Captivating: Unveiling the Mystery of a Woman's Soul | `original_title` |
| 11422 | Redeeming Love | `original_title` |
| 11436 | Rejoice (Redemption, #4) | `isbn` |
| 11436 | Rejoice (Redemption, #4) | `isbn13` |
| 11525 | 1,000 Places to See Before You Die | `language_code` |
| 11564 | The Girl Who Loved Tom Gordon | `language_code` |
| 11713 | The English Patient | `language_code` |
| 11908 | The Adventures of Augie March | `language_code` |
| 12017 | Inversions (Culture, #6) | `language_code` |
| 12204 | The Road Not Taken and Other Poems | `language_code` |
| 12357 | Take the Cannoli | `language_code` |
| 12499 | Belly Laughs: The Naked Truth About Pregnancy and Childbirth | `language_code` |
| 12535 | Plan B: Further Thoughts on Faith | `language_code` |
| 12543 | Bird by Bird: Some Instructions on Writing and Life | `language_code` |
| 12659 | Texas | `language_code` |
| 12839 | A Separate Reality | `language_code` |
| 12923 | The Castle of Otranto | `original_title` |
| 13023 | Alice in Wonderland | `original_title` |
| 13063 | Basket Case | `original_title` |
| 13063 | Basket Case | `language_code` |
| 13132 | 3rd Degree (Women's Murder Club, #3) | `language_code` |
| 13168 | Runaway Ralph (Ralph S. Mouse, #2) | `language_code` |
| 13235 | The Complete Stories and Poems | `language_code` |
| 13350 | Eragon & Eldest (Inheritance, #1-2) | `language_code` |
| 13376 | The House of the Scorpion (Matteo Alacran, #1) | `original_title` |
| 13451 | Storm of the Century: An Original Screenplay | `language_code` |
| 13621 | Death Note, Vol. 7: Zero (Death Note, #7) | `language_code` |
| 13667 | The Farthest Shore (Earthsea Cycle, #3) | `language_code` |
| 13809 | Exile's Return (Conclave of Shadows, #3) | `language_code` |
| 13817 | Shards of a Broken Crown (The Serpentwar Saga, #4) | `language_code` |
| 13891 | Winter's Heart (Wheel of Time, #9) | `original_title` |
| 14118 | Beauty and the Beast (Disney) | `language_code` |
| 14316 | Black Swan Green | `language_code` |
| 14469 | Selected Stories | `language_code` |
| 14480 | Calling Doctor Amelia Bedelia | `language_code` |
| 14481 | Come Back, Amelia Bedelia | `language_code` |
| 14758 | In Her Shoes | `language_code` |
| 14905 | The Complete Novels | `original_title` |
| 14963 | A Wedding in December | `language_code` |
| 14965 | Light on Snow | `language_code` |
| 15055 | Oranges Are Not the Only Fruit | `isbn` |
| 15055 | Oranges Are Not the Only Fruit | `isbn13` |
| 15171 | A Girl Named Zippy | `language_code` |
| 15398 | The Last Days of Dogtown | `language_code` |
| 15433 | Night Mare (Xanth, #6) | `language_code` |
| 15447 | The Source of Magic (Xanth, #2) | `language_code` |
| 15549 | Armageddon's Children (Genesis of Shannara, #1) | `language_code` |
| 15561 | Wizard at Large (Magic Kingdom of Landover, #3) | `language_code` |
| 15645 | Inferno (The Divine Comedy #1) | `language_code` |
| 15676 | Strangers | `language_code` |
| 15752 | By the Light of the Moon | `language_code` |
| 15760 | Dark Rivers of the Heart | `language_code` |
| 15764 | The Amateur Marriage | `language_code` |
| 15779 | Sideways Stories from Wayside School (Wayside School #1) | `original_title` |
| 16055 | The Magician's Assistant | `original_title` |
| 16204 | Daisy Miller | `language_code` |
| 16431 | Sole Survivor | `original_title` |
| 17136 | The Time Machine/The Invisible Man | `language_code` |
| 17324 | The Visitation | `language_code` |
| 17529 | Rebecca of Sunnybrook Farm | `language_code` |
| 17660 | The Tommyknockers | `isbn` |
| 17660 | The Tommyknockers | `isbn13` |
| 17688 | The Metamorphosis, In the Penal Colony, and Other Stories: The Great Short Works of Franz Kafka | `original_title` |
| 17716 | Waiting for Godot | `isbn` |
| 17716 | Waiting for Godot | `isbn13` |
| 17810 | In the Miso Soup | `isbn` |
| 17810 | In the Miso Soup | `isbn13` |
| 18130 | A Wind in the Door (A Wrinkle in Time Quintet, #2) | `isbn` |
| 18130 | A Wind in the Door (A Wrinkle in Time Quintet, #2) | `isbn13` |
| 18420 | Hands Of Light | `language_code` |
| 18452 | The Painted Bird | `original_title` |
| 18452 | The Painted Bird | `language_code` |
| 18580 | Summer of My German Soldier (Summer of My German Soldier, #1) | `language_code` |
| 18884 | Polgara the Sorceress (Malloreon) | `language_code` |
| 18989 | Tinker, Tailor, Soldier, Spy | `language_code` |
| 18999 | Smiley's People | `language_code` |
| 19000 | The Constant Gardener | `isbn` |
| 19000 | The Constant Gardener | `isbn13` |
| 19000 | The Constant Gardener | `language_code` |
| 19001 | A Perfect Spy | `language_code` |
| 19049 | What the Bleep Do We Know!?: Discovering the Endless Possibilities for Altering Your Everyday Reality | `language_code` |
| 19330 | The Complete Tales | `language_code` |
| 19494 | The Spy Who Came In from the Cold | `isbn` |
| 19494 | The Spy Who Came In from the Cold | `isbn13` |
| 19552 | Essentials of Classic Italian Cooking | `language_code` |
| 19691 | The Hunt for Red October (Jack Ryan Universe, #4) | `language_code` |
| 19793 | The Power of Intention: Learning to Co-create Your World Your Way | `language_code` |
| 20082 | The Renegades of Pern (Pern, #10) | `language_code` |
| 20563 | Adam Bede | `language_code` |
| 21025 | The Gift of Therapy: An Open Letter to a New Generation of Therapists and Their Patients | `language_code` |
| 21027 | Love's Executioner and Other Tales of Psychotherapy | `language_code` |
| 21060 | Crown Duel (Crown & Court #1-2) | `language_code` |
| 21340 | City of Night (Dean Koontz's Frankenstein, #2) | `language_code` |
| 21445 | The 5th Horseman (Women's Murder Club, #5) | `language_code` |
| 21683 | Prayers for Rain (Kenzie & Gennaro, #5) | `language_code` |
| 21727 | A Simple Plan | `language_code` |
| 22175 | Strange Pilgrims | `language_code` |
| 22206 | Lullaby | `language_code` |
| 22632 | The Trial and Death of Socrates | `original_title` |
| 22695 | Summer Sisters | `language_code` |
| 22995 | La casa de Bernarda Alba | `language_code` |
| 23196 | The River Why | `language_code` |
| 23422 | The Art of Travel | `language_code` |
| 23454 | Dragons of Winter Night (Dragonlance: Chronicles, #2) | `original_title` |
| 23885 | No One Writes to the Colonel and Other Stories | `language_code` |
| 23965 | Porno | `language_code` |
| 24019 | The New Best Recipe | `isbn` |
| 24019 | The New Best Recipe | `isbn13` |
| 24019 | The New Best Recipe | `language_code` |
| 24096 | Leonardo's Notebooks | `original_title` |
| 24096 | Leonardo's Notebooks | `language_code` |
| 24215 | Alice's Adventures in Wonderland: A Pop-Up Adaptation | `original_title` |
| 24244 | The Black Ice (Harry Bosch, #2; Harry Bosch Universe, #2) | `original_title` |
| 24384 | The Cricket in Times Square | `original_title` |
| 24431 | Trickster's Choice (Daughter of the Lioness, #1) | `original_title` |
| 24766 | The Secret Hour (Midnighters, #1) | `isbn` |
| 24766 | The Secret Hour (Midnighters, #1) | `isbn13` |
| 24938 | Wicked - Piano/Vocal Arrangement | `language_code` |
| 25346 | Out of the Dust | `language_code` |
| 25657 | Sellevision | `language_code` |
| 26324 | Social Intelligence: The New Science of Human Relationships | `language_code` |
| 26661 | Praying God's Word: Breaking Free From Spiritual Strongholds | `language_code` |
| 27037 | Confessions | `language_code` |
| 28212 | And the Band Played On: Politics, People, and the AIDS Epidemic | `language_code` |
| 28940 | Behind the Scenes at the Museum | `language_code` |
| 29034 | Twelve Angry Men | `language_code` |
| 29291 | Make Way for Ducklings | `language_code` |
| 29393 | Our Band Could Be Your Life: Scenes from the American Indie Underground 1981-1991 | `language_code` |
| 29580 | Second Foundation (Foundation #3) | `original_title` |
| 29744 | Goodbye, Columbus and Five Short Stories | `language_code` |
| 29797 | The Pilgrim's Progress | `original_title` |
| 29797 | The Pilgrim's Progress | `language_code` |
| 29801 | Scott Pilgrim, Volume 2: Scott Pilgrim vs. The World | `language_code` |
| 29802 | Scott Pilgrim, Volume 3: Scott Pilgrim & The Infinite Sadness | `language_code` |
| 29948 | The Bridge Across Forever: A True Love Story | `language_code` |
| 30013 | Prelude to Foundation | `isbn` |
| 30013 | Prelude to Foundation | `isbn13` |
| 30071 | The Walking Dead, Book One (The Walking Dead #1-12) | `original_title` |
| 30122 | The Missing Piece | `language_code` |
| 30512 | Paddy Clarke Ha Ha Ha | `language_code` |
| 31168 | Shirley | `language_code` |
| 31231 | The Matarese Circle (Matarese #1) | `language_code` |
| 31266 | The Scarlatti Inheritance | `language_code` |
| 31426 | The Collected Poems | `language_code` |
| 31493 | Standing in the Rainbow (Elmwood Springs, #2) | `original_title` |
| 31741 | Innocent Erendira and Other Stories | `language_code` |
| 31818 | The Philosophy of Andy Warhol (From A to B and Back Again) | `language_code` |
| 31819 | Harry Potter and Philosophy: If Aristotle Ran Hogwarts | `language_code` |
| 32127 | Ina May's Guide to Childbirth | `language_code` |
| 32423 | Watchers | `isbn` |
| 32423 | Watchers | `isbn13` |
| 32423 | Watchers | `language_code` |
| 32429 | Dragon Tears | `language_code` |
| 32442 | Cold Fire | `language_code` |
| 32445 | Strange Highways | `language_code` |
| 32527 | Alone (Detective D.D. Warren, #1) | `original_title` |
| 32552 | Essential Tales and Poems | `original_title` |
| 32559 | The Fall of the House of Usher and Other Tales  | `language_code` |
| 32929 | Goodnight Moon | `original_title` |
| 32987 | The Greatest Generation | `language_code` |
| 33293 | Naked Economics: Undressing the Dismal Science | `language_code` |
| 33335 | The Hidden Messages in Water | `language_code` |
| 33726 | Crazy For You | `language_code` |
| 33770 | Getting Over It | `language_code` |
| 33808 | The Lion's Game (John Corey, #2) | `language_code` |
| 33813 | The Gold Coast | `language_code` |
| 33820 | Up Country | `language_code` |
| 33926 | The Girls' Guide to Hunting and Fishing | `language_code` |
| 34053 | Just So Stories | `language_code` |
| 34072 | Jimmy Corrigan, the Smartest Kid on Earth | `language_code` |
| 34451 | Eat to Live: The Revolutionary Formula for Fast and Sustained Weight Loss | `language_code` |
| 34511 | Monstrous Regiment (Discworld, #31; Industrial Revolution, #3) | `isbn` |
| 34511 | Monstrous Regiment (Discworld, #31; Industrial Revolution, #3) | `isbn13` |
| 34527 | Feet of Clay (Discworld, #19; City Watch, #3) | `language_code` |
| 34548 | If Chins Could Kill: Confessions of a B-Movie Actor | `language_code` |
| 34988 | The Scions of Shannara (Heritage of Shannara, #1) | `original_title` |
| 34993 | The Sum of All Fears (Jack Ryan Universe, #7) | `language_code` |
| 35231 | Lord of Chaos (Wheel of Time, #6) | `original_title` |
| 35233 | The Wheel of Time: Boxed Set #1 (Wheel of Time, #1-3) | `language_code` |
| 35354 | Remember Me | `language_code` |
| 35430 | Path of Destruction (Star Wars: Darth Bane, #1) | `original_title` |
| 36638 | The Wolves of Willoughby Chase (The Wolves Chronicles, #1) | `language_code` |
| 37426 | Little Children | `language_code` |
| 38501 | Ham on Rye | `language_code` |
| 38505 | Hollywood | `language_code` |
| 38990 | Fun Home: A Family Tragicomic | `original_title` |
| 39032 | Mount Dragon | `language_code` |
| 39542 | How to Be a Domestic Goddess: Baking and the Art of Comfort Cooking | `language_code` |
| 39916 | Epileptic | `original_title` |
| 39933 | How to Read Literature Like a Professor: A Lively and Entertaining Guide to Reading Between the Lines | `original_title` |
| 40136 | The Nasty Bits: Collected Varietal Cuts, Usable Trim, Scraps, and Bones | `language_code` |
| 40158 | The Queen of Attolia (The Queen's Thief, #2) | `language_code` |
| 40168 | The Creative License: Giving Yourself Permission to Be The Artist You Truly Are | `language_code` |
| 40173 | Are You There, Vodka? It's Me, Chelsea | `language_code` |
| 40465 | Thank You for Smoking | `language_code` |
| 40470 | Cities of the Plain (The Border Trilogy, #3) | `language_code` |
| 40471 | Outer Dark | `language_code` |
| 40722 | The Sportswriter | `language_code` |
| 41950 | Quentins | `language_code` |
| 42058 | Richard III | `language_code` |
| 42435 | In Harm's Way: The Sinking of the U.S.S. Indianapolis and the Extraordinary Story of Its Survivors | `language_code` |
| 42696 | Trinity | `language_code` |
| 42909 | All Things Wise and Wonderful | `language_code` |
| 43325 | Nothing Lasts Forever | `isbn` |
| 43325 | Nothing Lasts Forever | `isbn13` |
| 43339 | Where Are the Children? | `language_code` |
| 43797 | Pandora / Vittorio the Vampire (New Tales of the Vampires) | `language_code` |
| 43805 | Servant of the Bones | `language_code` |
| 43884 | Phantom (Sword of Truth, #10) | `language_code` |
| 43917 | Rise of a Merchant Prince (The Serpentwar Saga, #2) | `language_code` |
| 43944 | Suite Française | `language_code` |
| 43945 | Portnoy's Complaint | `language_code` |
| 44361 | Velvet Elvis: Repainting the Christian Faith | `language_code` |
| 44688 | Magician's Gambit (The Belgariad, #3) | `language_code` |
| 44796 | The Moon and Sixpence | `language_code` |
| 45108 | Fool's Fate (Tawny Man, #3) | `language_code` |
| 45110 | Shaman's Crossing (Soldier Son, #1) | `language_code` |
| 45260 | The Naked God (Night's Dawn, #3) | `language_code` |
| 45760 | Girl With Curious Hair | `language_code` |
| 46191 | Why Men Love Bitches: From Doormat to Dreamgirl—A Woman's Guide to Holding Her Own in a Relationship | `language_code` |
| 46201 | The Selected Poetry of Rainer Maria Rilke | `original_title` |
| 46460 | Call for the Dead | `language_code` |
| 46676 | When Bad Things Happen to Good People | `language_code` |
| 46913 | FRUiTS | `original_title` |
| 47520 | Castle in the Air (Howl's Moving Castle, #2) | `language_code` |
| 47620 | Grim Tuesday (The Keys to the Kingdom, #2) | `language_code` |
| 47881 | Charlie Bone and the Hidden King (The Children of the Red King, #5) | `language_code` |
| 47922 | Because I'm Worth It (Gossip Girl, #4) | `language_code` |
| 47959 | Queen of the Darkness (The Black Jewels, #3) | `language_code` |
| 48019 | The Effective Executive: The Definitive Guide to Getting the Right Things Done (Harperbusiness Essentials) | `language_code` |
| 48464 | A Good Man is Hard to Find and Other Stories | `language_code` |
| 48811 | Nancy Drew: #1-64 | `original_publication_year` |
| 49006 | The Darkest Hour (Warriors, #6) | `original_title` |
| 49245 | His Needs, Her Needs: Building an Affair-Proof Marriage | `isbn` |
| 49245 | His Needs, Her Needs: Building an Affair-Proof Marriage | `isbn13` |
| 49251 | Citizen Soldiers: The U. S. Army from the Normandy Beaches to the Bulge to the Surrender of Germany | `language_code` |
| 49455 | Notes from Underground | `original_title` |
| 49552 | The Stranger | `isbn` |
| 49552 | The Stranger | `isbn13` |
| 50001 | The Complete Guide to Middle-Earth | `language_code` |
| 50750 | You Slay Me (Aisling Grey #1) | `original_title` |
| 51370 | Leading Change | `original_title` |
| 51370 | Leading Change | `language_code` |
| 52309 | The Autobiography of Benjamin Franklin | `original_title` |
| 53168 | Demon Thief (The Demonata, #2) | `language_code` |
| 54539 | Silas Marner | `language_code` |
| 55229 | April 1865: The Month That Saved America | `language_code` |
| 56157 | The Proper Care and Feeding of Husbands | `language_code` |
| 56405 | Love and Respect: The Love She Most Desires; The Respect He Desperately Needs | `original_title` |
| 56405 | Love and Respect: The Love She Most Desires; The Respect He Desperately Needs | `language_code` |
| 56452 | Now, Discover Your Strengths | `language_code` |
| 56465 | The Gift of Fear: Survival Signals That Protect Us from Violence | `language_code` |
| 56480 | Passion and Purity: Learning to Bring Your Love Life Under Christ's Control | `language_code` |
| 56674 | Empire of the Sun (Empire of the Sun, #1) | `isbn` |
| 56674 | Empire of the Sun (Empire of the Sun, #1) | `isbn13` |
| 56674 | Empire of the Sun (Empire of the Sun, #1) | `language_code` |
| 57605 | Pat the Bunny | `language_code` |
| 58077 | Grave Sight (Harper Connelly, #1) | `original_title` |
| 58547 | Journals | `language_code` |
| 58728 | Anne Frank's Tales from the Secret Annex | `language_code` |
| 59882 | Accident | `original_title` |
| 59882 | Accident | `language_code` |
| 59889 | Safe Harbour | `language_code` |
| 59978 | Sin City, Vol. 4: That Yellow Bastard (Sin City, #4) | `isbn` |
| 59978 | Sin City, Vol. 4: That Yellow Bastard (Sin City, #4) | `isbn13` |
| 60431 | Andy Goldsworthy: A Collaboration with Nature | `language_code` |
| 60551 | The Book on the Taboo Against Knowing Who You Are | `language_code` |
| 60935 | Possessing the Secret of Joy | `language_code` |
| 61665 | Billions & Billions: Thoughts on Life and Death at the Brink of the Millennium | `language_code` |
| 61905 | Barrayar (Vorkosigan Saga, #7) | `original_title` |
| 61915 | Falling Free (Vorkosigan Saga, #4) | `isbn` |
| 61915 | Falling Free (Vorkosigan Saga, #4) | `isbn13` |
| 61938 | The Rowan (The Tower and the Hive, #1) | `original_title` |
| 61942 | The Dragonriders of Pern (Dragonriders of Pern, #1-3) | `language_code` |
| 62479 | Servant of the Shard (Forgotten Realms: Paths of Darkness, #3; The Sellswords, #1) | `original_title` |
| 63432 | 3001: The Final Odyssey (Space Odyssey, #4) | `language_code` |
| 63832 | Blue Highways | `language_code` |
| 64081 | The Irresistible Revolution: Living as an Ordinary Radical | `language_code` |
| 64860 | E is for Evidence (Kinsey Millhone, #5) | `language_code` |
| 64955 | Midnight | `language_code` |
| 65336 | Selected Poems | `language_code` |
| 65840 | Anne of Windy Poplars (Anne of Green Gables, #4) | `language_code` |
| 66655 | Necroscope (Necroscope, #1) | `language_code` |
| 67657 | The Lady & Sons Savannah Country Cookbook | `language_code` |
| 68380 | Dragonlance Chronicles (Dragonlance #1-3) | `language_code` |
| 68429 | The Well of Ascension (Mistborn, #2) | `original_title` |
| 68521 | Excalibur (The Warlord Chronicles, #3) | `language_code` |
| 70287 | The Many Lives & Secret Sorrows of Josephine B. (Josephine Bonaparte, #1) | `language_code` |
| 70420 | The Undercover Economist | `language_code` |
| 71458 | Stupeur et tremblements | `isbn` |
| 71458 | Stupeur et tremblements | `isbn13` |
| 71784 | A New Song (Mitford Years, #5) | `language_code` |
| 71787 | In This Mountain (Mitford Years, #7) | `language_code` |
| 71863 | A Killing Frost (Tomorrow, #3) | `language_code` |
| 71867 | The Other Side of Dawn (Tomorrow, #7) | `language_code` |
| 72978 | Titus Andronicus | `original_title` |
| 73186 | The Case for Christ | `language_code` |
| 73965 | Drinking: A Love Story | `language_code` |
| 73968 | Love Story (Love Story, #1) | `language_code` |
| 74169 | Facing Your Giants: A David and Goliath Story for Everyday People | `language_code` |
| 76237 | The Further Adventures of Sherlock Holmes: After Sir Arthur Conan Doyle (Classic Crime) | `language_code` |
| 76248 | Sherlock Holmes of Baker Street: A Life of the World's First Consulting Detective | `language_code` |
| 76401 | Bury My Heart at Wounded Knee: An Indian History of the American West | `language_code` |
| 76664 | A Spell for Chameleon (Xanth #1) | `language_code` |
| 76668 | For Love of Evil (Incarnations of Immortality, #6) | `language_code` |
| 77161 | Grass for His Pillow (Tales of the Otori, #2) | `language_code` |
| 77295 | Gift from the Sea | `language_code` |
| 77366 | The Hero and the Crown (Damar, #2) | `original_title` |
| 77477 | Blessings | `language_code` |
| 77735 | The Honor of the Queen (Honor Harrington, #2) | `language_code` |
| 77736 | The Short Victorious War (Honor Harrington, #3) | `language_code` |
| 77739 | Honor Among Enemies (Honor Harrington, #6) | `language_code` |
| 78039 | Ramona the Pest (Ramona, #2) | `language_code` |
| 78408 | Lemony Snicket: The Unauthorized Autobiography (A Series of Unfortunate Events companion) | `language_code` |
| 78427 | The Total Money Makeover: A Proven Plan for Financial Fitness | `language_code` |
| 78960 | Good Wives (Little Women, #1.5) | `language_code` |
| 78970 | A Matter of Honor | `language_code` |
| 78982 | Not a Penny More, Not a Penny Less | `language_code` |
| 79006 | Honor Among Thieves | `language_code` |
| 79879 | From Head to Toe | `language_code` |
| 80449 | On the Genealogy of Morals | `language_code` |
| 80534 | Me & Emma | `language_code` |
| 80536 | Little Earthquakes | `language_code` |
| 80568 | Sam's Letters to Jennifer | `language_code` |
| 80670 | Otherwise Known as Sheila the Great (Fudge #2) | `language_code` |
| 80750 | The Covenant (Abram's Daughters, #1) | `language_code` |
| 81939 | The Mastery of Love: A Practical Guide to the Art of Relationship --Toltec Wisdom Book | `language_code` |
| 81948 | The E-Myth Revisited: Why Most Small Businesses Don't Work and What to Do About It | `language_code` |
| 81959 | As a Man Thinketh | `original_title` |
| 82356 | The Comedy of Errors | `original_title` |
| 82356 | The Comedy of Errors | `language_code` |
| 82397 | Richard II | `language_code` |
| 82748 | Sushi for Beginners | `language_code` |
| 82817 | Zoya | `isbn` |
| 82817 | Zoya | `isbn13` |
| 82817 | Zoya | `language_code` |
| 83539 | Fantastic Voyage | `language_code` |
| 83763 | Prey | `language_code` |
| 84351 | The Secret History of the Pink Carnation (Pink Carnation, #1) | `original_title` |
| 84525 | What Got You Here Won't Get You There: How Successful People Become Even More Successful | `isbn` |
| 84525 | What Got You Here Won't Get You There: How Successful People Become Even More Successful | `isbn13` |
| 84525 | What Got You Here Won't Get You There: How Successful People Become Even More Successful | `language_code` |
| 84699 | Never Eat Alone: And Other Secrets to Success, One Relationship at a Time | `language_code` |
| 85321 | The Tenth Justice | `language_code` |
| 85431 | Friday Night Lights: A Town, a Team, and a Dream | `language_code` |
| 85443 | The Lords of Discipline | `language_code` |
| 85987 | Portrait in Sepia | `language_code` |
| 85989 | Princess on the Brink (The Princess Diaries, #8) | `language_code` |
| 85993 | Party Princess (The Princess Diaries, #7) | `language_code` |
| 86172 | A Man in Full | `language_code` |
| 86424 | Lifeguard | `language_code` |
| 86658 | The Secret Agent | `language_code` |
| 87425 | Tintin in Tibet (Tintin, #20) | `original_title` |
| 87632 | Ultramarathon Man: Confessions of an All-Night Runner | `language_code` |
| 87640 | PostSecret: Extraordinary Confessions from Ordinary Lives (PostSecret) | `language_code` |
| 89186 | Pushing Ice | `language_code` |
| 89369 | The Te of Piglet | `original_title` |
| 89375 | 90 Minutes in Heaven: A True Story of Death and Life | `language_code` |
| 89399 | Fortune's Rocks | `language_code` |
| 89731 | Kira-Kira | `original_title` |
| 89959 | The Constitution of the United States of America | `language_code` |
| 90072 | Dr. Seuss's Green Eggs and Ham: For Soprano, Boy Soprano, and Orchestra | `original_publication_year` |
| 90072 | Dr. Seuss's Green Eggs and Ham: For Soprano, Boy Soprano, and Orchestra | `original_title` |
| 90072 | Dr. Seuss's Green Eggs and Ham: For Soprano, Boy Soprano, and Orchestra | `language_code` |
| 90078 | An Essay Concerning Human Understanding | `language_code` |
| 91244 | Beezus and Ramona (Ramona, #1) | `language_code` |
| 91249 | Ramona Forever (Ramona, #7) | `language_code` |
| 91767 | Frida: A Biography of Frida Kahlo | `language_code` |
| 92254 | Angels in America, Part Two: Perestroika | `original_title` |
| 92308 | The Importance of Being Earnest and Other Plays | `original_title` |
| 92371 | Lie Down with Lions | `language_code` |
| 92871 | Brothers Majere (Dragonlance: Preludes, #3) | `language_code` |
| 93000 | Piano/Vocal/Guitar Sheet Music: The Chronicles of Narnia: The Lion, the Witch and The Wardrobe | `language_code` |
| 93276 | King Arthur and His Knights: Selected Tales | `language_code` |
| 93726 | Princess in Training (The Princess Diaries, #6) | `language_code` |
| 93981 | The Interpretation of Dreams | `language_code` |
| 94669 | The Mistress of Spices | `language_code` |
| 94799 | Ghost Soldiers: The Epic Account of World War II's Greatest Rescue Mission | `language_code` |
| 94807 | The Frog and Toad Treasury: Frog and Toad are Friends/Frog and Toad Together/Frog and Toad All Year  (Frog and Toad #1-3) | `language_code` |
| 95558 | Solaris | `isbn` |
| 95558 | Solaris | `isbn13` |
| 95607 | Unveiled: Tamar (Lineage of Grace #1) | `language_code` |
| 95622 | The Last Sin Eater | `language_code` |
| 95658 | Best Friends for Never (The Clique, #2) | `language_code` |
| 95659 | Invasion of the Boy Snatchers (The Clique, #4) | `language_code` |
| 95660 | The Pretty Committee Strikes Back (The Clique, #5) | `language_code` |
| 95661 | Revenge of the Wannabes (The Clique, #3) | `language_code` |
| 95707 | Your Best Life Now: 7 Steps to Living at Your Full Potential | `language_code` |
| 95747 | The Miracle of Mindfulness: An Introduction to the Practice of Meditation | `language_code` |
| 95819 | The Poetry of Robert Frost (Collected Poems, Complete & Unabridged) | `original_title` |
| 96082 | The Last Time They Met | `language_code` |
| 96594 | Fearless (The Lost Fleet, #2) | `language_code` |
| 96642 | Rocket Boys (Coalwood #1) | `language_code` |
| 96980 | Centaur Aisle (Xanth, #4) | `language_code` |
| 97084 | Apathy and Other Small Victories | `language_code` |
| 97860 | Tuesday | `language_code` |
| 98250 | Once a Runner | `language_code` |
| 98427 | The General's Daughter | `language_code` |
| 98687 | Call Me by Your Name | `language_code` |
| 99110 | The Complete Tales and Poems of Winnie-the-Pooh (Winnie-the-Pooh, #1-4) | `original_title` |
| 99452 | Ogre, Ogre (Xanth #5) | `language_code` |
| 99955 | Common Sense, The Rights of Man and Other Essential Writings | `original_title` |
| 102954 | Preacher, Volume 7: Salvation | `language_code` |
| 102958 | Preacher, Volume 9: Alamo | `original_title` |
| 103111 | X-Men: The Dark Phoenix Saga | `original_title` |
| 103902 | Gustav Klimt: 1862-1918 | `language_code` |
| 104734 | The Vagina Monologues | `language_code` |
| 105189 | The Story of a Shipwrecked Sailor | `isbn` |
| 105189 | The Story of a Shipwrecked Sailor | `isbn13` |
| 105760 | Zodiac | `language_code` |
| 106131 | Charlie Bone and the Castle of Mirrors (The Children of the Red King, #4) | `language_code` |
| 107195 | I Kissed Dating Goodbye | `language_code` |
| 107291 | Needful Things | `language_code` |
| 107664 | Raven's Gate (The Gatekeepers, #1) | `language_code` |
| 107670 | Evil Star (The Gatekeepers, #2) | `language_code` |
| 107821 | Bridge of Sighs | `language_code` |
| 109515 | How I Raised Myself from Failure to Success in Selling | `language_code` |
| 110692 | The Redemption of Althalus | `language_code` |
| 111126 | Hateship, Friendship, Courtship, Loveship, Marriage: Stories | `language_code` |
| 112292 | Dauntless (The Lost Fleet, #1) | `language_code` |
| 112872 | A Light in the Window (Mitford Years, #2) | `language_code` |
| 112874 | These High, Green Hills (Mitford Years, #3) | `language_code` |
| 113429 | No One Belongs Here More Than You | `language_code` |
| 113576 | The Smartest Guys in the Room: The Amazing Rise and Scandalous Fall of Enron | `language_code` |
| 114170 | Then Came You (The Gamblers, #1) | `isbn` |
| 114170 | Then Came You (The Gamblers, #1) | `isbn13` |
| 114345 | The Little House Collection (Little House, #1-9) | `language_code` |
| 114954 | The Opal Deception  (Artemis Fowl, #4) | `isbn` |
| 114954 | The Opal Deception  (Artemis Fowl, #4) | `isbn13` |
| 116020 | Walden & Civil Disobedience | `original_title` |
| 116236 | The Education of Little Tree | `language_code` |
| 116295 | Guards! Guards!: The Play | `original_title` |
| 116356 | Footfall | `language_code` |
| 116494 | Anastasia Krupnik (Anastasia Krupnik, #1) | `language_code` |
| 117251 | Hamlet: Screenplay, Introduction And Film Diary | `original_title` |
| 117835 | Nourishing Traditions: The Cookbook That Challenges Politically Correct Nutrition and the Diet Dictocrats | `language_code` |
| 119091 | Taltos (Lives of the Mayfair Witches, #3) | `language_code` |
| 119760 | The Seat of the Soul | `original_title` |
| 120230 | Barefoot Contessa at Home: Everyday Recipes You'll Make Over and Over Again | `language_code` |
| 120461 | Oscar et la dame rose | `language_code` |
| 120840 | David Gets In Trouble | `language_code` |
| 121792 | The Revenge of the Baby-Sat | `language_code` |
| 122212 | Waiting to Exhale (Waiting To Exhale #1) | `language_code` |
| 122574 | Getting Stoned with Savages: A Trip Through the Islands of Fiji and Vanuatu | `language_code` |
| 122967 | The Ugly Duckling | `original_title` |
| 123063 | Under the Skin | `language_code` |
| 123170 | Big Red (Big Red, #1) | `language_code` |
| 125540 | One Day at Horrorland (Goosebumps, #16) | `language_code` |
| 125542 | Stay Out of the Basement  (Goosebumps, #2) | `language_code` |
| 125564 | Night of the Living Dummy (Goosebumps, #7) | `language_code` |
| 125955 | White: The Great Pursuit (The Circle, #3) | `language_code` |
| 125958 | Skin | `language_code` |
| 125963 | Thr3e | `language_code` |
| 126185 | The Christmas Train | `language_code` |
| 126381 | Purple Hibiscus | `language_code` |
| 127451 | Don't Die, My Love | `language_code` |
| 127586 | The White Dragon (Pern, #3) | `language_code` |
| 127970 | The Prize Winner of Defiance, Ohio: How My Mother Raised 10 Kids on 25 Words or Less | `language_code` |
| 128066 | The Pianist: The Extraordinary Story of One Man's Survival in Warsaw, 1939–45 | `language_code` |
| 128711 | The Yacoubian Building | `isbn` |
| 128711 | The Yacoubian Building | `isbn13` |
| 128755 | Cross Bones (Temperance Brennan, #8) | `language_code` |
| 128759 | Fatal Voyage (Temperance Brennan, #4) | `language_code` |
| 129510 | Empire of Ivory (Temeraire, #4) | `language_code` |
| 129565 | Financial Peace Revisited | `language_code` |
| 129947 | The Water is Wide: A Memoir | `language_code` |
| 130260 | Birdman (Jack Caffery, #1) | `language_code` |
| 131304 | Big Bang: The Origin of the Universe | `language_code` |
| 131830 | Women's Bodies, Women's Wisdom: Creating Physical and Emotional Health and Healing | `language_code` |
| 132152 | Streams in the Desert | `language_code` |
| 133445 | The Edible Woman | `language_code` |
| 133906 | The Collected Poems | `language_code` |
| 133954 | Washington Square | `language_code` |
| 134360 | Diane Arbus: Monograph | `language_code` |
| 134958 | Elizabeth: The Struggle for the Throne | `language_code` |
| 136640 | The Codex | `language_code` |
| 136977 | The Places That Scare You: A Guide to Fearlessness in Difficult Times | `language_code` |
| 137792 | Ya Yas in Bloom | `language_code` |
| 139004 | Essays and Poems | `language_code` |
| 139220 | Heat: An Amateur's Adventures as Kitchen Slave, Line Cook, Pasta-Maker, and Apprentice to a Dante-Quoting Butcher in Tuscany | `language_code` |
| 140091 | Real Murders (Aurora Teagarden, #1) | `original_title` |
| 140131 | The Three Little Pigs (Disney Classic) | `language_code` |
| 140302 | Poirot Investiga (Hércules Poirot, #3) | `isbn` |
| 140302 | Poirot Investiga (Hércules Poirot, #3) | `isbn13` |
| 141019 | Snow White and the Seven Dwarfs (Little Golden Book) | `language_code` |
| 141077 | The Kreutzer Sonata | `language_code` |
| 141526 | Pulp | `language_code` |
| 141565 | This Is Your Brain on Music: The Science of a Human Obsession | `language_code` |
| 142108 | Rich Dad's Guide to Investing: What the Rich Invest in That the Poor and Middle Class Do Not! | `language_code` |
| 142900 | The Master Butchers Singing Club | `language_code` |
| 144773 | Contest | `language_code` |
| 147074 | Janet Evanovich Three and Four Two-Book Set (Stephanie Plum, #3-4) | `language_code` |
| 147941 | Figure Drawing for All It's Worth (How to draw and paint) | `language_code` |
| 148337 | Where Eagles Dare  | `language_code` |
| 149196 | Eva Luna | `language_code` |
| 153136 | The Cake Bible | `language_code` |
| 153175 | King of Foxes (Conclave of Shadows, #2) | `language_code` |
| 153492 | The 39 Steps (Richard Hannay, #1) | `language_code` |
| 153542 | Mike Mulligan and His Steam Shovel | `language_code` |
| 153781 | Magic Steps (The Circle Opens, #1) | `language_code` |
| 153785 | Page (Protector of the Small, #2) | `isbn` |
| 153785 | Page (Protector of the Small, #2) | `isbn13` |
| 153795 | Squire (Protector of the Small, #3) | `isbn` |
| 153795 | Squire (Protector of the Small, #3) | `isbn13` |
| 153800 | Lady Knight (Protector of the Small, #4) | `isbn` |
| 153800 | Lady Knight (Protector of the Small, #4) | `isbn13` |
| 153800 | Lady Knight (Protector of the Small, #4) | `language_code` |
| 155370 | Double Identity | `language_code` |
| 155981 | Psycho-Cybernetics, A New Way to Get More Living Out of Life | `language_code` |
| 157076 | The Most Dangerous Game | `language_code` |
| 158516 | The Twelve Chairs | `language_code` |
| 158944 | The Fannie Farmer Cookbook: Anniversary | `language_code` |
| 159418 | Discourse on Method | `original_title` |
| 159760 | Reviving Ophelia: Saving the Selves of Adolescent Girls | `language_code` |
| 160194 | Noises Off | `language_code` |
| 160848 | Wanted | `language_code` |
| 161415 | See You at the Top | `language_code` |
| 164323 | The Google Story: Inside the Hottest Business, Media, and Technology Success of Our Time | `language_code` |
| 164836 | Succulent Wild Woman | `language_code` |
| 165030 | Anybody Out There? (Walsh Family, #4) | `language_code` |
| 165053 | Graffiti World: Street Art from Five Continents | `language_code` |
| 167216 | Amy and Isabelle  | `language_code` |
| 168571 | Shadow Prey (Lucas Davenport, #2) | `isbn` |
| 168571 | Shadow Prey (Lucas Davenport, #2) | `isbn13` |
| 168571 | Shadow Prey (Lucas Davenport, #2) | `original_title` |
| 169718 | Babbitt | `language_code` |
| 169848 | A Christmas Carol, The Chimes and The Cricket on the Hearth | `original_title` |
| 169848 | A Christmas Carol, The Chimes and The Cricket on the Hearth | `language_code` |
| 169871 | Talking to Dragons (Enchanted Forest Chronicles, #4) | `original_title` |
| 169875 | Searching for Dragons (Enchanted Forest Chronicles, #2) | `original_title` |
| 169879 | Calling on Dragons (Enchanted Forest Chronicles, #3) | `original_title` |
| 170171 | Catalyst | `original_title` |
| 170618 | Daddy's Little Girl | `language_code` |
| 170619 | All Around the Town | `language_code` |
| 171102 | The Birth House | `language_code` |
| 173673 | A Course in Miracles | `language_code` |
| 174703 | What to Expect When You're Expecting | `language_code` |
| 174845 | Life Together: The Classic Exploration of Christian Community | `language_code` |
| 174879 | On Becoming a Person: A Therapist's View of Psychotherapy | `language_code` |
| 175004 | Eagle Strike (Alex Rider, #4) | `language_code` |
| 176839 | One True Thing | `language_code` |
| 178599 | Arsenic and Old Lace | `language_code` |
| 179264 | The Madonnas of Leningrad | `language_code` |
| 180463 | Leadership and Self-Deception: Getting Out of the Box | `language_code` |
| 181077 | Sadako and the Thousand Paper Cranes | `isbn` |
| 181077 | Sadako and the Thousand Paper Cranes | `isbn13` |
| 181077 | Sadako and the Thousand Paper Cranes | `language_code` |
| 181116 | Monday Mourning (Temperance Brennan, #7) | `original_title` |
| 181206 | The 80/20 Principle: The Secret to Achieving More with Less | `language_code` |
| 181601 | If You Give a Pig a Party | `language_code` |
| 183092 | Night Light (Restoration #2) | `language_code` |
| 183554 | Developing the Leader Within You | `language_code` |
| 184850 | Virgin River (Virgin River, #1) | `language_code` |
| 185012 | Doubt | `language_code` |
| 186669 | Brilliance of the Moon (Tales of the Otori, #3) | `language_code` |
| 187812 | Avalon High | `language_code` |
| 190361 | Obsidian Butterfly (Anita Blake, Vampire Hunter, #9) | `isbn` |
| 190361 | Obsidian Butterfly (Anita Blake, Vampire Hunter, #9) | `isbn13` |
| 192341 | The Starter Wife | `language_code` |
| 193093 | Stone Soup | `language_code` |
| 196970 | The Night Before Christmas | `original_title` |
| 197436 | Ralph S. Mouse by Beverly Cleary: Teacher Guide (Novel Units) | `original_publication_year` |
| 197436 | Ralph S. Mouse by Beverly Cleary: Teacher Guide (Novel Units) | `original_title` |
| 197436 | Ralph S. Mouse by Beverly Cleary: Teacher Guide (Novel Units) | `language_code` |
| 198863 | Screw It, Let's Do It: Lessons In Life | `language_code` |
| 201145 | A Kiss for Little Bear (An I Can Read Book) by Minarik, Else Holmelund [1984] | `language_code` |
| 201175 | Rapture in Death (In Death, #4) | `language_code` |
| 202146 | Flyboys: A True Story of Courage | `language_code` |
| 202948 | Ladder of Years | `language_code` |
| 203805 | Vincent Van Gogh: The Complete Paintings | `original_title` |
| 204045 | Naruto, Vol. 05: Exam Hell (Naruto, #5) | `original_title` |
| 204479 | Spying in High Heels (High Heels, #1) | `isbn` |
| 204479 | Spying in High Heels (High Heels, #1) | `isbn13` |
| 205218 | Ethics | `language_code` |
| 205330 | There Was an Old Lady Who Swallowed a Fly | `language_code` |
| 206731 | The Tibetan Book of Living and Dying | `language_code` |
| 207694 | The Nanny | `language_code` |
| 208036 | Metaphysics | `language_code` |
| 210404 | A Sand County Almanac and Sketches Here and There | `language_code` |
| 213367 | Desiring God: Meditations of a Christian Hedonist | `language_code` |
| 214332 | The Case for Faith: A Journalist Investigates the Toughest Objections to Christianity | `original_title` |
| 214333 | The Case for a Creator: A Journalist Investigates Scientific Evidence That Points Toward God | `language_code` |
| 214856 | Leven Thumps and the Gateway to Foo (Leven Thumps, #1) | `language_code` |
| 215539 | The Pilgrims of Rayne (Pendragon, #8) | `language_code` |
| 219535 | The Other | `original_title` |
| 222458 | Rules | `language_code` |
| 223838 | In His Steps | `language_code` |
| 224410 | Dracula (Marvel Illustrated) | `language_code` |
| 225545 | A Color of His Own | `language_code` |
| 226315 | The Next Big Thing | `language_code` |
| 227280 | I Do -- But I Don't | `language_code` |
| 227443 | Bridget Jones's Diary (Bridget Jones, #1) | `original_title` |
| 227729 | The Coffin Dancer (Lincoln Rhyme, #2) | `original_title` |
| 227778 | Charlie Bone and the Time Twister (The Children of the Red King, #2) | `language_code` |
| 228765 | Zen of Seeing: Seeing/Drawing as Meditation | `language_code` |
| 228990 | The Illearth War (The Chronicles of Thomas Covenant the Unbeliever, #2) | `language_code` |
| 229123 | Christy | `language_code` |
| 232958 | I Love You Through and Through | `language_code` |
| 233691 | The Far Side Gallery 3 | `language_code` |
| 234724 | Shadow Puppets (Ender's Shadow, #3) | `language_code` |
| 242157 | How to Talk to a Widower | `language_code` |
| 243298 | The Shining Ones (The Tamuli, #2) | `language_code` |
| 243308 | Steel Magnolias (DPS Acting Edition) | `original_title` |
| 245700 | The Art of Amy Brown | `language_code` |
| 246468 | The Jordan Rules | `language_code` |
| 246546 | An Old-Fashioned Girl | `language_code` |
| 248470 | River Secrets (The Books of Bayern, #3) | `language_code` |
| 249042 | Darkness Visible: A Memoir of Madness | `language_code` |
| 253058 | Temple of the Winds (Sword of Truth, #4) | `language_code` |
| 255127 | The Fifth Discipline: The Art & Practice of The Learning Organization | `original_title` |
| 255127 | The Fifth Discipline: The Art & Practice of The Learning Organization | `language_code` |
| 255458 | Systematic Theology: An Introduction to Biblical Doctrine | `language_code` |
| 256598 | Curse of the Bane (The Last Apprentice / Wardstone Chronicles, #2) | `language_code` |
| 257257 | The 20th Century Art Book | `language_code` |
| 261083 | Heretic (The Grail Quest, #3) | `language_code` |
| 261161 | Dial L for Loser (The Clique, #6) | `language_code` |
| 262545 | The Whistling Season | `language_code` |
| 262731 | The Definitive Book of Body Language | `isbn` |
| 262731 | The Definitive Book of Body Language | `isbn13` |
| 264158 | The Raven | `language_code` |
| 265205 | Life Application Study Bible: NIV | `original_title` |
| 265264 | One | `language_code` |
| 265650 | Shakespeare's Romeo and Juliet | `language_code` |
| 266904 | The Penderwicks: A Summer Tale of Four Sisters, Two Rabbits, and a Very Interesting Boy (The Penderwicks #1) | `isbn` |
| 266904 | The Penderwicks: A Summer Tale of Four Sisters, Two Rabbits, and a Very Interesting Boy (The Penderwicks #1) | `isbn13` |
| 267972 | Wait Till Helen Comes | `original_title` |
| 268955 | Mummies in the Morning (Magic Tree House, #3) | `original_title` |
| 270032 | Seven Years in Tibet | `language_code` |
| 270521 | The Russia House | `language_code` |
| 272315 | Keeping You a Secret | `language_code` |
| 275247 | Little Lord Fauntleroy | `language_code` |
| 276342 | Angel Falls | `language_code` |
| 278102 | Kaleidoscope | `original_title` |
| 280958 | Sin City: Una Dura Despedida, #1 de 3 | `original_title` |
| 280958 | Sin City: Una Dura Despedida, #1 de 3 | `language_code` |
| 281433 | Tick Tock | `language_code` |
| 281512 | He Chose the Nails | `original_title` |
| 283494 | Ironside (Modern Faerie Tales, #3) | `language_code` |
| 284195 | Nantucket Nights | `language_code` |
| 285500 | The Declaration of Independence and The Constitution of the United States | `language_code` |
| 291364 | Curious George Rides a Bike | `language_code` |
| 293625 | Child of God | `language_code` |
| 294613 | Little Bear's Friend | `language_code` |
| 295132 | Care of the Soul: A Guide for Cultivating Depth and Sacredness in Everyday Life | `language_code` |
| 295961 | The Eagle Has Landed (Liam Devlin, #1) | `language_code` |
| 296298 | The Guns of Navarone | `language_code` |
| 297135 | Summer Island | `language_code` |
| 298137 | Mao's Last Dancer | `original_title` |
| 298137 | Mao's Last Dancer | `language_code` |
| 298230 | Agnes Grey | `language_code` |
| 298568 | Night of the Soul Stealer (The Last Apprentice / Wardstone Chronicles, #3) | `language_code` |
| 298663 | The Killer Inside Me | `language_code` |
| 298816 | Peace Child: An Unforgettable Story of Primitive Jungle Treachery in the 20th Century | `language_code` |
| 299384 | Sleeping Beauty: a Little Golden Book (Disney Princess) | `original_title` |
| 300044 | Knife Edge (Noughts & Crosses, #2) | `language_code` |
| 300225 | Bloodline | `language_code` |
| 300650 | On Becoming Baby Wise: Giving Your Infant the Gift of Nighttime Sleep | `language_code` |
| 303098 | Riptide | `language_code` |
| 304079 | The Essential Rumi | `language_code` |
| 306654 | Cold Sassy Tree | `language_code` |
| 313256 | Dark Challenge (Dark, #5) | `isbn` |
| 313256 | Dark Challenge (Dark, #5) | `isbn13` |
| 313256 | Dark Challenge (Dark, #5) | `language_code` |
| 313620 | If You Want to Walk on Water, You've Got to Get Out of the Boat | `language_code` |
| 315519 | Rich Man, Poor Man | `language_code` |
| 315882 | Henry's Freedom Box: A True Story from the Underground Railroad | `original_title` |
| 318525 | Red Storm Rising | `language_code` |
| 318742 | The Souls of Black Folk | `language_code` |
| 321645 | Kissed by an Angel/The Power of Love/Soulmates (Kissed by an Angel, #1-3) | `original_title` |
| 324737 | Fresh Wind, Fresh Fire: What Happens When God's Spirit Invades the Heart of His People | `language_code` |
| 324748 | The Dip: A Little Book That Teaches You When to Quit (and When to Stick) | `language_code` |
| 325128 | Kidnapped (David Balfour, #1) | `language_code` |
| 325416 | The Voyages of Doctor Dolittle (Doctor Dolittle, #2) | `language_code` |
| 325421 | The Story of Doctor Dolittle (Doctor Dolittle, #1) | `language_code` |
| 327246 | Anatomy for the Artist | `language_code` |
| 327847 | The Joy of Cooking | `language_code` |
| 331695 | Almost French: Love and a New Life in Paris | `language_code` |
| 331701 | Stone Soup | `language_code` |
| 332348 | The Year of Fog | `language_code` |
| 336161 | The Grouchy Ladybug | `language_code` |
| 337058 | Jacob Have I Loved | `isbn` |
| 337058 | Jacob Have I Loved | `isbn13` |
| 337615 | Nine Parts of Desire: The Hidden World of Islamic Women | `language_code` |
| 339026 | The Akhenaten Adventure (Children of the Lamp, #1) | `language_code` |
| 342637 | Dali: The Paintings | `language_code` |
| 342667 | A Total Waste of Makeup (Charlize Edwards, #1) | `language_code` |
| 343614 | The Law of Attraction: The Basics of the Teachings of Abraham | `language_code` |
| 345627 | Vampire Academy (Vampire Academy, #1) | `original_title` |
| 347143 | The Abstinence Teacher | `language_code` |
| 347577 | Away Laughing on a Fast Camel (Confessions of Georgia Nicolson, #5) | `language_code` |
| 347656 | Don't Waste Your Life | `language_code` |
| 348573 | The Borrowers (The Borrowers, #1) | `language_code` |
| 349254 | The Lord of the Rings: The Return of the King: Visual Companion | `original_publication_year` |
| 349254 | The Lord of the Rings: The Return of the King: Visual Companion | `original_title` |
| 351023 | The Worst Witch (Worst Witch, #1) | `original_publication_year` |
| 351023 | The Worst Witch (Worst Witch, #1) | `language_code` |
| 352383 | Antigone | `language_code` |
| 356373 | Experiencing God: Knowing and Doing the Will of God, Workbook | `isbn` |
| 356373 | Experiencing God: Knowing and Doing the Will of God, Workbook | `isbn13` |
| 356373 | Experiencing God: Knowing and Doing the Will of God, Workbook | `language_code` |
| 364826 | سینوهه | `isbn` |
| 364826 | سینوهه | `isbn13` |
| 370057 | The Truth Seeker (O'Malley #3) | `language_code` |
| 374233 | If on a Winter's Night a Traveler | `isbn` |
| 374233 | If on a Winter's Night a Traveler | `isbn13` |
| 380975 | K is for Killer (Kinsey Millhone, #11) | `language_code` |
| 380976 | P is for Peril (Kinsey Millhone, #16) | `language_code` |
| 381421 | Jesus Calling: Enjoying Peace in His Presence | `original_title` |
| 381421 | Jesus Calling: Enjoying Peace in His Presence | `language_code` |
| 381787 | Truth Will Prevail (The Work and the Glory, #3) | `language_code` |
| 386142 | Legally Blonde | `language_code` |
| 392431 | Damaged: The Heartbreaking True Story of a Forgotten Child | `language_code` |
| 393145 | The Riddle (The Books of Pellinor, #2) | `original_title` |
| 394772 | The Mixed-Up Chameleon | `language_code` |
| 394841 | Travel Team | `language_code` |
| 396266 | The Winter Rose (The Tea Rose, #2) | `language_code` |
| 397860 | The Fog | `language_code` |
| 401679 | Llama Llama Red Pajama | `language_code` |
| 402014 | On the Bright Side, I'm Now the Girlfriend of a Sex God (Confessions of Georgia Nicolson, #2) | `language_code` |
| 402017 | The Cake Mix Doctor | `language_code` |
| 404223 | The Wounded Land (The Second Chronicles of Thomas Covenant, #1) | `language_code` |
| 404562 | Henry & Ramona | `language_code` |
| 407813 | The Blue Sword (Damar, #1) | `original_title` |
| 407813 | The Blue Sword (Damar, #1) | `language_code` |
| 407999 | Competitive Strategy: Techniques for Analyzing Industries and Competitors | `language_code` |
| 411053 | Better Homes and Gardens New Cook Book   | `language_code` |
| 417780 | Why Mosquitoes Buzz in People's Ears | `language_code` |
| 419083 | Killing Pablo: The Hunt for the World's Greatest Outlaw | `language_code` |
| 420278 | The Complete Poems 1927-1979 | `original_title` |
| 425029 | Presumed Innocent | `language_code` |
| 425124 | Sacred (Kenzie & Gennaro, #3) | `language_code` |
| 426625 | Fancy Nancy | `language_code` |
| 428862 | Wreck This Journal | `language_code` |
| 429024 | The Old Curiosity Shop | `language_code` |
| 434229 | Cape Fear | `isbn` |
| 434229 | Cape Fear | `isbn13` |
| 434229 | Cape Fear | `language_code` |
| 437885 | Frosty the Snowman (Frosty the Snowman) | `language_code` |
| 438024 | Let's Pretend This Never Happened (Dear Dumb Diary #1) | `language_code` |
| 441618 | Breaking Free: Discover the Victory of Total Surrender | `language_code` |
| 450836 | Like a Fire Burning (The Work and the Glory, #2) | `language_code` |
| 452157 | The Road to the Dark Tower: Exploring Stephen King's Magnum Opus | `language_code` |
| 454236 | Miracle in the Andes | `language_code` |
| 455764 | Audrey Rose | `language_code` |
| 457457 | Fine Things | `language_code` |
| 458034 | Caressed by Ice (Psy-Changeling #3) | `original_title` |
| 460717 | The Dogs of War | `language_code` |
| 465904 | Dragonsdawn (Pern, #9) | `language_code` |
| 478894 | The Sword of Shannara Trilogy (Shannara, #1-3) | `language_code` |
| 481749 | Jesus the Christ | `language_code` |
| 487445 | The Onion Field | `language_code` |
| 491735 | The Dirty Girls Social Club (Dirty Girls, #1) | `language_code` |
| 493455 | The Uglies Trilogy (Uglies, #1-3) | `language_code` |
| 497164 | Camera Lucida: Reflections on Photography | `language_code` |
| 497199 | Factotum | `language_code` |
| 498641 | The Practice of the Presence of God | `language_code` |
| 502406 | Curious George Takes a Job | `language_code` |
| 508413 | The Shunning (The Heritage of Lancaster County, #1) | `language_code` |
| 512475 | The Cradle Will Fall | `language_code` |
| 514313 | Bringing Down the House: The Inside Story of Six M.I.T. Students Who Took Vegas for Millions | `language_code` |
| 519933 | The Lives of Christopher Chant (Chrestomanci, #2) | `language_code` |
| 520738 | On Ugliness | `language_code` |
| 527862 | The Acid House | `language_code` |
| 529626 | Sometimes a Great Notion | `language_code` |
| 530793 | The Wives of Henry VIII | `language_code` |
| 531421 | Bella Tuscany | `language_code` |
| 531989 | Drown | `language_code` |
| 533675 | Pinocchio | `language_code` |
| 535494 | How Should We Then Live? The Rise and Decline of Western Thought and Culture | `language_code` |
| 536790 | Trumps of Doom (The Chronicles of Amber, #6) | `isbn` |
| 536790 | Trumps of Doom (The Chronicles of Amber, #6) | `isbn13` |
| 537070 | Gregor and the Code of Claw (Underland Chronicles, #5) | `language_code` |
| 537094 | The Overcoat | `language_code` |
| 541341 | Deep and Dark and Dangerous (A Ghost Story) | `language_code` |
| 542639 | The Shock of the New | `language_code` |
| 543086 | Tom's Midnight Garden | `language_code` |
| 543505 | The Tale of Mrs. Tiggy-Winkle | `language_code` |
| 554674 | The Story of the Trapp Family Singers | `language_code` |
| 556629 | The Holiness of God | `language_code` |
| 563887 | The Littles | `language_code` |
| 567616 | The Art Book | `original_title` |
| 576570 | The Princess and the Pea | `language_code` |
| 577542 | Rikki-Tikki-Tavi | `language_code` |
| 579143 | Scuffy the Tugboat (Big Little Golden Book) | `language_code` |
| 581125 | The Minority Report | `language_code` |
| 581552 | In the Penal Colony | `isbn` |
| 581552 | In the Penal Colony | `isbn13` |
| 590552 | Chicken Soup with Rice: A Book of Months (The Nutshell Library) | `language_code` |
| 594361 | The Lion King: A little Golden Book | `language_code` |
| 595822 | The Protector (O'Malley #4) | `original_title` |
| 596259 | Standing for Something: 10 Neglected Virtues That Will Heal Our Hearts and Homes | `language_code` |
| 606818 | Holy Blood, Holy Grail | `isbn` |
| 606818 | Holy Blood, Holy Grail | `isbn13` |
| 616318 | Justice, Volume 1 | `original_title` |
| 616678 | The Diamond Throne (The Elenium, #1) | `language_code` |
| 621739 | Millions of Cats | `language_code` |
| 625554 | Pillar of Light (The Work and the Glory, #1) | `language_code` |
| 633270 | The Ear, the Eye, and the Arm | `language_code` |
| 643301 | Angels and Demons / The Da Vinci Code (Robert Langdon, #1-2) | `original_title` |
| 643301 | Angels and Demons / The Da Vinci Code (Robert Langdon, #1-2) | `language_code` |
| 643962 | L is for Lawless (Kinsey Millhone, #12) | `language_code` |
| 646056 | The Little Mermaid | `language_code` |
| 646462 | The Qur'an / القرآن الكريم | `isbn` |
| 646462 | The Qur'an / القرآن الكريم | `isbn13` |
| 651260 | Domes of Fire (The Tamuli, #1) | `language_code` |
| 653559 | Sherlock Holmes and the Case of the Hound of the Baskervilles (Illustrated Classic Editions) | `original_title` |
| 668710 | Magic and Other Misdemeanors (The Sisters Grimm, #5) | `language_code` |
| 672493 | The Pursuit of God | `language_code` |
| 672948 | Arch of Triumph: A Novel of a Man Without a Country | `language_code` |
| 673252 | Anne McCaffrey's Dragonflight #1 | `original_title` |
| 682745 | The Basketball Diaries | `isbn` |
| 682745 | The Basketball Diaries | `isbn13` |
| 685401 | Permission Marketing: Turning Strangers Into Friends And Friends Into Customers | `original_title` |
| 685401 | Permission Marketing: Turning Strangers Into Friends And Friends Into Customers | `language_code` |
| 687278 | When Things Fall Apart: Heart Advice for Difficult Times | `language_code` |
| 688663 | The Art of Simple Food: Notes, Lessons, and Recipes from a Delicious Revolution | `language_code` |
| 691520 | No One Here Gets Out Alive | `language_code` |
| 693172 | Twilight Eyes | `language_code` |
| 712807 | Ruby Holler | `language_code` |
| 714380 | The Discoverers: A History of Man's Search to Know His World and Himself | `language_code` |
| 714711 | You Can Win: A Step by Step Tool for Top Achievers | `language_code` |
| 716696 | رباعيات خيام | `isbn` |
| 716696 | رباعيات خيام | `isbn13` |
| 720298 | Codependent No More: How to Stop Controlling Others and Start Caring for Yourself | `language_code` |
| 734542 | Freight Train | `language_code` |
| 744615 | Scott Pilgrim, Volume 4: Scott Pilgrim Gets It Together | `language_code` |
| 747061 | Book of Mormon, Doctrine and Covenants, Pearl of Great Price | `language_code` |
| 758153 | Born Free: A Lioness of Two Worlds (Story of Elsa, #1) | `language_code` |
| 759960 | Rumble Fish | `language_code` |
| 760025 | Positioning: The Battle for Your Mind: How to Be Seen and Heard in the Overcrowded Marketplace | `language_code` |
| 760168 | Just Me in the Tub (Mercer Mayer's Little Critter) | `language_code` |
| 760205 | There's a Nightmare in My Closet | `language_code` |
| 762288 | Nothing's Fair in Fifth Grade | `language_code` |
| 763047 | Straight Talking | `language_code` |
| 765148 | Giraffes Can't Dance | `original_publication_year` |
| 765148 | Giraffes Can't Dance | `original_title` |
| 766020 | The Rainbow Fish | `original_title` |
| 769212 | The Last Seven Months of Anne Frank | `language_code` |
| 769658 | Battlefield Earth: A Saga of the Year 3000 | `isbn` |
| 769658 | Battlefield Earth: A Saga of the Year 3000 | `isbn13` |
| 770038 | Is Your Mama a Llama? | `language_code` |
| 772852 | The Cross and the Switchblade | `language_code` |
| 772976 | Frida Kahlo: 1907-1954 Pain and Passion | `language_code` |
| 773276 | Good Night, Gorilla | `language_code` |
| 773951 | The Story of Ferdinand | `language_code` |
| 774060 | Prisoner of My Desire | `language_code` |
| 781498 | The Day Jimmy's Boa Ate the Wash | `language_code` |
| 784911 | Rise of the Evening Star (Fablehaven, #2) | `language_code` |
| 785092 | Secrets of the Millionaire Mind: Mastering the Inner Game of Wealth | `language_code` |
| 805023 | My Sweet Audrina (Audrina, #1) | `language_code` |
| 808853 | The Complete Adventures of Curious George | `language_code` |
| 809849 | Dear Zoo: A Lift-the-Flap Book | `original_publication_year` |
| 809849 | Dear Zoo: A Lift-the-Flap Book | `original_title` |
| 809849 | Dear Zoo: A Lift-the-Flap Book | `language_code` |
| 815234 | The Napping House | `language_code` |
| 821056 | Hinds' Feet on High Places | `language_code` |
| 824763 | Reborn! Vol. 01: Reborn Arrives! (Reborn!, #1) | `language_code` |
| 825081 | Lilly's Purple Plastic Purse | `language_code` |
| 825473 | The Devil's Alternative | `language_code` |
| 826583 | If You Take a Mouse to the Movies | `language_code` |
| 826584 | If You Give a Moose a Muffin | `original_title` |
| 827497 | One Flew Over the Cuckoo's Nest | `language_code` |
| 831470 | Bambi | `original_title` |
| 831829 | 30 Days of Night, Vol. 1 | `language_code` |
| 833253 | The Power of a Praying Wife | `language_code` |
| 835155 | See Jane Date | `language_code` |
| 836984 | Distant Shores | `language_code` |
| 838917 | The Power of a Praying Woman | `language_code` |
| 839263 | David Goes To School | `original_title` |
| 845977 | A Return to Love: Reflections on the Principles of "A Course in Miracles" | `language_code` |
| 846066 | The Berenstain Bears Forget Their Manners | `original_title` |
| 846984 | Love, Stargirl (Stargirl, #2) | `language_code` |
| 849380 | The Seven Principles for Making Marriage Work: A Practical Guide from the Country's Foremost Relationship Expert | `language_code` |
| 851393 | The Imitation of Christ | `language_code` |
| 851678 | What Remains: A Memoir of Fate, Friendship, and Love | `language_code` |
| 852460 | Fix-It and Forget-It Cookbook: Feasting with Your Slow Cooker | `language_code` |
| 856917 | Absolute Boyfriend, Vol. 1 | `original_publication_year` |
| 857418 | The Carrot Seed | `language_code` |
| 857448 | Harry the Dirty Dog | `original_title` |
| 857501 | Hand, Hand, Fingers, Thumb | `language_code` |
| 858514 | Wemberly Worried | `language_code` |
| 858719 | Clifford the Big Red Dog | `language_code` |
| 866222 | Winning | `language_code` |
| 867247 | A Book of Five Rings: The Classic Guide to Strategy | `language_code` |
| 867650 | The Little Red Hen (Little Golden Book) | `language_code` |
| 886512 | Jamberry | `language_code` |
| 887201 | Faeries | `isbn` |
| 887201 | Faeries | `isbn13` |
| 887201 | Faeries | `language_code` |
| 892295 | The Annotated Sherlock Holmes: The Four Novels and the Fifty-Six Short Stories Complete (2 Volume Set) | `language_code` |
| 894072 | The Little Red Caboose (Little Golden Book) | `language_code` |
| 895886 | Lassie Come-Home | `language_code` |
| 896622 | The Wolf and the Dove | `language_code` |
| 896623 | The Flame and the Flower | `language_code` |
| 900070 | The Berenstain Bears Go to School | `original_title` |
| 900892 | A Random Walk Down Wall Street | `original_title` |
| 901680 | Edvard Munch: 1863-1944 (Basic Art) | `language_code` |
| 905092 | The Millionaire Mind | `original_title` |
| 905092 | The Millionaire Mind | `language_code` |
| 905382 | Anne Frank : The Biography | `language_code` |
| 906560 | Tramp for the Lord | `language_code` |
| 918789 | West Side Story | `language_code` |
| 925367 | The Climb: Tragic Ambitions on Everest | `language_code` |
| 949709 | There Was An Old Lady Who Swallowed A Fly (Classic Books) | `language_code` |
| 953260 | Disney after Dark (Kingdom Keepers, #1) | `language_code` |
| 961833 | Mariana | `language_code` |
| 968403 | The Descendants | `language_code` |
| 988170 | Tawny Scrawny Lion | `language_code` |
| 989313 | Heart of Darkness and Selected Short Fiction | `original_title` |
| 1001896 | The Real Mother Goose | `language_code` |
| 1009996 | Artisan Bread in Five Minutes a Day: The Discovery That Revolutionizes Home Baking | `original_title` |
| 1034605 | The Country Mouse and the City Mouse; The Fox and the Crow; The Dog and His Bone | `language_code` |
| 1044141 | The 8th Habit: From Effectiveness to Greatness | `original_publication_year` |
| 1044141 | The 8th Habit: From Effectiveness to Greatness | `original_title` |
| 1045757 | Once (Once, #1) | `language_code` |
| 1055617 | The Miracle of Forgiveness | `language_code` |
| 1056627 | Become a Better You: 7 Keys to Improving Your Life Every Day | `original_publication_year` |
| 1056627 | Become a Better You: 7 Keys to Improving Your Life Every Day | `original_title` |
| 1056627 | Become a Better You: 7 Keys to Improving Your Life Every Day | `language_code` |
| 1059680 | Veganomicon: The Ultimate Vegan Cookbook | `language_code` |
| 1099097 | The Tiger Who Came to Tea | `language_code` |
| 1107001 | The Silver Palate Cookbook | `language_code` |
| 1111600 | The Wheel of Time: Boxed Set  (Wheel of Time, #1-8) | `language_code` |
| 1113545 | The Candy Shop War (The Candy Shop War, #1) | `language_code` |
| 1129315 | The Berenstain Bears' Trouble at School | `original_title` |
| 1149440 | Heavier Than Heaven: A Biography of Kurt Cobain | `language_code` |
| 1207980 | Helmet for My Pillow | `language_code` |
| 1219103 | Five Weeks in a Balloon (Extraordinary Voyages, #1) | `language_code` |
| 1231511 | Dark River (Warriors: Power of Three, #2) | `original_title` |
| 1231511 | Dark River (Warriors: Power of Three, #2) | `language_code` |
| 1268348 | The Secret Between Us | `language_code` |
| 1268479 | Warbreaker (Warbreaker, #1) | `isbn` |
| 1268479 | Warbreaker (Warbreaker, #1) | `isbn13` |
| 1275105 | A Charlie Brown Christmas | `language_code` |
| 1298171 | Finding Nemo | `language_code` |
| 1298205 | Dumbo: A Little Golden Book | `language_code` |
| 1317181 | Harry Potter and the Order of the Phoenix (Harry Potter, #5, Part 1) | `original_title` |
| 1317181 | Harry Potter and the Order of the Phoenix (Harry Potter, #5, Part 1) | `language_code` |
| 1347837 | Rule of Two (Star Wars: Darth Bane, #2) | `original_title` |
| 1350249 | The Lion King (Disney's Wonderful World of Reading) | `original_title` |
| 1372055 | Courageous (The Lost Fleet, #3) | `language_code` |
| 1375896 | Queste (Septimus Heap, #4) | `language_code` |
| 1422926 | Frosty the Snow Man | `language_code` |
| 1464757 | Edensor (Tetralogi Laskar Pelangi, #3) | `isbn` |
| 1464757 | Edensor (Tetralogi Laskar Pelangi, #3) | `isbn13` |
| 1491906 | Gang Leader for a Day: A Rogue Sociologist Takes to the Streets | `language_code` |
| 1499952 | Daddy-Long-Legs (Daddy-Long-Legs, #1) | `isbn` |
| 1499952 | Daddy-Long-Legs (Daddy-Long-Legs, #1) | `isbn13` |
| 1503274 | Rhett Butler's People | `language_code` |
| 1603923 | Beauty and the Beast | `language_code` |
| 1617875 | My Best Friend's Girl | `language_code` |
| 1629007 | Where Are You Now? | `original_title` |
| 1662160 | Your Inner Fish: A Journey into the 3.5-Billion-Year History of the Human Body | `language_code` |
| 1672727 | Two-Way Street | `language_code` |
| 1722717 | The Declaration (The Declaration, #1) | `language_code` |
| 1756703 | Blue-Eyed Devil (Travises, #2) | `original_title` |
| 1767779 | Five Little Monkeys Jumping on the Bed | `language_code` |
| 1772910 | White Nights | `isbn` |
| 1772910 | White Nights | `isbn13` |
| 1776251 | Jamie at Home: Cook Your Way to the Good Life | `language_code` |
| 1779929 | The Middle Place | `language_code` |
| 1830755 | Mine to Possess (Psy-Changeling #4) | `original_title` |
| 1833852 | A Fraction of the Whole | `language_code` |
| 1838166 | The Penderwicks on Gardam Street (The Penderwicks, #2) | `language_code` |
| 1848444 | A Scandal in Bohemia (The Adventures of Sherlock Holmes, #1) | `language_code` |
| 1876770 | Chrzest ognia (Saga o Wiedźminie, #5) | `isbn` |
| 1876770 | Chrzest ognia (Saga o Wiedźminie, #5) | `isbn13` |
| 1881621 | Shugo Chara!, Vol. 1: Who Do You Want to Be? (Shugo Chara!, #1) | `language_code` |
| 1908456 | Presentation Zen: Simple Ideas on Presentation Design and Delivery | `language_code` |
| 1923820 | Holy Bible: King James Version | `isbn` |
| 1923820 | Holy Bible: King James Version | `isbn13` |
| 1923820 | Holy Bible: King James Version | `original_title` |
| 1963638 | The Untethered Soul: The Journey Beyond Yourself | `language_code` |
| 2017056 | Skeletons at the Feast | `language_code` |
| 2122216 | Special A, Vol. 1 (Special A, #1) | `isbn` |
| 2122216 | Special A, Vol. 1 (Special A, #1) | `isbn13` |
| 2141830 | Secrets of a Shoe Addict (Shoe Addict, #2) | `language_code` |
| 2176735 | Breath | `language_code` |
| 2223324 | Harry Potter and the Chamber of Secrets: Sheet Music for Flute with C.D | `language_code` |
| 2251306 | Brain Rules: 12 Principles for Surviving and Thriving at Work, Home, and School | `language_code` |
| 2285777 | A Summer Affair | `language_code` |
| 2296567 | Say You're One of Them | `language_code` |
| 2350129 | Preach My Gospel: A Guide To Missionary Service | `language_code` |
| 2501453 | عابر سرير | `isbn` |
| 2501453 | عابر سرير | `isbn13` |
| 2501455 | فوضى الحواس | `isbn` |
| 2501455 | فوضى الحواس | `isbn13` |
| 2501458 | ذاكرة الجسد | `isbn` |
| 2501458 | ذاكرة الجسد | `isbn13` |
| 2505836 | Money, and the Law of Attraction: Learning to Attract Wealth, Health, and Happiness | `language_code` |
| 2508854 | تاكسي: حواديت المشاوير | `isbn` |
| 2508854 | تاكسي: حواديت المشاوير | `isbn13` |
| 2548866 | James Potter and the Hall of Elders' Crossing (James Potter, #1) | `isbn` |
| 2548866 | James Potter and the Hall of Elders' Crossing (James Potter, #1) | `isbn13` |
| 2659997 | Stolen Innocence: My Story of Growing Up in a Polygamous Sect, Becoming a Teenage Bride, and Breaking Free of Warren Jeffs | `language_code` |
| 2678349 | استمتع بحياتك | `isbn` |
| 2678349 | استمتع بحياتك | `isbn13` |
| 2747288 | Dragonheart (Pern, #21) | `language_code` |
| 2750180 | لا تحزن | `isbn` |
| 2750180 | لا تحزن | `isbn13` |
| 2804776 | One Fifth Avenue | `isbn` |
| 2804776 | One Fifth Avenue | `isbn13` |
| 2804776 | One Fifth Avenue | `language_code` |
| 2854962 | Charlie Bone and the Shadow (The Children of the Red King, #7) | `language_code` |
| 2865944 | If You Give a Cat a Cupcake | `language_code` |
| 2983489 | Why We Suck: A Feel Good Guide to Staying Fat, Loud, Lazy and Stupid | `language_code` |
| 3090465 | The Twilight Saga (Twilight, #1-4) | `language_code` |
| 3099780 | The Initiation / The Captive Part I (The Secret Circle, #1-2) | `original_title` |
| 3157876 | Do-It-Yourself Book (Diary of a Wimpy Kid) | `original_title` |
| 3181953 | The Heretic's Daughter | `language_code` |
| 3240691 | واحة الغروب | `isbn` |
| 3240691 | واحة الغروب | `isbn13` |
| 3243517 | رأيت رام الله | `isbn` |
| 3243517 | رأيت رام الله | `isbn13` |
| 3253215 | An Illustrated Life: Drawing Inspiration From The Private Sketchbooks Of Artists, Illustrators And Designers | `language_code` |
| 3301759 | The Murders in the Rue Morgue | `isbn` |
| 3301759 | The Murders in the Rue Morgue | `isbn13` |
| 3320520 | The 3 Mistakes of My Life | `isbn` |
| 3320520 | The 3 Mistakes of My Life | `isbn13` |
| 3331756 | عائد إلى حيفا | `isbn` |
| 3331756 | عائد إلى حيفا | `isbn13` |
| 3338544 | رحلتي من الشك إلى الإيمان | `isbn` |
| 3338544 | رحلتي من الشك إلى الإيمان | `isbn13` |
| 3474186 | Forever Princess (The Princess Diaries, #10) | `language_code` |
| 3491072 | حول العالم في 200 يوم | `isbn` |
| 3491072 | حول العالم في 200 يوم | `isbn13` |
| 3554772 | عزازيل | `isbn` |
| 3554772 | عزازيل | `isbn13` |
| 3609760 | Twilight: The Complete Illustrated Movie Companion | `original_publication_year` |
| 3692091 | 1/4 جرام | `isbn` |
| 3692091 | 1/4 جرام | `isbn13` |
| 3698601 | Food Matters: A Guide to Conscious Eating with More Than 75 Recipes | `language_code` |
| 3754026 | Beyond the Shadows (Night Angel, #3) | `original_title` |
| 3819326 | Angels' Blood (Guild Hunter, #1) | `original_title` |
| 3831279 | ڤيرتيجو | `isbn` |
| 3831279 | ڤيرتيجو | `isbn13` |
| 3975186 | True Colors | `language_code` |
| 3992598 | The Demigod Files (Percy Jackson and the Olympians) | `original_title` |
| 4005310 | Why Evolution Is True | `language_code` |
| 4110198 | The 8th Confession (Women's Murder Club, #8) | `language_code` |
| 4212386 | Maryamah Karpov: Mimpi-mimpi Lintang (Tetralogi Laskar Pelangi, #4) | `isbn` |
| 4212386 | Maryamah Karpov: Mimpi-mimpi Lintang (Tetralogi Laskar Pelangi, #4) | `isbn13` |
| 4499669 | The Love Dare | `original_title` |
| 4502877 | Midnight Sun (Twilight, #1.5) | `isbn` |
| 4502877 | Midnight Sun (Twilight, #1.5) | `isbn13` |
| 4527502 | The Scarecrow (Jack McEvoy, #2) | `isbn` |
| 4527502 | The Scarecrow (Jack McEvoy, #2) | `isbn13` |
| 4566934 | Winter in Tokyo | `isbn` |
| 4566934 | Winter in Tokyo | `isbn13` |
| 4618728 | Honolulu | `language_code` |
| 4634266 | NARUTO -ナルト- 巻ノ四十三 | `isbn` |
| 4634266 | NARUTO -ナルト- 巻ノ四十三 | `isbn13` |
| 4653511 | رجال في الشمس | `isbn` |
| 4653511 | رجال في الشمس | `isbn13` |
| 4837112 | Percy Jackson and the Sword of Hades (Percy Jackson and the Olympians, #4.5) | `language_code` |
| 4902793 | Sookie Stackhouse 7-copy Boxed Set (Sookie Stackhouse, #1-7) | `language_code` |
| 5031805 | ESV Study Bible | `original_title` |
| 5048174 | 2BR02B | `isbn` |
| 5048174 | 2BR02B | `isbn13` |
| 5061675 | A Game of Thrones / A Clash of Kings (A Song of Ice and Fire, #1-2) | `isbn` |
| 5061675 | A Game of Thrones / A Clash of Kings (A Song of Ice and Fire, #1-2) | `isbn13` |
| 5061675 | A Game of Thrones / A Clash of Kings (A Song of Ice and Fire, #1-2) | `language_code` |
| 5103512 | Martha Stewart's Cupcakes: 175 Inspired Ideas for Everyone's Favorite Treat | `language_code` |
| 5153799 | Father Mine (Black Dagger Brotherhood, #6.5) | `isbn` |
| 5153799 | Father Mine (Black Dagger Brotherhood, #6.5) | `isbn13` |
| 5153799 | Father Mine (Black Dagger Brotherhood, #6.5) | `original_title` |
| 5171894 | The Doomsday Key (Sigma Force, #6) | `original_publication_year` |
| 5171894 | The Doomsday Key (Sigma Force, #6) | `original_title` |
| 5206937 | A Modest Proposal | `language_code` |
| 5292173 | Relentless (The Lost Fleet, #5) | `language_code` |
| 5295735 | الحرافيش | `isbn` |
| 5295735 | الحرافيش | `isbn13` |
| 5557442 | ظل الأفعى | `isbn` |
| 5557442 | ظل الأفعى | `isbn13` |
| 5607622 | قمر على سمرقند | `isbn` |
| 5607622 | قمر على سمرقند | `isbn13` |
| 5628753 | Branded by Fire (Psy-Changeling #6) | `original_title` |
| 5664022 | حوار مع صديقي الملحد | `isbn` |
| 5664022 | حوار مع صديقي الملحد | `isbn13` |
| 5664022 | حوار مع صديقي الملحد | `original_title` |
| 5771014 | The Talent Code: Unlocking the Secret of Skill in Sports, Art, Music, Math, and Just About Everything Else | `language_code` |
| 5883777 | The Holy Bible: English Standard Version | `isbn` |
| 5883777 | The Holy Bible: English Standard Version | `isbn13` |
| 6023056 | Act Like a Lady, Think Like a Man: What Men Really Think About Love, Relationships, Intimacy, and Commitment | `language_code` |
| 6054190 | Dune Road | `original_publication_year` |
| 6054190 | Dune Road | `original_title` |
| 6080822 | The Castaways | `language_code` |
| 6131786 | The Virgin Cure | `language_code` |
| 6145711 | The Walking Dead, Vol. 10: What We Become | `isbn` |
| 6145711 | The Walking Dead, Vol. 10: What We Become | `isbn13` |
| 6164358 | The Mysterious Benedict Society and the Prisoner's Dilemma (The Mysterious Benedict Society, #3) | `language_code` |
| 6167746 | Marked / Betrayed / Chosen / Untamed (House of Night, #1-4) | `original_title` |
| 6251012 | UR | `isbn` |
| 6251012 | UR | `isbn13` |
| 6324090 | Alice's Adventures in Wonderland | `isbn` |
| 6324090 | Alice's Adventures in Wonderland | `isbn13` |
| 6324090 | Alice's Adventures in Wonderland | `original_title` |
| 6332526 | Inside of a Dog: What Dogs See, Smell, and Know | `original_title` |
| 6339989 | Vampire Academy Collection (Vampire Academy, #1-3) | `language_code` |
| 6344097 | The Stand: Captain Trips | `original_title` |
| 6344534 | The Second Ship (The Rho Agenda, #1) | `language_code` |
| 6351910 | Dynasty of Evil (Star Wars: Darth Bane, #3) | `original_title` |
| 6357022 | Club Shadowlands (Masters of the Shadowlands, #1) | `isbn` |
| 6357022 | Club Shadowlands (Masters of the Shadowlands, #1) | `isbn13` |
| 6361871 | The Pioneer Woman Cooks: Recipes from an Accidental Country Girl | `language_code` |
| 6387565 | Witch & Wizard (Witch & Wizard, #1) | `isbn` |
| 6387565 | Witch & Wizard (Witch & Wizard, #1) | `isbn13` |
| 6388558 | The Warlord Wants Forever (Immortals After Dark #1) | `isbn` |
| 6388558 | The Warlord Wants Forever (Immortals After Dark #1) | `isbn13` |
| 6393047 | The Viper's Nest (39 Clues, #7) | `original_title` |
| 6393082 | Ender's Game, Volume 1: Battle School (Ender's Saga) | `original_title` |
| 6395833 | Guts | `isbn` |
| 6395833 | Guts | `isbn13` |
| 6421588 | Hourglass (Evernight, #3) | `original_title` |
| 6443349 | Percy Jackson and the Olympians Boxed Set (Percy Jackson and the Olympians, #1-5) | `language_code` |
| 6452796 | Drive: The Surprising Truth About What Motivates Us | `language_code` |
| 6486483 | Emotional Intelligence 2.0 | `language_code` |
| 6488483 | The Walking Dead, Vol. 11: Fear the Hunters | `language_code` |
| 6506085 | Food Inc.: A Participant Guide: How Industrial Food is Making Us Sicker, Fatter, and Poorer-And What You Can Do About It | `isbn` |
| 6506085 | Food Inc.: A Participant Guide: How Industrial Food is Making Us Sicker, Fatter, and Poorer-And What You Can Do About It | `isbn13` |
| 6512154 | Zeitoun | `language_code` |
| 6515834 | Forgotten God: Reversing Our Tragic Neglect of the Holy Spirit | `language_code` |
| 6532496 | Not My Daughter | `language_code` |
| 6582637 | Archangel's Kiss (Guild Hunter, #2) | `original_title` |
| 6600807 | Jealousy (Strange Angels, #3) | `language_code` |
| 6604887 | أنت لي | `isbn` |
| 6604887 | أنت لي | `isbn13` |
| 6609490 | Night World: The Ultimate Fan Guide | `language_code` |
| 6609549 | By the Time You Read This, I'll Be Dead | `language_code` |
| 6614886 | زغازيغ | `isbn` |
| 6614886 | زغازيغ | `isbn13` |
| 6614886 | زغازيغ | `original_publication_year` |
| 6614886 | زغازيغ | `original_title` |
| 6621143 | Something Like Fate | `language_code` |
| 6621287 | com نسيان | `isbn` |
| 6621287 | com نسيان | `isbn13` |
| 6630751 | First to Kill (Nathan McBride, #1) | `isbn` |
| 6630751 | First to Kill (Nathan McBride, #1) | `isbn13` |
| 6667514 | The Checklist Manifesto: How to Get Things Right | `language_code` |
| 6681333 | Eleventh Grade Burns (The Chronicles of Vladimir Tod, #4) | `language_code` |
| 6681454 | Caught | `language_code` |
| 6686671 | Electric Daisy, Vol. 1 (Dengeki Daisy, #1) | `isbn` |
| 6686671 | Electric Daisy, Vol. 1 (Dengeki Daisy, #1) | `isbn13` |
| 6688121 | Negeri 5 Menara (Negeri 5 Menara, #1) | `isbn` |
| 6688121 | Negeri 5 Menara (Negeri 5 Menara, #1) | `isbn13` |
| 6692041 | Mornings in Jenin | `language_code` |
| 6694937 | Game Change: Obama and the Clintons, McCain and Palin, and the Race of a Lifetime | `language_code` |
| 6696465 | Finally (Willow Falls, #2) | `language_code` |
| 6713071 | Last Words | `original_title` |
| 6758423 | Women, Food and God: An Unexpected Path to Almost Everything | `original_title` |
| 6765740 | Perahu Kertas | `isbn` |
| 6765740 | Perahu Kertas | `isbn13` |
| 6801614 | One Piece, Volume 38: Rocketman!! (One Piece, #38) | `language_code` |
| 6828896 | Delivering Happiness: A Path to Profits, Passion, and Purpose | `language_code` |
| 6855294 | Tell-All | `language_code` |
| 6871646 | Pete the Cat: I Love My White Shoes | `original_title` |
| 6871737 | Turtle in Paradise | `original_title` |
| 6878614 | Storm Prey (Lucas Davenport, #20) | `language_code` |
| 6891433 | Panserhjerte (Harry Hole, #8) | `isbn` |
| 6891433 | Panserhjerte (Harry Hole, #8) | `isbn13` |
| 6907672 | The Talisman (Volume 1): The Road of Trials | `original_title` |
| 6931246 | Kraken | `language_code` |
| 6988014 | Seven Days in the Art World | `language_code` |
| 7010683 | Beachcombers | `original_title` |
| 7025086 | Ender's Game, Volume 2: Command School | `original_title` |
| 7090290 | My Fair Lazy: One Reality Television Addict's Attempt to Discover If Not Being A Dumb Ass Is the New Black, or, a Culture-Up Manifesto | `original_title` |
| 7108725 | Start with Why: How Great Leaders Inspire Everyone to Take Action | `language_code` |
| 7119070 | أحببتك أكثر مما ينبغي | `isbn` |
| 7119070 | أحببتك أكثر مما ينبغي | `isbn13` |
| 7135858 | My Name Is Memory | `original_title` |
| 7147831 | Min kamp 1 (Min kamp #1) | `isbn` |
| 7147831 | Min kamp 1 (Min kamp #1) | `isbn13` |
| 7182899 | Into the Gauntlet (The 39 Clues, #10) | `original_title` |
| 7202825 | Unleashed (Ross Siblings, #1) | `original_title` |
| 7262166 | Tough Customer (Mitchell & Associates #2) | `original_title` |
| 7263429 | Wolfsbane (Nightshade #2; Nightshade World #5) | `original_title` |
| 7278837 | Diary of a Wimpy Kid: #1-4 | `original_title` |
| 7290826 | Promises to Keep | `original_title` |
| 7307503 | Archangel's Consort (Guild Hunter, #3) | `original_title` |
| 7352220 | Black Butler, Vol. 3 (Black Butler, #3) | `isbn` |
| 7352220 | Black Butler, Vol. 3 (Black Butler, #3) | `isbn13` |
| 7468160 | Every Last One | `original_title` |
| 7469133 | Dexter Is Delicious (Dexter, #5) | `language_code` |
| 7494887 | The Pacific | `original_title` |
| 7497897 | Radical: Taking Back Your Faith from the American Dream | `original_title` |
| 7505716 | Alice's Adventures in Wonderland & Other Stories | `original_title` |
| 7521400 | This Time Together: Laughter and Reflection | `original_title` |
| 7557548 | Men at Arms: The Play | `original_title` |
| 7592279 | The Emperor of Nihon-Ja (Ranger's Apprentice, #10) | `original_title` |
| 7614747 | Venom (Elemental Assassin, #3) | `original_title` |
| 7619057 | Warm Bodies (Warm Bodies, #1) | `language_code` |
| 7646805 | The Gift (Witch & Wizard, #2) | `language_code` |
| 7648269 | Empire of the Summer Moon: Quanah Parker and the Rise and Fall of the Comanches, the Most Powerful Indian Tribe in American History | `language_code` |
| 7664334 | Amy & Roger's Epic Detour | `original_title` |
| 7683254 | Monster Hunter Vendetta (Monster Hunter International, #2) | `original_title` |
| 7696135 | Making Ideas Happen: Overcoming the Obstacles Between Vision and Reality | `original_title` |
| 7696135 | Making Ideas Happen: Overcoming the Obstacles Between Vision and Reality | `language_code` |
| 7701043 | الجزار | `isbn` |
| 7701043 | الجزار | `isbn13` |
| 7701275 | The Immortals Boxed Set (The Immortals, #1-3) | `original_title` |
| 7701275 | The Immortals Boxed Set (The Immortals, #1-3) | `language_code` |
| 7704143 | تراب الماس | `isbn` |
| 7704143 | تراب الماس | `isbn13` |
| 7726143 | Origins (The Vampire Diaries: Stefan's Diaries, #1) | `original_title` |
| 7726892 | The Island | `original_title` |
| 7726892 | The Island | `language_code` |
| 7743783 | The Unidentified Redhead (Redhead, #1) | `isbn` |
| 7743783 | The Unidentified Redhead (Redhead, #1) | `isbn13` |
| 7746259 | The Stand: Soul Survivors | `original_title` |
| 7775841 | Sleepwalk With Me and Other Painfully True Stories | `original_title` |
| 7775841 | Sleepwalk With Me and Other Painfully True Stories | `language_code` |
| 7778609 | Kill the Dead (Sandman Slim, #2) | `original_title` |
| 7783920 | Because of Mr. Terupt | `original_title` |
| 7785207 | The Mating  (Law of the Lycans, #2) | `isbn` |
| 7785207 | The Mating  (Law of the Lycans, #2) | `isbn13` |
| 7821447 | Sh*t My Dad Says | `language_code` |
| 7824768 | ليتها تقرأ | `isbn` |
| 7824768 | ليتها تقرأ | `isbn13` |
| 7831145 | Play of Passion (Psy-Changeling #9) | `original_title` |
| 7862725 | Branded (Fall of Angels, #1) | `original_title` |
| 7894870 | Bone: Tall Tales | `original_title` |
| 7897478 | The Bedwetter: Stories of Courage, Redemption, and Pee | `isbn` |
| 7897478 | The Bedwetter: Stories of Courage, Redemption, and Pee | `isbn13` |
| 7905977 | The Adventures of Ook and Gluk, Kung-Fu Cavemen from the Future | `original_title` |
| 7907803 | An Object of Beauty | `original_title` |
| 7908638 | Star Island (Skink, #6) | `language_code` |
| 7913305 | The Immortals of Meluha (Shiva Trilogy, #1) | `isbn` |
| 7913305 | The Immortals of Meluha (Shiva Trilogy, #1) | `isbn13` |
| 7933292 | Heaven is for Real: A Little Boy's Astounding Story of His Trip to Heaven and Back | `original_title` |
| 7942786 | Fair Game (Alpha & Omega, #3) | `original_title` |
| 7981206 | Dead Reckoning (Sookie Stackhouse, #11) | `isbn` |
| 7981206 | Dead Reckoning (Sookie Stackhouse, #11) | `isbn13` |
| 8008928 | Savages | `original_title` |
| 8034188 | Where Good Ideas Come From: The Natural History of Innovation | `original_title` |
| 8074967 | Archangel's Blade (Guild Hunter, #4) | `language_code` |
| 8112318 | The Candymakers (The Candymakers, #1) | `original_title` |
| 8113940 | Witches of East End (The Beauchamp Family, #1) | `isbn` |
| 8113940 | Witches of East End (The Beauchamp Family, #1) | `isbn13` |
| 8135807 | Rock Me (Ross Siblings, #2) | `isbn` |
| 8135807 | Rock Me (Ross Siblings, #2) | `isbn13` |
| 8135807 | Rock Me (Ross Siblings, #2) | `original_title` |
| 8152697 | Wishin' and Hopin' | `isbn` |
| 8152697 | Wishin' and Hopin' | `isbn13` |
| 8177526 | Fate (My Blood Approves, #2) | `isbn` |
| 8177526 | Fate (My Blood Approves, #2) | `isbn13` |
| 8229399 | Big Nate Strikes Again (Big Nate Novels, #2) | `original_title` |
| 8239301 | الطنطورية | `isbn` |
| 8239301 | الطنطورية | `isbn13` |
| 8274537 | Tales from a Not-So-Popular Party Girl (Dork Diaries, #2) | `language_code` |
| 8281069 | The Unofficial Harry Potter Cookbook: From Cauldron Cakes to Knickerbocker Glory--More Than 150 Magical Recipes for Wizards and Non-Wizards Alike (Unofficial Cookbook) | `original_title` |
| 8281069 | The Unofficial Harry Potter Cookbook: From Cauldron Cakes to Knickerbocker Glory--More Than 150 Magical Recipes for Wizards and Non-Wizards Alike (Unofficial Cookbook) | `language_code` |
| 8288246 | Red Glove (Curse Workers, #2) | `original_title` |
| 8296140 | Clara and Mr. Tiffany | `language_code` |
| 8320534 | Raymond E. Feist's Magician Master | `original_title` |
| 8320534 | Raymond E. Feist's Magician Master | `language_code` |
| 8343444 | Daun Yang Jatuh Tak Pernah Membenci Angin | `isbn` |
| 8343444 | Daun Yang Jatuh Tak Pernah Membenci Angin | `isbn13` |
| 8346300 | Harry Potter: A Pop-Up Book: Based on the Film Phenomenon | `original_title` |
| 8346300 | Harry Potter: A Pop-Up Book: Based on the Film Phenomenon | `language_code` |
| 8354134 | The Running Dream | `original_title` |
| 8407173 | Jasper Jones | `isbn` |
| 8407173 | Jasper Jones | `isbn13` |
| 8428984 | Half Way Home | `isbn` |
| 8428984 | Half Way Home | `isbn13` |
| 8428984 | Half Way Home | `original_title` |
| 8471815 | You Don't Have to Say You Love Me | `original_title` |
| 8542839 | Fire Burn and Cauldron Bubble (Jolie Wilkins, #1) | `isbn` |
| 8542839 | Fire Burn and Cauldron Bubble (Jolie Wilkins, #1) | `isbn13` |
| 8570787 | Drop Dead Healthy: One Man's Humble Quest for Bodily Perfection | `original_title` |
| 8575295 | Wisdom (My Blood Approves, #4) | `isbn` |
| 8575295 | Wisdom (My Blood Approves, #4) | `isbn13` |
| 8593026 | Hostile Witness (Witness Series, #1) | `isbn` |
| 8593026 | Hostile Witness (Witness Series, #1) | `isbn13` |
| 8635145 | Embrace (The Violet Eden Chapters, #1) | `isbn` |
| 8635145 | Embrace (The Violet Eden Chapters, #1) | `isbn13` |
| 8643220 | Vampire Academy: The Graphic Novel (Vampire Academy: The Graphic Novel, #1) | `language_code` |
| 8686068 | The Devotion of Suspect X | `language_code` |
| 8689913 | Madame Tussaud: A Novel of the French Revolution | `original_title` |
| 8702806 | Eve (Eve Duncan, #12; Eve, Quinn and Bonnie #1) | `original_title` |
| 8712343 | Kiss of Snow (Psy-Changeling #10) | `original_title` |
| 8718952 | Vampire Academy Box Set (Vampire Academy, #1-4) | `original_title` |
| 8720415 | Miles to Go (The Walk, #2) | `language_code` |
| 8724779 | Marked / Betrayed / Chosen / Untamed / Hunted (House of Night #1-5) | `original_publication_year` |
| 8724779 | Marked / Betrayed / Chosen / Untamed / Hunted (House of Night #1-5) | `original_title` |
| 8726744 | The Twilight Saga Complete Collection  (Twilight, #1-4 + 3.5) | `original_title` |
| 8765461 | Choosing to SEE | `original_title` |
| 8765461 | Choosing to SEE | `language_code` |
| 8793878 | The Keeping (Law of the Lycans, #3) | `isbn` |
| 8793878 | The Keeping (Law of the Lycans, #3) | `isbn13` |
| 8835897 | Defiance (Strange Angels, #4) | `language_code` |
| 8857310 | Unfamiliar Fishes | `language_code` |
| 8951449 | Hollowland (The Hollows, #1) | `original_title` |
| 9018370 | The Walking Dead, Vol. 13: Too Far Gone | `language_code` |
| 9086994 | Aleph | `isbn` |
| 9086994 | Aleph | `isbn13` |
| 9160695 | Battle Hymn of the Tiger Mother | `original_title` |
| 9166559 | These Things Hidden | `language_code` |
| 9219901 | Unbearable Lightness: A Story of Loss and Gain | `original_title` |
| 9219901 | Unbearable Lightness: A Story of Loss and Gain | `language_code` |
| 9279734 | Forever Mine (The Moreno Brothers, #1) | `isbn` |
| 9279734 | Forever Mine (The Moreno Brothers, #1) | `isbn13` |
| 9293020 | The Elephant Tree | `original_title` |
| 9296438 | Save Me | `language_code` |
| 9305362 | Captive Prince (Captive Prince, #1) | `isbn` |
| 9305362 | Captive Prince (Captive Prince, #1) | `isbn13` |
| 9409469 | The Gray Wolf Throne (Seven Realms, #3) | `isbn` |
| 9409469 | The Gray Wolf Throne (Seven Realms, #3) | `isbn13` |
| 9418327 | Bossypants | `isbn` |
| 9418327 | Bossypants | `isbn13` |
| 9429531 | The Dry Grass of August | `language_code` |
| 9440324 | The Midnight Palace (Niebla, #2) | `language_code` |
| 9484114 | The Happiness Advantage: The Seven Principles of Positive Psychology That Fuel Success and Performance at Work | `language_code` |
| 9489502 | Cold Vengeance (Pendergast, #11) | `language_code` |
| 9496240 | The Hangman's Daughter (The Hangman's Daughter, #1) | `isbn` |
| 9496240 | The Hangman's Daughter (The Hangman's Daughter, #1) | `isbn13` |
| 9512985 | The Personal MBA: Master the Art of Business | `original_title` |
| 9512985 | The Personal MBA: Master the Art of Business | `language_code` |
| 9528186 | Pretty Little Liars (TV Series) | `original_publication_year` |
| 9528186 | Pretty Little Liars (TV Series) | `original_title` |
| 9529502 | Big Nate on a Roll (Big Nate Novels, #3) | `language_code` |
| 9545064 | The Story of Beautiful Girl | `language_code` |
| 9581507 | Don't Breathe a Word | `original_title` |
| 9606002 | The Preacher (Patrik Hedström, #2) | `language_code` |
| 9635657 | Tales from a Not-So-Talented Pop Star (Dork Diaries, #3) | `isbn` |
| 9635657 | Tales from a Not-So-Talented Pop Star (Dork Diaries, #3) | `isbn13` |
| 9639197 | Turn of Mind | `language_code` |
| 9666241 | النبطي | `isbn` |
| 9666241 | النبطي | `isbn13` |
| 9670094 | Through My Eyes | `original_title` |
| 9722217 | رغم الفراق | `isbn` |
| 9722217 | رغم الفراق | `isbn13` |
| 9722217 | رغم الفراق | `original_title` |
| 9748274 | A Tale of Two Cities / Great Expectations | `original_publication_year` |
| 9748274 | A Tale of Two Cities / Great Expectations | `original_title` |
| 9751378 | Summer Rental | `original_title` |
| 9757266 | Sometimes It Happens | `original_title` |
| 9798177 | Middle School: The Worst Years of My Life (Midde School, #1) | `original_title` |
| 9799572 | Rock Chick Redemption (Rock Chick, #3) | `original_title` |
| 9802372 | The Name of the Star (Shades of London, #1) | `language_code` |
| 9814682 | A Song of Ice and Fire (A Song of Ice and Fire, #1-4) | `original_title` |
| 9832370 | BookRags Summary:  A Storm of Swords | `isbn` |
| 9832370 | BookRags Summary:  A Storm of Swords | `isbn13` |
| 9832370 | BookRags Summary:  A Storm of Swords | `original_publication_year` |
| 9832370 | BookRags Summary:  A Storm of Swords | `original_title` |
| 9858488 | Dead End in Norvelt | `original_title` |
| 9858714 | The Mind Readers (Mind Readers, #1) | `isbn` |
| 9858714 | The Mind Readers (Mind Readers, #1) | `isbn13` |
| 9902804 | Lies That Chelsea Handler Told Me | `original_title` |
| 9915707 | Endure (Need, #4) | `isbn` |
| 9915707 | Endure (Need, #4) | `isbn13` |
| 9917879 | The Unwanteds (Unwanteds, #1) | `original_title` |
| 9917945 | Perfect (Impulse, #2) | `original_title` |
| 9923372 | Maine | `language_code` |
| 9925913 | Shock Wave (Virgil Flowers, #5) | `isbn` |
| 9925913 | Shock Wave (Virgil Flowers, #5) | `isbn13` |
| 9969571 | Ready Player One | `original_title` |
| 10088913 | مخطوطة بن إسحاق: مدينة الموتى | `isbn` |
| 10088913 | مخطوطة بن إسحاق: مدينة الموتى | `isbn13` |
| 10111087 | Turn Right at Machu Picchu: Rediscovering the Lost City One Step at a Time | `original_title` |
| 10161216 | Mr. Churchill's Secretary (Maggie Hope Mystery, #1) | `original_title` |
| 10169662 | Never Knowing | `isbn` |
| 10169662 | Never Knowing | `isbn13` |
| 10209997 | The Night Strangers | `original_title` |
| 10211494 | Stories I Only Tell My Friends | `original_title` |
| 10295484 | Heart on a Chain | `isbn` |
| 10295484 | Heart on a Chain | `isbn13` |
| 10305231 | The Next Always (Inn BoonsBoro, #1) | `language_code` |
| 10327303 | Uncommon Criminals (Heist Society, #2) | `language_code` |
| 10335318 | Destiny of the Republic: A Tale of Madness, Medicine and the Murder of a President | `original_title` |
| 10365343 | Zone One | `original_title` |
| 10421530 | Kiss of Frost (Mythos Academy, #2) | `language_code` |
| 10468258 | The Finding (Law of the Lycans, #5) | `isbn` |
| 10468258 | The Finding (Law of the Lycans, #5) | `isbn13` |
| 10473214 | 13 Gifts (Willow Falls, #3) | `original_title` |
| 10508526 | The Chronicles of Harris Burdick: 14 Amazing Authors Tell the Tales | `original_title` |
| 10537195 | The Last Council (Amulet, #4) | `original_title` |
| 10586539 | Wake (Watersong #1) | `isbn` |
| 10586539 | Wake (Watersong #1) | `isbn13` |
| 10594929 | Out of Oz (The Wicked Years, #4) | `original_title` |
| 10599302 | Head Over Heels (Lucky Harbor, #3) | `isbn` |
| 10599302 | Head Over Heels (Lucky Harbor, #3) | `isbn13` |
| 10604115 | Happy Accidents: A Memoir | `original_title` |
| 10604115 | Happy Accidents: A Memoir | `language_code` |
| 10659536 | Every Thing on It | `language_code` |
| 10661081 | Vampire Academy: The Ultimate Guide (Vampire Academy) | `original_title` |
| 10664113 | A Dance with Dragons (A Song of Ice and Fire, #5) | `isbn` |
| 10664113 | A Dance with Dragons (A Song of Ice and Fire, #5) | `isbn13` |
| 10706934 | بيكاسو وستاربكس | `isbn` |
| 10706934 | بيكاسو وستاربكس | `isbn13` |
| 10710392 | Chopsticks | `original_title` |
| 10762697 | The Farseer Trilogy (Farseer Trilogy #1-3) | `original_title` |
| 10776793 | War Brides | `isbn` |
| 10776793 | War Brides | `isbn13` |
| 10778410 | The Fire (Witch & Wizard, #3) | `original_title` |
| 10778410 | The Fire (Witch & Wizard, #3) | `language_code` |
| 10785687 | Harry Potter Page to Screen: The Complete Filmmaking Journey | `language_code` |
| 10790276 | Courageous | `language_code` |
| 10790376 | A Modern Witch (A Modern Witch, #1) | `isbn` |
| 10790376 | A Modern Witch (A Modern Witch, #1) | `isbn13` |
| 10801027 | Cross My Heart (Cross My Heart, #1) | `isbn` |
| 10801027 | Cross My Heart (Cross My Heart, #1) | `isbn13` |
| 10813469 | Rock Chick Renegade (Rock Chick, #4) | `isbn` |
| 10813469 | Rock Chick Renegade (Rock Chick, #4) | `isbn13` |
| 10813469 | Rock Chick Renegade (Rock Chick, #4) | `original_title` |
| 10813480 | For You (The 'Burg, #1) | `isbn` |
| 10813480 | For You (The 'Burg, #1) | `isbn13` |
| 10830444 | Guilty Wives | `isbn` |
| 10830444 | Guilty Wives | `isbn13` |
| 10868182 | The Hidden Child (Patrik Hedström, #5) | `language_code` |
| 10875239 | Lethal | `language_code` |
| 10960383 | A Grown-Up Kind of Pretty | `original_title` |
| 10970532 | The Siren (The Original Sinners, #1) | `language_code` |
| 11051889 | The Fallen Star (Fallen Star, #1) | `original_title` |
| 11051889 | The Fallen Star (Fallen Star, #1) | `language_code` |
| 11076177 | The Cat's Table | `original_title` |
| 11096647 | Flat-Out Love (Flat-Out Love, #1) | `isbn` |
| 11096647 | Flat-Out Love (Flat-Out Love, #1) | `isbn13` |
| 11101772 | The Scrapbook of Frankie Pratt | `original_title` |
| 11104030 | MWF Seeking BFF: My Yearlong Search For A New Best Friend | `original_title` |
| 11104933 | Willpower: Rediscovering the Greatest Human Strength | `language_code` |
| 11198480 | Not a Fan: Becoming a Completely Committed Follower of Jesus | `original_title` |
| 11201007 | Hearts in Darkness (Hearts in Darkness, #1) | `isbn` |
| 11201007 | Hearts in Darkness (Hearts in Darkness, #1) | `isbn13` |
| 11227040 | Sweet Dreams (Colorado Mountain, #2) | `isbn` |
| 11227040 | Sweet Dreams (Colorado Mountain, #2) | `isbn13` |
| 11227041 | The Gamble (Colorado Mountain, #1) | `isbn` |
| 11227041 | The Gamble (Colorado Mountain, #1) | `isbn13` |
| 11227043 | Rock Chick Revenge (Rock Chick, #5) | `isbn` |
| 11227043 | Rock Chick Revenge (Rock Chick, #5) | `isbn13` |
| 11227043 | Rock Chick Revenge (Rock Chick, #5) | `original_title` |
| 11237412 | Six's Legacy (Lorien Legacies: The Lost Files, #1) | `isbn` |
| 11237412 | Six's Legacy (Lorien Legacies: The Lost Files, #1) | `isbn13` |
| 11239856 | Maid for the Billionaire (Legacy Collection, #1) | `isbn` |
| 11239856 | Maid for the Billionaire (Legacy Collection, #1) | `isbn13` |
| 11239856 | Maid for the Billionaire (Legacy Collection, #1) | `original_title` |
| 11260526 | The Twilight Saga Breaking Dawn Part 1: The Official Illustrated Movie Companion (The Twilight Saga: The Official Illustrated Movie Companion, #4) | `original_title` |
| 11262424 | Between the Lines (Between the Lines, #1) | `isbn` |
| 11262424 | Between the Lines (Between the Lines, #1) | `isbn13` |
| 11266880 | It Chooses You | `original_title` |
| 11281852 | Kisses from Katie: A Story of Relentless Love and Redemption | `original_title` |
| 11306337 | EntreLeadership: 20 Years of Practical Business Wisdom from the Trenches | `original_title` |
| 11306337 | EntreLeadership: 20 Years of Practical Business Wisdom from the Trenches | `language_code` |
| 11324166 | Timeless (Parasol Protectorate, #5) | `isbn` |
| 11324166 | Timeless (Parasol Protectorate, #5) | `isbn13` |
| 11337912 | The Prisoner of Cell 25 (Michael Vey, #1) | `language_code` |
| 11350430 | The Mystery Knight (The Tales of Dunk and Egg, #3) | `isbn` |
| 11350430 | The Mystery Knight (The Tales of Dunk and Egg, #3) | `isbn13` |
| 11381910 | Heft | `language_code` |
| 11382346 | That Boy (That Boy, #1) | `isbn` |
| 11382346 | That Boy (That Boy, #1) | `isbn13` |
| 11389341 | The Meaning of Marriage: Facing the Complexities of Commitment with the Wisdom of God | `original_title` |
| 11391817 | Drawing from Memory | `original_title` |
| 11395597 | Why Be Happy When You Could Be Normal? | `language_code` |
| 11401915 | The Ripper (The Vampire Diaries: Stefan's Diaries, #4) | `language_code` |
| 11408650 | The Unbecoming of Mara Dyer (Mara Dyer, #1) | `isbn` |
| 11408650 | The Unbecoming of Mara Dyer (Mara Dyer, #1) | `isbn13` |
| 11445880 | Midnight in Austenland (Austenland, #2) | `original_title` |
| 11450591 | The Mill River Recluse | `isbn` |
| 11450591 | The Mill River Recluse | `isbn13` |
| 11479285 | Breathe (Sea Breeze, #1) | `isbn` |
| 11479285 | Breathe (Sea Breeze, #1) | `isbn13` |
| 11505797 | Beautiful Disaster (Beautiful, #1) | `isbn` |
| 11505797 | Beautiful Disaster (Beautiful, #1) | `isbn13` |
| 11512688 | The Dead of Night (The 39 Clues: Cahills vs. Vespers, #3) | `original_title` |
| 11561469 | Reason to Breathe (Breathing, #1) | `isbn` |
| 11561469 | Reason to Breathe (Breathing, #1) | `isbn13` |
| 11665750 | At Peace (The 'Burg, #2) | `isbn` |
| 11665750 | At Peace (The 'Burg, #2) | `isbn13` |
| 11737313 | Three Times Lucky (Tupelo Landing, #1) | `original_title` |
| 11742691 | The Hunger Games: Official Illustrated Movie Companion | `original_title` |
| 11757975 | The Look of Love (San Francisco Sullivans, #1; The Sullivans, #1) | `isbn` |
| 11757975 | The Look of Love (San Francisco Sullivans, #1; The Sullivans, #1) | `isbn13` |
| 11784281 | Take This Regret (Take This Regret, #1) | `isbn` |
| 11784281 | Take This Regret (Take This Regret, #1) | `isbn13` |
| 11808919 | Maid for Love (Gansett Island Series, #1) | `isbn` |
| 11808919 | Maid for Love (Gansett Island Series, #1) | `isbn13` |
| 11821514 | Long Time Coming | `isbn` |
| 11821514 | Long Time Coming | `isbn13` |
| 11851522 | The Complete Works of H.P. Lovecraft | `isbn` |
| 11851522 | The Complete Works of H.P. Lovecraft | `isbn13` |
| 11851522 | The Complete Works of H.P. Lovecraft | `original_title` |
| 11873368 | The World of the Hunger Games (Hunger Games Trilogy) | `original_title` |
| 11913681 | The Boyfriend Thief (Stolen Kiss, #1) | `isbn` |
| 11913681 | The Boyfriend Thief (Stolen Kiss, #1) | `isbn13` |
| 11913681 | The Boyfriend Thief (Stolen Kiss, #1) | `original_title` |
| 11942408 | شاب كشك في رحلة البحث عن الجادون | `isbn` |
| 11942408 | شاب كشك في رحلة البحث عن الجادون | `isbn13` |
| 11947156 | Prince of Wolves (The Grey Wolves, #1) | `isbn` |
| 11947156 | Prince of Wolves (The Grey Wolves, #1) | `isbn13` |
| 11970096 | Twenty-Eight and a Half Wishes (Rose Gardner Mystery, #1) | `isbn` |
| 11970096 | Twenty-Eight and a Half Wishes (Rose Gardner Mystery, #1) | `isbn13` |
| 11970096 | Twenty-Eight and a Half Wishes (Rose Gardner Mystery, #1) | `original_title` |
| 11970747 | The Hedge Knight (The Tales of Dunk and Egg, #1) | `isbn` |
| 11970747 | The Hedge Knight (The Tales of Dunk and Egg, #1) | `isbn13` |
| 11981168 | The One You Love (Emma Holden Suspense Mystery, #1) | `isbn` |
| 11981168 | The One You Love (Emma Holden Suspense Mystery, #1) | `isbn13` |
| 11981168 | The One You Love (Emma Holden Suspense Mystery, #1) | `original_title` |
| 11985631 | The Sworn Sword (The Tales of Dunk and Egg, #2) | `isbn` |
| 11985631 | The Sworn Sword (The Tales of Dunk and Egg, #2) | `isbn13` |
| 11995136 | محال | `isbn` |
| 11995136 | محال | `isbn13` |
| 11996019 | The King's Agent | `original_title` |
| 12000020 | Aristotle and Dante Discover the Secrets of the Universe (Aristotle and Dante Discover the Secrets of the Universe, #1) | `language_code` |
| 12002819 | The Flight of Gemma Hardy | `original_title` |
| 12019355 | Infamous (Chronicles of Nick, #3) | `language_code` |
| 12037026 | Come Home | `language_code` |
| 12039943 | Capital | `language_code` |
| 12063467 | Fury (New Species, #1) | `original_title` |
| 12065943 | Extra Yarn (E. B. White Read-Aloud Award. Picture Books) | `original_title` |
| 12067972 | Where You Are (Between the Lines, #2) | `isbn` |
| 12067972 | Where You Are (Between the Lines, #2) | `isbn13` |
| 12072362 | The Pioneer Woman Cooks: Food from My Frontier  | `original_title` |
| 12107920 | Shatterproof (The 39 Clues: Cahills vs. Vespers, #4) | `original_title` |
| 12107920 | Shatterproof (The 39 Clues: Cahills vs. Vespers, #4) | `language_code` |
| 12107925 | Day of Doom (The 39 Clues: Cahills vs. Vespers, #6) | `original_title` |
| 12107927 | Trust No One (The 39 Clues: Cahills vs. Vespers, #5) | `original_title` |
| 12158480 | Why Nations Fail: The Origins of Power, Prosperity, and Poverty | `language_code` |
| 12171769 | 7: An Experimental Mutiny Against Excess | `original_title` |
| 12191246 | Second Son (Jack Reacher, #15.5) | `isbn` |
| 12191246 | Second Son (Jack Reacher, #15.5) | `isbn13` |
| 12191246 | Second Son (Jack Reacher, #15.5) | `language_code` |
| 12254379 | 1Q84 #1-2 (1Q84, #1-2) | `isbn` |
| 12254379 | 1Q84 #1-2 (1Q84, #1-2) | `isbn13` |
| 12287209 | Wool (Wool, #1) | `isbn` |
| 12287209 | Wool (Wool, #1) | `isbn13` |
| 12288282 | Gunmetal Magic (Kate Daniels, #5.5) | `isbn` |
| 12288282 | Gunmetal Magic (Kate Daniels, #5.5) | `isbn13` |
| 12299419 | Mystery Man (Dream Man, #1) | `isbn` |
| 12299419 | Mystery Man (Dream Man, #1) | `isbn13` |
| 12326627 | The White Princess (The Plantagenet and Tudor Novels, #5) | `isbn` |
| 12326627 | The White Princess (The Plantagenet and Tudor Novels, #5) | `isbn13` |
| 12331767 | High-Rise | `language_code` |
| 12341557 | The Wind Through the Keyhole (The Dark Tower, #4.5) | `isbn` |
| 12341557 | The Wind Through the Keyhole (The Dark Tower, #4.5) | `isbn13` |
| 12351649 | Perfection (Neighbor from Hell, #2) | `isbn` |
| 12351649 | Perfection (Neighbor from Hell, #2) | `isbn13` |
| 12389310 | Crow's Row (Crow's Row, #1) | `original_title` |
| 12390650 | Wildest Dreams (Fantasyland, #1) | `isbn` |
| 12390650 | Wildest Dreams (Fantasyland, #1) | `isbn13` |
| 12413836 | Avatar: The Last Airbender (The Promise, #1) | `original_title` |
| 12413836 | Avatar: The Last Airbender (The Promise, #1) | `language_code` |
| 12413949 | White Girl Problems | `original_title` |
| 12415695 | كخه يا بابا | `isbn` |
| 12415695 | كخه يا بابا | `isbn13` |
| 12458287 | The Golden Dynasty (Fantasyland, #2) | `isbn` |
| 12458287 | The Golden Dynasty (Fantasyland, #2) | `isbn13` |
| 12458287 | The Golden Dynasty (Fantasyland, #2) | `original_title` |
| 12475019 | Some Assembly Required: A Journal of My Son's First Son | `original_title` |
| 12513614 | Captive in the Dark (The Dark Duet, #1) | `isbn` |
| 12513614 | Captive in the Dark (The Dark Duet, #1) | `isbn13` |
| 12583975 | The Billionaire Wins the Game (Billionaire Bachelors, #1) | `isbn` |
| 12583975 | The Billionaire Wins the Game (Billionaire Bachelors, #1) | `isbn13` |
| 12598982 | Afterwards | `language_code` |
| 12602078 | The Tycoon's Revenge (Baby for the Billionaire, #1) | `isbn` |
| 12602078 | The Tycoon's Revenge (Baby for the Billionaire, #1) | `isbn13` |
| 12602078 | The Tycoon's Revenge (Baby for the Billionaire, #1) | `original_title` |
| 12605157 | The $100 Startup: Reinvent the Way You Make a Living, Do What You Love, and Create a New Future | `original_title` |
| 12611073 | The Harbinger: The Ancient Mystery that Holds the Secret of America's Future | `original_title` |
| 12611073 | The Harbinger: The Ancient Mystery that Holds the Secret of America's Future | `language_code` |
| 12647642 | Love Unrehearsed (Love, #2) | `isbn` |
| 12647642 | Love Unrehearsed (Love, #2) | `isbn13` |
| 12652457 | The Broken Eye (Lightbringer, #3) | `isbn` |
| 12652457 | The Broken Eye (Lightbringer, #3) | `isbn13` |
| 12667194 | Accordance (Significance, #2) | `isbn` |
| 12667194 | Accordance (Significance, #2) | `isbn13` |
| 12675109 | Great by Choice: Uncertainty, Chaos, and Luck--Why Some Thrive Despite Them All | `isbn` |
| 12675109 | Great by Choice: Uncertainty, Chaos, and Luck--Why Some Thrive Despite Them All | `isbn13` |
| 12675109 | Great by Choice: Uncertainty, Chaos, and Luck--Why Some Thrive Despite Them All | `original_title` |
| 12706435 | Defiance (Significance, #3) | `isbn` |
| 12706435 | Defiance (Significance, #3) | `isbn13` |
| 12712435 | Seating Arrangements | `language_code` |
| 12716010 | Rapture (Fallen, #4) | `isbn` |
| 12716010 | Rapture (Fallen, #4) | `isbn13` |
| 12716613 | The Witness | `language_code` |
| 12737118 | Wife 22 | `language_code` |
| 12755792 | A Hidden Fire (Elemental Mysteries, #1) | `isbn` |
| 12755792 | A Hidden Fire (Elemental Mysteries, #1) | `isbn13` |
| 12755792 | A Hidden Fire (Elemental Mysteries, #1) | `language_code` |
| 12758317 | In One Person | `language_code` |
| 12760903 | The Vision (Fallen Star, #3) | `isbn` |
| 12760903 | The Vision (Fallen Star, #3) | `isbn13` |
| 12760903 | The Vision (Fallen Star, #3) | `original_title` |
| 12799058 | Summerland | `isbn` |
| 12799058 | Summerland | `isbn13` |
| 12842134 | Just One Year (Just One Day, #2) | `isbn` |
| 12842134 | Just One Year (Just One Day, #2) | `isbn13` |
| 12867423 | Girl Walks into a Bar . . .: Comedy Calamities, Dating Disasters, and a Midlife Miracle | `original_title` |
| 12867423 | Girl Walks into a Bar . . .: Comedy Calamities, Dating Disasters, and a Midlife Miracle | `language_code` |
| 12878300 | Fearless: The Heroic Story of One Navy SEAL's Sacrifice in the Hunt for Osama Bin Laden and the Unwavering Devotion of the Woman Who Loved Him | `original_title` |
| 12878300 | Fearless: The Heroic Story of One Navy SEAL's Sacrifice in the Hunt for Osama Bin Laden and the Unwavering Devotion of the Woman Who Loved Him | `language_code` |
| 12881141 | Wild Man (Dream Man, #2) | `isbn` |
| 12881141 | Wild Man (Dream Man, #2) | `isbn13` |
| 12900174 | The Vincent Boys (The Vincent Boys, #1) | `isbn` |
| 12900174 | The Vincent Boys (The Vincent Boys, #1) | `isbn13` |
| 12902549 | An Invisible Thread: The True Story of an 11-Year-Old Panhandler, a Busy Sales Executive, and an Unlikely Meeting with Destiny | `isbn` |
| 12902549 | An Invisible Thread: The True Story of an 11-Year-Old Panhandler, a Busy Sales Executive, and an Unlikely Meeting with Destiny | `isbn13` |
| 12922320 | Criminal (Will Trent, #6) | `isbn` |
| 12922320 | Criminal (Will Trent, #6) | `isbn13` |
| 12924261 | This Book Is Full of Spiders: Seriously, Dude, Don't Touch It (John Dies at the End, #2) | `original_title` |
| 12926804 | One for the Murphys | `original_title` |
| 12958487 | Lady Luck (Colorado Mountain, #3) | `isbn` |
| 12958487 | Lady Luck (Colorado Mountain, #3) | `isbn13` |
| 12987640 | Imagine: How Creativity Works | `original_title` |
| 13027304 | The Hunger Games Tribute Guide | `original_title` |
| 13031445 | The Hunger Pains: A Parody | `original_title` |
| 13051316 | The Misremembered Man (Tailorstown #1) | `isbn` |
| 13051316 | The Misremembered Man (Tailorstown #1) | `isbn13` |
| 13057939 | In the Shadow of the Banyan | `language_code` |
| 13065142 | Rock Chick Reckoning (Rock Chick, #6) | `isbn` |
| 13065142 | Rock Chick Reckoning (Rock Chick, #6) | `isbn13` |
| 13065142 | Rock Chick Reckoning (Rock Chick, #6) | `original_title` |
| 13069213 | Yes, Chef | `original_title` |
| 13070346 | Blood Rites (The Grey Wolves, #2) | `isbn` |
| 13070346 | Blood Rites (The Grey Wolves, #2) | `isbn13` |
| 13096848 | Avatar: The Last Airbender (The Promise, #2) | `original_title` |
| 13125947 | Reached (Matched, #3) | `language_code` |
| 13129925 | Horrorstör | `language_code` |
| 13132816 | Emmy & Oliver | `isbn` |
| 13132816 | Emmy & Oliver | `isbn13` |
| 13146214 | Because of Low (Sea Breeze, #2) | `isbn` |
| 13146214 | Because of Low (Sea Breeze, #2) | `isbn13` |
| 13151283 | بضع ساعات في يوم ما | `isbn` |
| 13151283 | بضع ساعات في يوم ما | `isbn13` |
| 13151637 | طه الغريب | `isbn` |
| 13151637 | طه الغريب | `isbn13` |
| 13152194 | Tiny Beautiful Things: Advice on Love and Life from Dear Sugar | `language_code` |
| 13152998 | Home | `language_code` |
| 13153693 | Ghettoside: A True Story of Murder in America | `language_code` |
| 13154952 | Calico Joe | `language_code` |
| 13167062 | Spring Fever | `original_title` |
| 13167847 | Most Talkative: Stories from the Front Lines of Pop Culture | `original_title` |
| 13167847 | Most Talkative: Stories from the Front Lines of Pop Culture | `language_code` |
| 13178410 | Proper Gauge (Wool, #2) | `isbn` |
| 13178410 | Proper Gauge (Wool, #2) | `isbn13` |
| 13184572 | The Next Best Thing | `isbn` |
| 13184572 | The Next Best Thing | `isbn13` |
| 13184572 | The Next Best Thing | `language_code` |
| 13184992 | Rock Chick Regret (Rock Chick, #7) | `isbn` |
| 13184992 | Rock Chick Regret (Rock Chick, #7) | `isbn13` |
| 13184992 | Rock Chick Regret (Rock Chick, #7) | `original_title` |
| 13188676 | Ignite Me (Shatter Me, #3) | `isbn` |
| 13188676 | Ignite Me (Shatter Me, #3) | `isbn13` |
| 13223520 | Existence (Existence Trilogy, #1) | `isbn` |
| 13223520 | Existence (Existence Trilogy, #1) | `isbn13` |
| 13223520 | Existence (Existence Trilogy, #1) | `original_title` |
| 13226173 | The Infernal Devices: Clockwork Angel (The Infernal Devices: Manga, #1) | `original_title` |
| 13230263 | Mrs. Kennedy and Me: An Intimate Memoir | `original_title` |
| 13235689 | How Music Works | `language_code` |
| 13241659 | Ever After (The Hollows, #11) | `original_title` |
| 13256064 | Phantom (Harry Hole, #9) | `language_code` |
| 13272498 | Last to Die (Rizzoli & Isles, #10) | `language_code` |
| 13281637 | Intuition (The Premonition, #2) | `original_title` |
| 13312527 | The Opportunist (Love Me with Lies, #1) | `isbn` |
| 13312527 | The Opportunist (Love Me with Lies, #1) | `isbn13` |
| 13323842 | Predestined (Existence Trilogy, #2) | `isbn` |
| 13323842 | Predestined (Existence Trilogy, #2) | `isbn13` |
| 13330603 | The Sandcastle Girls | `language_code` |
| 13330761 | The Dog Stars | `language_code` |
| 13331184 | Heads in Beds: A Reckless Memoir of Hotels, Hustles, and So-Called Hospitality | `language_code` |
| 13331199 | The Smitten Kitchen Cookbook | `original_title` |
| 13331199 | The Smitten Kitchen Cookbook | `language_code` |
| 13345975 | Avoiding Commitment (Avoiding, #1) | `isbn` |
| 13345975 | Avoiding Commitment (Avoiding, #1) | `isbn13` |
| 13362536 | Opal (Lux, #3) | `language_code` |
| 13363270 | Just One Drop (The Grey Wolves, #3) | `isbn` |
| 13363270 | Just One Drop (The Grey Wolves, #3) | `isbn13` |
| 13369678 | The Vincent Brothers (The Vincent Boys, #2) | `isbn` |
| 13369678 | The Vincent Brothers (The Vincent Boys, #2) | `isbn13` |
| 13372690 | Slammed (Slammed, #1) | `isbn` |
| 13372690 | Slammed (Slammed, #1) | `isbn13` |
| 13402447 | UnEnchanted (An Unfortunate Fairy Tale, #1) | `isbn` |
| 13402447 | UnEnchanted (An Unfortunate Fairy Tale, #1) | `isbn13` |
| 13412515 | Law Man (Dream Man, #3) | `isbn` |
| 13412515 | Law Man (Dream Man, #3) | `isbn13` |
| 13415554 | The Assassin and the Pirate Lord (Throne of Glass, #0.1) | `isbn` |
| 13415554 | The Assassin and the Pirate Lord (Throne of Glass, #0.1) | `isbn13` |
| 13417946 | Eden (Providence, #3) | `original_title` |
| 13417946 | Eden (Providence, #3) | `language_code` |
| 13419891 | The Assassin and the Desert (Throne of Glass, #0.3) | `isbn` |
| 13419891 | The Assassin and the Desert (Throne of Glass, #0.3) | `isbn13` |
| 13425393 | I Suck at Girls | `original_title` |
| 13425393 | I Suck at Girls | `language_code` |
| 13425570 | How Will You Measure Your Life? | `language_code` |
| 13431827 | The Remaining (The Remaining, #1) | `isbn` |
| 13431827 | The Remaining (The Remaining, #1) | `isbn13` |
| 13431827 | The Remaining (The Remaining, #1) | `original_title` |
| 13448656 | Motorcycle Man (Dream Man, #4) | `isbn` |
| 13448656 | Motorcycle Man (Dream Man, #4) | `isbn13` |
| 13453029 | Wool Omnibus (Silo, #1) | `isbn` |
| 13453029 | Wool Omnibus (Silo, #1) | `isbn13` |
| 13489517 | 28 حرف | `isbn` |
| 13489517 | 28 حرف | `isbn13` |
| 13489518 | Out of the Dark (The Grey Wolves, #4) | `isbn` |
| 13489518 | Out of the Dark (The Grey Wolves, #4) | `isbn13` |
| 13496084 | Point of Retreat (Slammed, #2) | `isbn` |
| 13496084 | Point of Retreat (Slammed, #2) | `isbn13` |
| 13496738 | While It Lasts (Sea Breeze, #3) | `isbn` |
| 13496738 | While It Lasts (Sea Breeze, #3) | `isbn13` |
| 13502963 | Indebted (The Premonition, #3) | `isbn` |
| 13502963 | Indebted (The Premonition, #3) | `isbn13` |
| 13502963 | Indebted (The Premonition, #3) | `original_title` |
| 13502970 | Incendiary (The Premonition, #4) | `isbn` |
| 13502970 | Incendiary (The Premonition, #4) | `isbn13` |
| 13507011 | Low Pressure | `isbn` |
| 13507011 | Low Pressure | `isbn13` |
| 13508607 | The Secret Keeper | `language_code` |
| 13519844 | Independence (Significance, #4) | `original_title` |
| 13521299 | Alex Cross, Run (Alex Cross, #20) | `language_code` |
| 13522957 | Feral Sins (The Phoenix Pack, #1) | `isbn` |
| 13522957 | Feral Sins (The Phoenix Pack, #1) | `isbn13` |
| 13523061 | The Defining Decade: Why Your Twenties Matter--And How to Make the Most of Them Now | `language_code` |
| 13530981 | Dear Life: Stories | `language_code` |
| 13531832 | Vampires in the Lemon Grove | `original_title` |
| 13540215 | The Orchardist | `language_code` |
| 13545075 | UnWholly (Unwind, #2) | `language_code` |
| 13545345 | Tales from a Not-So-Graceful Ice Princess (Dork Diaries, #4) | `language_code` |
| 13546173 | The Assassin and the Underworld (Throne of Glass, #0.4) | `isbn` |
| 13546173 | The Assassin and the Underworld (Throne of Glass, #0.4) | `isbn13` |
| 13547234 | The Testament of Mary | `language_code` |
| 13547241 | Unorthodox: The Scandalous Rejection of My Hasidic Roots | `original_title` |
| 13560262 | Avoiding Responsibility (Avoiding, #2) | `original_title` |
| 13565676 | The Assassin and the Empire (Throne of Glass, #0.5) | `isbn` |
| 13565676 | The Assassin and the Empire (Throne of Glass, #0.5) | `isbn13` |
| 13565914 | Knight (Unfinished Hero, #1) | `isbn` |
| 13565914 | Knight (Unfinished Hero, #1) | `isbn13` |
| 13568322 | The Zombie Room | `original_title` |
| 13568619 | The Shadowhunter's Codex | `isbn` |
| 13568619 | The Shadowhunter's Codex | `isbn13` |
| 13569581 | Blood Song (Raven's Shadow, #1) | `isbn` |
| 13569581 | Blood Song (Raven's Shadow, #1) | `isbn13` |
| 13573236 | The Racketeer | `language_code` |
| 13573795 | Ceaseless (Existence Trilogy, #3) | `isbn` |
| 13573795 | Ceaseless (Existence Trilogy, #3) | `isbn13` |
| 13580846 | My Life with the Walter Boys (My Life with the Walter Boys #1) | `isbn` |
| 13580846 | My Life with the Walter Boys (My Life with the Walter Boys #1) | `isbn13` |
| 13584236 | Fifty Shades Trilogy (Fifty Shades, #1-3) | `original_title` |
| 13584236 | Fifty Shades Trilogy (Fifty Shades, #1-3) | `language_code` |
| 13586743 | One Last Thing Before I Go | `language_code` |
| 13588356 | Daring Greatly: How the Courage to Be Vulnerable Transforms the Way We Live, Love, Parent, and Lead | `language_code` |
| 13589182 | Mastery | `language_code` |
| 13593526 | City of Women | `original_title` |
| 13593526 | City of Women | `language_code` |
| 13593553 | To Sell Is Human: The Surprising Truth About Moving Others | `original_title` |
| 13593553 | To Sell Is Human: The Surprising Truth About Moving Others | `language_code` |
| 13593555 | Mad River (Virgil Flowers, #6) | `original_title` |
| 13600318 | Reckless (Thoughtless, #3) | `isbn` |
| 13600318 | Reckless (Thoughtless, #3) | `isbn13` |
| 13601550 | Accidentally on Purpose (Accidentally on Purpose, #1) | `isbn` |
| 13601550 | Accidentally on Purpose (Accidentally on Purpose, #1) | `isbn13` |
| 13601550 | Accidentally on Purpose (Accidentally on Purpose, #1) | `original_title` |
| 13603717 | First Shift: Legacy (Shift, #1) | `isbn` |
| 13603717 | First Shift: Legacy (Shift, #1) | `isbn13` |
| 13605723 | Sentinel (Covenant, #5) | `original_title` |
| 13605727 | Elixir (Covenant, #3.5) | `language_code` |
| 13612739 | Seduced in the Dark (The Dark Duet, #2) | `isbn` |
| 13612739 | Seduced in the Dark (The Dark Duet, #2) | `isbn13` |
| 13612739 | Seduced in the Dark (The Dark Duet, #2) | `original_title` |
| 13623012 | The Prisoner of Heaven (The Cemetery of Forgotten Books, #3) | `language_code` |
| 13624367 | Checkmate (Neighbor from Hell, #3) | `isbn` |
| 13624367 | Checkmate (Neighbor from Hell, #3) | `isbn13` |
| 13628812 | The Rent Collector | `original_title` |
| 13634927 | A Leaf on the Wind of All Hallows (Outlander, #8.5) | `isbn` |
| 13634927 | A Leaf on the Wind of All Hallows (Outlander, #8.5) | `isbn13` |
| 13638570 | Out of Breath (Breathing, #3) | `isbn` |
| 13638570 | Out of Breath (Breathing, #3) | `isbn13` |
| 13640229 | Creed (Unfinished Hero, #2) | `isbn` |
| 13640229 | Creed (Unfinished Hero, #2) | `isbn13` |
| 13642929 | My Beloved World | `original_title` |
| 13643567 | The Evolution of Mara Dyer (Mara Dyer, #2) | `isbn` |
| 13643567 | The Evolution of Mara Dyer (Mara Dyer, #2) | `isbn13` |
| 13649056 | Try Me (One Night with Sole Regret, #1) | `isbn` |
| 13649056 | Try Me (One Night with Sole Regret, #1) | `isbn13` |
| 13765729 | Abducted (Lizzy Gardner #1) | `isbn` |
| 13765729 | Abducted (Lizzy Gardner #1) | `isbn13` |
| 14060046 | Obsession | `isbn` |
| 14060046 | Obsession | `isbn13` |
| 14060046 | Obsession | `original_title` |
| 14165516 | The Marriage Trap (Marriage to a Billionaire, #2) | `isbn` |
| 14165516 | The Marriage Trap (Marriage to a Billionaire, #2) | `isbn13` |
| 14367051 | City of Bones / City of Ashes / City of Glass / City of Fallen Angels / City of Lost Souls (The Mortal Instruments, #1-5) | `original_title` |
| 14367051 | City of Bones / City of Ashes / City of Glass / City of Fallen Angels / City of Lost Souls (The Mortal Instruments, #1-5) | `language_code` |
| 14740588 | Notorious Nineteen (Stephanie Plum, #19) | `isbn` |
| 14740588 | Notorious Nineteen (Stephanie Plum, #19) | `isbn13` |
| 14744381 | The Walking Dead, Compendium 2 | `original_title` |
| 14745338 | Fairest (An Unfortunate Fairy Tale, #2) | `isbn` |
| 14745338 | Fairest (An Unfortunate Fairy Tale, #2) | `isbn13` |
| 14745338 | Fairest (An Unfortunate Fairy Tale, #2) | `original_title` |
| 14781501 | NYPD Red (NYPD Red, #1) | `language_code` |
| 14889780 | Two Graves (Pendergast, #12) | `language_code` |
| 15034320 | Pines (Wayward Pines, #1) | `language_code` |
| 15059301 | Captured (The Captive, #1) | `isbn` |
| 15059301 | Captured (The Captive, #1) | `isbn13` |
| 15059301 | Captured (The Captive, #1) | `original_title` |
| 15062217 | 14 | `isbn` |
| 15062217 | 14 | `isbn13` |
| 15283043 | The Distance Between Us | `original_title` |
| 15513156 | Of Triton (The Syrena Legacy, #2) | `original_title` |
| 15704001 | Seduction and Snacks (Chocolate Lovers, #1) | `isbn` |
| 15704001 | Seduction and Snacks (Chocolate Lovers, #1) | `isbn13` |
| 15717721 | If I Were You (Inside Out, #1) | `isbn` |
| 15717721 | If I Were You (Inside Out, #1) | `isbn13` |
| 15722284 | Saint Odd (Odd Thomas, #7) | `isbn` |
| 15722284 | Saint Odd (Odd Thomas, #7) | `isbn13` |
| 15723286 | Curtsies & Conspiracies (Finishing School, #2) | `isbn` |
| 15723286 | Curtsies & Conspiracies (Finishing School, #2) | `isbn13` |
| 15724654 | The Mighty Storm (The Storm, #1) | `isbn` |
| 15724654 | The Mighty Storm (The Storm, #1) | `isbn13` |
| 15728921 | Don't Let Me Go | `isbn` |
| 15728921 | Don't Let Me Go | `isbn13` |
| 15729261 | The Marriage Mistake (Marriage to a Billionaire, #3) | `isbn` |
| 15729261 | The Marriage Mistake (Marriage to a Billionaire, #3) | `isbn13` |
| 15730101 | The Call of Cthulhu | `isbn` |
| 15730101 | The Call of Cthulhu | `isbn13` |
| 15733346 | Is It Just Me? | `original_title` |
| 15733851 | You Had Me At Hello | `language_code` |
| 15734464 | 12th of Never (Women's Murder Club, #12) | `isbn` |
| 15734464 | 12th of Never (Women's Murder Club, #12) | `isbn13` |
| 15737147 | Help Thanks Wow: The Three Essential Prayers | `original_title` |
| 15738951 | Deep Down (Jack Reacher, #16.5) | `isbn` |
| 15738951 | Deep Down (Jack Reacher, #16.5) | `isbn13` |
| 15739018 | Taking Chances (Taking Chances, #1) | `isbn` |
| 15739018 | Taking Chances (Taking Chances, #1) | `isbn13` |
| 15739018 | Taking Chances (Taking Chances, #1) | `original_title` |
| 15742039 | Breathe (Colorado Mountain, #4) | `isbn` |
| 15742039 | Breathe (Colorado Mountain, #4) | `isbn13` |
| 15743078 | The Divergent Series 2-Book Collection (Divergent, #1-2) | `original_title` |
| 15745371 | Chosen at Nightfall (Shadow Falls, #5) | `original_title` |
| 15748335 | Leave Me Breathless (Ross Siblings, #3) | `isbn` |
| 15748335 | Leave Me Breathless (Ross Siblings, #3) | `isbn13` |
| 15748335 | Leave Me Breathless (Ross Siblings, #3) | `original_title` |
| 15749186 | To All the Boys I've Loved Before (To All the Boys I've Loved Before, #1) | `isbn` |
| 15749186 | To All the Boys I've Loved Before (To All the Boys I've Loved Before, #1) | `isbn13` |
| 15752757 | Rock Chick Revolution (Rock Chick, #8) | `isbn` |
| 15752757 | Rock Chick Revolution (Rock Chick, #8) | `isbn13` |
| 15752757 | Rock Chick Revolution (Rock Chick, #8) | `original_title` |
| 15757434 | Crash (Crash, #1) | `isbn` |
| 15757434 | Crash (Crash, #1) | `isbn13` |
| 15760001 | On Dublin Street (On Dublin Street, #1) | `isbn` |
| 15760001 | On Dublin Street (On Dublin Street, #1) | `isbn13` |
| 15761241 | The Wild Ones (The Wild Ones, #1) | `isbn` |
| 15761241 | The Wild Ones (The Wild Ones, #1) | `isbn13` |
| 15762657 | Seducing Cinderella (Fighting for Love, #1) | `isbn` |
| 15762657 | Seducing Cinderella (Fighting for Love, #1) | `isbn13` |
| 15762975 | Wrong Bed, Right Guy (Come Undone, #1) | `isbn` |
| 15762975 | Wrong Bed, Right Guy (Come Undone, #1) | `isbn13` |
| 15766776 | Rump: The True Story of Rumpelstiltskin | `original_title` |
| 15768191 | Sweet Peril (Sweet, #2) | `original_title` |
| 15768536 | Fall From Grace (Mad World, #1) | `isbn` |
| 15768536 | Fall From Grace (Mad World, #1) | `isbn13` |
| 15768536 | Fall From Grace (Mad World, #1) | `original_title` |
| 15771862 | Wave | `isbn` |
| 15771862 | Wave | `isbn13` |
| 15776904 | The Beggar King (The Hangman's Daughter, #3) | `isbn` |
| 15776904 | The Beggar King (The Hangman's Daughter, #3) | `isbn13` |
| 15778138 | Just for Now (Sea Breeze, #4) | `isbn` |
| 15778138 | Just for Now (Sea Breeze, #4) | `isbn13` |
| 15783307 | The Perfect Game (The Perfect Game, #1) | `isbn` |
| 15783307 | The Perfect Game (The Perfect Game, #1) | `isbn13` |
| 15784909 | This Girl (Slammed, #3) | `isbn` |
| 15784909 | This Girl (Slammed, #3) | `isbn13` |
| 15786110 | Relish: My Life in the Kitchen | `original_title` |
| 15791403 | Mistress | `language_code` |
| 15793165 | Don't Go | `original_title` |
| 15797722 | Deeply Odd (Odd Thomas, #6) | `original_title` |
| 15801668 | The Girls of Atomic City: The Untold Story of the Women Who Helped Win World War II | `original_title` |
| 15811495 | Touch & Go (Tessa Leoni, #2) | `original_title` |
| 15811520 | Detroit: An American Autopsy | `original_title` |
| 15820492 | Annabel (Delirium, #0.5) | `language_code` |
| 15820748 | The Prince (The Selection, #0.5) | `language_code` |
| 15828714 | Sometimes It Lasts (Sea Breeze, #5) | `isbn` |
| 15828714 | Sometimes It Lasts (Sea Breeze, #5) | `isbn13` |
| 15832316 | Dirty Red (Love Me with Lies, #2) | `isbn` |
| 15832316 | Dirty Red (Love Me with Lies, #2) | `isbn13` |
| 15835685 | Clash (Crash, #2) | `isbn` |
| 15835685 | Clash (Crash, #2) | `isbn13` |
| 15843166 | You Are a Badass: How to Stop Doubting Your Greatness and Start Living an Awesome Life | `original_title` |
| 15843166 | You Are a Badass: How to Stop Doubting Your Greatness and Start Living an Awesome Life | `language_code` |
| 15849910 | The King's Curse (The Plantagenet and Tudor Novels, #7) | `original_title` |
| 15852756 | Naked (The Blackstone Affair, #1) | `isbn` |
| 15852756 | Naked (The Blackstone Affair, #1) | `isbn13` |
| 15902792 | Still Foolin' 'Em: Where I've Been, Where I'm Going, and Where the Hell Are My Keys | `original_title` |
| 15981894 | Devoured (Devoured, #1) | `isbn` |
| 15981894 | Devoured (Devoured, #1) | `isbn13` |
| 15993374 | Charade (Games, #1) | `isbn` |
| 15993374 | Charade (Games, #1) | `isbn13` |
| 16001443 | All In (The Blackstone Affair, #2) | `isbn` |
| 16001443 | All In (The Blackstone Affair, #2) | `isbn13` |
| 16001893 | Down to You (The Bad Boys, #1) | `isbn` |
| 16001893 | Down to You (The Bad Boys, #1) | `isbn13` |
| 16007855 | Sweet Reckoning (Sweet, #3) | `original_title` |
| 16031620 | الفيل الأزرق | `isbn` |
| 16031620 | الفيل الأزرق | `isbn13` |
| 16031679 | Tempting the Player (Gamble Brothers, #2) | `language_code` |
| 16041169 | Disastrous (Disastrous, #1) | `original_title` |
| 16042305 | Love Left Behind | `isbn` |
| 16042305 | Love Left Behind | `isbn13` |
| 16042305 | Love Left Behind | `original_title` |
| 16045144 | The Beautiful Mystery (Chief Inspector Armand Gamache, #8) | `language_code` |
| 16045855 | Crush (Crush, #1) | `isbn` |
| 16045855 | Crush (Crush, #1) | `isbn13` |
| 16045855 | Crush (Crush, #1) | `original_title` |
| 16047244 | Rock the Heart (Black Falcon, #1) | `isbn` |
| 16047244 | Rock the Heart (Black Falcon, #1) | `isbn13` |
| 16053316 | Wethering the Storm (The Storm, #2) | `isbn` |
| 16053316 | Wethering the Storm (The Storm, #2) | `isbn13` |
| 16056862 | The Unwanted Wife (Unwanted, #1) | `isbn` |
| 16056862 | The Unwanted Wife (Unwanted, #1) | `isbn13` |
| 16058610 | Whistling Past the Graveyard | `original_title` |
| 16066586 | The Cellar (The Cellar, #1) | `isbn` |
| 16066586 | The Cellar (The Cellar, #1) | `isbn13` |
| 16066586 | The Cellar (The Cellar, #1) | `original_title` |
| 16068905 | Fangirl | `isbn` |
| 16068905 | Fangirl | `isbn13` |
| 16068905 | Fangirl | `original_title` |
| 16070018 | Truth (Consequences, #2) | `original_title` |
| 16070521 | Come Away with Me (With Me in Seattle, #1) | `isbn` |
| 16070521 | Come Away with Me (With Me in Seattle, #1) | `isbn13` |
| 16070903 | Fallen Too Far (Rosemary Beach, #1; Too Far, #1) | `isbn` |
| 16070903 | Fallen Too Far (Rosemary Beach, #1; Too Far, #1) | `isbn13` |
| 16076787 | السنجة | `isbn` |
| 16076787 | السنجة | `isbn13` |
| 16079228 | Beautifully Damaged (Beautifully Damaged, #1) | `isbn` |
| 16079228 | Beautifully Damaged (Beautifully Damaged, #1) | `isbn13` |
| 16081202 | Open Road Summer | `isbn` |
| 16081202 | Open Road Summer | `isbn13` |
| 16081754 | Find You in the Dark (Find You in the Dark, #1) | `isbn` |
| 16081754 | Find You in the Dark (Find You in the Dark, #1) | `isbn13` |
| 16081961 | الأسود يليق بك | `isbn` |
| 16081961 | الأسود يليق بك | `isbn13` |
| 16084702 | Fifty Shades Duo: Fifty Shades Darker / Fifty Shades Freed (Fifty Shades, #2-3) | `isbn` |
| 16084702 | Fifty Shades Duo: Fifty Shades Darker / Fifty Shades Freed (Fifty Shades, #2-3) | `isbn13` |
| 16084702 | Fifty Shades Duo: Fifty Shades Darker / Fifty Shades Freed (Fifty Shades, #2-3) | `original_title` |
| 16090636 | Fight with Me (With Me in Seattle, #2) | `isbn` |
| 16090636 | Fight with Me (With Me in Seattle, #2) | `isbn13` |
| 16090636 | Fight with Me (With Me in Seattle, #2) | `original_title` |
| 16090981 | Thief (Love Me with Lies, #3) | `isbn` |
| 16090981 | Thief (Love Me with Lies, #3) | `isbn13` |
| 16093188 | Up to Me (The Bad Boys, #2) | `isbn` |
| 16093188 | Up to Me (The Bad Boys, #2) | `isbn13` |
| 16096873 | Revealed (House of Night, #11) | `isbn` |
| 16096873 | Revealed (House of Night, #11) | `isbn13` |
| 16102880 | Bad Rep (Bad Rep, #1) | `isbn` |
| 16102880 | Bad Rep (Bad Rep, #1) | `isbn13` |
| 16102880 | Bad Rep (Bad Rep, #1) | `original_title` |
| 16109563 | Undeniable (Undeniable, #1) | `isbn` |
| 16109563 | Undeniable (Undeniable, #1) | `isbn13` |
| 16113791 | The Coincidence of Callie & Kayden (The Coincidence, #1) | `isbn` |
| 16113791 | The Coincidence of Callie & Kayden (The Coincidence, #1) | `isbn13` |
| 16114861 | Unbeautifully (Undeniable, #2) | `isbn` |
| 16114861 | Unbeautifully (Undeniable, #2) | `isbn13` |
| 16114861 | Unbeautifully (Undeniable, #2) | `original_title` |
| 16114862 | Unattainable (Undeniable, #3) | `isbn` |
| 16114862 | Unattainable (Undeniable, #3) | `isbn13` |
| 16114862 | Unattainable (Undeniable, #3) | `original_title` |
| 16117182 | Broken Silence (Silence, #2) | `isbn` |
| 16117182 | Broken Silence (Silence, #2) | `isbn13` |
| 16117804 | The Proposal (The Proposition, #2) | `isbn` |
| 16117804 | The Proposal (The Proposition, #2) | `isbn13` |
| 16119079 | Forever My Girl (The Beaumont Series, #1) | `original_title` |
| 16122163 | From Ashes (From Ashes, #1) | `original_title` |
| 16122643 | Eyes Wide Open (The Blackstone Affair, #3) | `isbn` |
| 16122643 | Eyes Wide Open (The Blackstone Affair, #3) | `isbn13` |
| 16124019 | Waking Up Married (Waking Up, #1) | `isbn` |
| 16124019 | Waking Up Married (Waking Up, #1) | `isbn13` |
| 16130986 | An Innocent Client | `isbn` |
| 16130986 | An Innocent Client | `isbn13` |
| 16131484 | The Infinite Sea (The 5th Wave, #2) | `isbn` |
| 16131484 | The Infinite Sea (The 5th Wave, #2) | `isbn13` |
| 16134551 | Fallen Crest High (Fallen Crest High, #1) | `isbn` |
| 16134551 | Fallen Crest High (Fallen Crest High, #1) | `isbn13` |
| 16134782 | In Flight (Up in the Air, #1) | `isbn` |
| 16134782 | In Flight (Up in the Air, #1) | `isbn13` |
| 16136959 | Mile High (Up in the Air, #2) | `isbn` |
| 16136959 | Mile High (Up in the Air, #2) | `isbn13` |
| 16139641 | Grounded (Up in the Air, #3) | `isbn` |
| 16139641 | Grounded (Up in the Air, #3) | `isbn13` |
| 16140036 | This Man (This Man, #1) | `isbn` |
| 16140036 | This Man (This Man, #1) | `isbn13` |
| 16141924 | Dad Is Fat | `language_code` |
| 16143347 | We Were Liars | `isbn` |
| 16143347 | We Were Liars | `isbn13` |
| 16148398 | Saga #1 | `isbn` |
| 16148398 | Saga #1 | `isbn13` |
| 16148938 | Second Shift: Order (Shift, #2) | `isbn` |
| 16148938 | Second Shift: Order (Shift, #2) | `isbn13` |
| 16148938 | Second Shift: Order (Shift, #2) | `original_title` |
| 16150119 | Wired (Wired, #1) | `isbn` |
| 16150119 | Wired (Wired, #1) | `isbn13` |
| 16150119 | Wired (Wired, #1) | `original_title` |
| 16150996 | Convicted (Consequences, #3) | `isbn` |
| 16150996 | Convicted (Consequences, #3) | `isbn13` |
| 16150996 | Convicted (Consequences, #3) | `original_title` |
| 16151178 | The Sea of Tranquility | `isbn` |
| 16151178 | The Sea of Tranquility | `isbn13` |
| 16152943 | Wanted (Wanted, #1) | `original_title` |
| 16163690 | Own the Wind (Chaos, #1) | `isbn` |
| 16163690 | Own the Wind (Chaos, #1) | `isbn13` |
| 16170522 | صانع الظلام | `isbn` |
| 16170522 | صانع الظلام | `isbn13` |
| 16170625 | المانيفستو | `isbn` |
| 16170625 | المانيفستو | `isbn13` |
| 16174197 | Knight & Play (Knight, #1) | `isbn` |
| 16174197 | Knight & Play (Knight, #1) | `isbn13` |
| 16175040 | Endless Knight (The Arcana Chronicles, #2) | `isbn` |
| 16175040 | Endless Knight (The Arcana Chronicles, #2) | `isbn13` |
| 16182601 | Bread and   Wine: A Love Letter to Life Around the Table with Recipes | `original_title` |
| 16218778 | Coming Clean | `original_title` |
| 16233105 | Someone to Love (Someone to Love, #1) | `isbn` |
| 16233105 | Someone to Love (Someone to Love, #1) | `isbn13` |
| 16248139 | The Last Original Wife | `original_title` |
| 16248196 | The Art of Thinking Clearly | `language_code` |
| 16277248 | Avatar: The Last Airbender (The Search, #1) | `original_title` |
| 16279715 | Connected (Connections, #1) | `isbn` |
| 16279715 | Connected (Connections, #1) | `isbn13` |
| 16299256 | The Game Changer (The Perfect Game, #2) | `isbn` |
| 16299256 | The Game Changer (The Perfect Game, #2) | `isbn13` |
| 16299256 | The Game Changer (The Perfect Game, #2) | `original_title` |
| 16299991 | A Quest of Heroes (The Sorcerer's Ring, #1) | `isbn` |
| 16299991 | A Quest of Heroes (The Sorcerer's Ring, #1) | `isbn13` |
| 16299991 | A Quest of Heroes (The Sorcerer's Ring, #1) | `original_title` |
| 16301111 | Always You (Best Friend, #1) | `isbn` |
| 16301111 | Always You (Best Friend, #1) | `isbn13` |
| 16429619 | The Kiss of Deception (The Remnant Chronicles, #1) | `isbn` |
| 16429619 | The Kiss of Deception (The Remnant Chronicles, #1) | `isbn13` |
| 16479439 | Ex-Heroes (Ex-Heroes, #1) | `language_code` |
| 16704759 | Knight & Stay (Knight, #2) | `isbn` |
| 16704759 | Knight & Stay (Knight, #2) | `isbn13` |
| 16704759 | Knight & Stay (Knight, #2) | `original_title` |
| 17032328 | If You Stay (Beautifully Broken, #1) | `isbn` |
| 17032328 | If You Stay (Beautifully Broken, #1) | `isbn13` |
| 17158513 | Captive Prince: Volume Two (Captive Prince, #2) | `isbn` |
| 17158513 | Captive Prince: Volume Two (Captive Prince, #2) | `isbn13` |
| 17158596 | Collide (Collide, #1) | `isbn` |
| 17158596 | Collide (Collide, #1) | `isbn13` |
| 17166702 | True Love Story | `isbn` |
| 17166702 | True Love Story | `isbn13` |
| 17167042 | Fighting for Flight (Fighting, #1) | `isbn` |
| 17167042 | Fighting for Flight (Fighting, #1) | `isbn13` |
| 17167042 | Fighting for Flight (Fighting, #1) | `original_title` |
| 17181905 | The Arrangement: The Ferro Family (The Arrangement, #1) | `isbn` |
| 17181905 | The Arrangement: The Ferro Family (The Arrangement, #1) | `isbn13` |
| 17181905 | The Arrangement: The Ferro Family (The Arrangement, #1) | `original_title` |
| 17190226 | Surrender Your Love (Surrender Your Love, #1) | `isbn` |
| 17190226 | Surrender Your Love (Surrender Your Love, #1) | `isbn13` |
| 17191012 | Fallen Crest Family (Fallen Crest High, #2) | `isbn` |
| 17191012 | Fallen Crest Family (Fallen Crest High, #2) | `isbn13` |
| 17191012 | Fallen Crest Family (Fallen Crest High, #2) | `original_title` |
| 17200687 | Rule (Marked Men, #1) | `isbn` |
| 17200687 | Rule (Marked Men, #1) | `isbn13` |
| 17201095 | Play with Me (With Me in Seattle, #3) | `isbn` |
| 17201095 | Play with Me (With Me in Seattle, #3) | `isbn13` |
| 17201104 | Rock with Me (With Me in Seattle, #4) | `isbn` |
| 17201104 | Rock with Me (With Me in Seattle, #4) | `isbn13` |
| 17201110 | Safe with Me (With Me in Seattle, #5) | `isbn` |
| 17201110 | Safe with Me (With Me in Seattle, #5) | `isbn13` |
| 17201110 | Safe with Me (With Me in Seattle, #5) | `original_title` |
| 17204568 | Crazy Little Thing (Bell Harbor, #1) | `isbn` |
| 17204568 | Crazy Little Thing (Bell Harbor, #1) | `isbn13` |
| 17204860 | Jet (Marked Men, #2) | `isbn` |
| 17204860 | Jet (Marked Men, #2) | `isbn13` |
| 17225311 | Tampa | `language_code` |
| 17228280 | Better off Friends | `isbn` |
| 17228280 | Better off Friends | `isbn13` |
| 17235347 | Life Before Legend: Stories of the Criminal and the Prodigy (Legend, #0.5) | `isbn` |
| 17235347 | Life Before Legend: Stories of the Criminal and the Prodigy (Legend, #0.5) | `isbn13` |
| 17255186 | The Phoenix Project: A Novel About IT, DevOps, and Helping Your Business Win | `original_title` |
| 17255265 | This Man Confessed (This Man, #3) | `isbn` |
| 17255265 | This Man Confessed (This Man, #3) | `isbn13` |
| 17255435 | A Shade of Vampire (A Shade of Vampire, #1) | `original_title` |
| 17257484 | Trouble | `isbn` |
| 17257484 | Trouble | `isbn13` |
| 17257990 | Fire Inside (Chaos, #2) | `isbn` |
| 17257990 | Fire Inside (Chaos, #2) | `isbn13` |
| 17257990 | Fire Inside (Chaos, #2) | `original_title` |
| 17257993 | Raid (Unfinished Hero, #3) | `isbn` |
| 17257993 | Raid (Unfinished Hero, #3) | `isbn13` |
| 17267122 | Pulse (Collide, #2) | `isbn` |
| 17267122 | Pulse (Collide, #2) | `isbn13` |
| 17286162 | Forever Black (Forever, #1) | `isbn` |
| 17286162 | Forever Black (Forever, #1) | `isbn13` |
| 17287009 | Humans of New York | `original_title` |
| 17287028 | My Story | `original_title` |
| 17306293 | Shift (Silo, #2) | `isbn` |
| 17306293 | Shift (Silo, #2) | `isbn13` |
| 17314410 | Beauty from Surrender (Beauty, #2) | `isbn` |
| 17314410 | Beauty from Surrender (Beauty, #2) | `isbn13` |
| 17314430 | Wait for You (Wait for You, #1) | `isbn` |
| 17314430 | Wait for You (Wait for You, #1) | `isbn13` |
| 17316075 | Second Chance Boyfriend (One Week Girlfriend, #2) | `isbn` |
| 17316075 | Second Chance Boyfriend (One Week Girlfriend, #2) | `isbn13` |
| 17317675 | Epilogue (The Dark Duet, #3) | `isbn` |
| 17317675 | Epilogue (The Dark Duet, #3) | `isbn13` |
| 17317675 | Epilogue (The Dark Duet, #3) | `original_title` |
| 17331349 | Think Like a Freak | `original_title` |
| 17333237 | Stella Bain | `original_title` |
| 17333237 | Stella Bain | `language_code` |
| 17333880 | Twisted Perfection (Rosemary Beach, #5; Perfection, #1) | `isbn` |
| 17333880 | Twisted Perfection (Rosemary Beach, #5; Perfection, #1) | `isbn13` |
| 17334079 | What Really Happened in Peru (The Bane Chronicles, #1) | `original_title` |
| 17336849 | Lost & Found (Lost & Found, #1) | `original_title` |
| 17337562 | Forever Too Far (Rosemary Beach, #3; Too Far, #3) | `isbn` |
| 17337562 | Forever Too Far (Rosemary Beach, #3; Too Far, #3) | `isbn13` |
| 17339590 | "حكايات فرغلي المستكاوي "حكايتى مع كفر السحلاوية | `isbn` |
| 17339590 | "حكايات فرغلي المستكاوي "حكايتى مع كفر السحلاوية | `isbn13` |
| 17340050 | Losing Hope (Hopeless, #2) | `isbn` |
| 17340050 | Losing Hope (Hopeless, #2) | `isbn13` |
| 17348985 | Help for the Haunted | `original_title` |
| 17375956 | Reaper's Property (Reapers MC, #1) | `isbn` |
| 17375956 | Reaper's Property (Reapers MC, #1) | `isbn13` |
| 17377032 | Bad Things (Tristan & Danika, #1) | `isbn` |
| 17377032 | Bad Things (Tristan & Danika, #1) | `isbn13` |
| 17377032 | Bad Things (Tristan & Danika, #1) | `original_title` |
| 17383994 | Divergent Series Complete Box Set (Divergent, #1-3) | `original_title` |
| 17401198 | Only the Innocent (DCI Tom Douglas #1) | `isbn` |
| 17401198 | Only the Innocent (DCI Tom Douglas #1) | `isbn13` |
| 17404452 | Forever You (Forever, #2) | `isbn` |
| 17404452 | Forever You (Forever, #2) | `isbn13` |
| 17404452 | Forever You (Forever, #2) | `original_title` |
| 17406847 | Defy (Defy, #1) | `isbn` |
| 17406847 | Defy (Defy, #1) | `isbn13` |
| 17407233 | The Submissive (Submissive, #1) | `isbn` |
| 17407233 | The Submissive (Submissive, #1) | `isbn13` |
| 17448960 | Falling into You (Falling, #1) | `isbn` |
| 17448960 | Falling into You (Falling, #1) | `isbn13` |
| 17449417 | Simple Perfection (Rosemary Beach, #6; Perfection, #2) | `isbn` |
| 17449417 | Simple Perfection (Rosemary Beach, #6; Perfection, #2) | `isbn13` |
| 17455541 | Happy, Happy, Happy | `isbn` |
| 17455541 | Happy, Happy, Happy | `isbn13` |
| 17455585 | White Hot Kiss (The Dark Elements, #1) | `isbn` |
| 17455585 | White Hot Kiss (The Dark Elements, #1) | `isbn13` |
| 17455815 | Stone Cold Touch (The Dark Elements, #2) | `isbn` |
| 17455815 | Stone Cold Touch (The Dark Elements, #2) | `isbn13` |
| 17465470 | The Royal Ranger (Ranger's Apprentice, #12) | `language_code` |
| 17504320 | Taking Shots (Assassins, #1) | `isbn` |
| 17504320 | Taking Shots (Assassins, #1) | `isbn13` |
| 17504320 | Taking Shots (Assassins, #1) | `original_title` |
| 17524166 | نادي السيارات | `isbn` |
| 17524166 | نادي السيارات | `isbn13` |
| 17524166 | نادي السيارات | `original_title` |
| 17557143 | The Billionaire's Obsession ~ Simon (The Billionaire's Obsession, #1) | `isbn` |
| 17557143 | The Billionaire's Obsession ~ Simon (The Billionaire's Obsession, #1) | `isbn13` |
| 17558817 | Be with Me (Wait for You, #2) | `isbn` |
| 17558817 | Be with Me (Wait for You, #2) | `isbn13` |
| 17560674 | The Bet (The Bet, #1) | `isbn` |
| 17560674 | The Bet (The Bet, #1) | `isbn13` |
| 17563080 | Murder of Crows (The Others, #2) | `isbn` |
| 17563080 | Murder of Crows (The Others, #2) | `isbn13` |
| 17563539 | The Egg | `isbn` |
| 17563539 | The Egg | `isbn13` |
| 17569860 | Conquer Your Love (Surrender Your Love, #2) | `original_title` |
| 17570538 | The Blood Mirror (Lightbringer, #4) | `isbn` |
| 17570538 | The Blood Mirror (Lightbringer, #4) | `isbn13` |
| 17571564 | Hyperbole and a Half: Unfortunate Situations, Flawed Coping Mechanisms, Mayhem, and Other Things That Happened | `original_title` |
| 17660462 | The Everything Store: Jeff Bezos and the Age of Amazon | `original_title` |
| 17667452 | When I Found You | `isbn` |
| 17667452 | When I Found You | `isbn13` |
| 17667561 | The Shadow Throne (The Ascendance Trilogy, #3) | `isbn` |
| 17667561 | The Shadow Throne (The Ascendance Trilogy, #3) | `isbn13` |
| 17673271 | Si-cology 1: Tales and Wisdom from Duck Dynasty’s Favorite Uncle | `original_title` |
| 17673307 | Neanderthal Seeks Human (Knitting in the City, #1) | `isbn` |
| 17673307 | Neanderthal Seeks Human (Knitting in the City, #1) | `isbn13` |
| 17674991 | Paddle Your Own Canoe: One Man's Fundamentals for Delicious Living | `original_title` |
| 17675031 | This Star Won't Go Out: The Life and Words of Esther Grace Earl | `original_title` |
| 17704902 | Five Days at Memorial: Life and Death in a Storm-Ravaged Hospital | `original_title` |
| 17707603 | George Washington's Secret Six: The Spy Ring That Saved the American Revolution | `original_title` |
| 17726978 | The Magpies | `original_title` |
| 17729712 | Beautiful Broken Rules (Broken, #1) | `isbn` |
| 17729712 | Beautiful Broken Rules (Broken, #1) | `isbn13` |
| 17729712 | Beautiful Broken Rules (Broken, #1) | `original_title` |
| 17733861 | A Shade of Blood (A Shade of Vampire, #2) | `isbn` |
| 17733861 | A Shade of Blood (A Shade of Vampire, #2) | `isbn13` |
| 17733861 | A Shade of Blood (A Shade of Vampire, #2) | `original_publication_year` |
| 17733861 | A Shade of Blood (A Shade of Vampire, #2) | `original_title` |
| 17788401 | Ugly Love | `isbn` |
| 17788401 | Ugly Love | `isbn13` |
| 17792606 | Mine (Real, #2) | `isbn` |
| 17792606 | Mine (Real, #2) | `isbn13` |
| 17794657 | The Lake (The Lake Trilogy #1) | `isbn` |
| 17794657 | The Lake (The Lake Trilogy #1) | `isbn13` |
| 17794657 | The Lake (The Lake Trilogy #1) | `original_title` |
| 17798233 | Rome (Marked Men, #3) | `isbn` |
| 17798233 | Rome (Marked Men, #3) | `isbn13` |
| 17798287 | Driven (Driven, #1) | `isbn` |
| 17798287 | Driven (Driven, #1) | `isbn13` |
| 17800786 | Damaged 2 (Damaged, #2) | `isbn` |
| 17800786 | Damaged 2 (Damaged, #2) | `isbn13` |
| 17800786 | Damaged 2 (Damaged, #2) | `original_title` |
| 17825503 | Leo | `isbn` |
| 17825503 | Leo | `isbn13` |
| 17830559 | Remy (Real, #3) | `isbn` |
| 17830559 | Remy (Real, #3) | `isbn13` |
| 17830559 | Remy (Real, #3) | `original_title` |
| 17831614 | Beautiful Player (Beautiful Bastard, #3) | `isbn` |
| 17831614 | Beautiful Player (Beautiful Bastard, #3) | `isbn13` |
| 17831616 | Beautiful Bitch (Beautiful Bastard, #1.5) | `isbn` |
| 17831616 | Beautiful Bitch (Beautiful Bastard, #1.5) | `isbn13` |
| 17831617 | Beautiful Bombshell (Beautiful Bastard, #2.5) | `isbn` |
| 17831617 | Beautiful Bombshell (Beautiful Bastard, #2.5) | `isbn13` |
| 17831619 | Beautiful Beginning (Beautiful Bastard, #3.5) | `isbn` |
| 17831619 | Beautiful Beginning (Beautiful Bastard, #3.5) | `isbn13` |
| 17831619 | Beautiful Beginning (Beautiful Bastard, #3.5) | `original_title` |
| 17833099 | Price of a Kiss (Forbidden Men, #1) | `isbn` |
| 17833099 | Price of a Kiss (Forbidden Men, #1) | `isbn13` |
| 17833099 | Price of a Kiss (Forbidden Men, #1) | `original_title` |
| 17835351 | Nikola Tesla: Imagination and the Man That Invented the 20th Century | `isbn` |
| 17835351 | Nikola Tesla: Imagination and the Man That Invented the 20th Century | `isbn13` |
| 17835766 | One More Chance (Rosemary Beach, #8; Chance, #2) | `isbn` |
| 17835766 | One More Chance (Rosemary Beach, #8; Chance, #2) | `isbn13` |
| 17835773 | Misbehaving (Sea Breeze, #6) | `isbn` |
| 17835773 | Misbehaving (Sea Breeze, #6) | `isbn13` |
| 17860199 | The World of Divergent: The Path to Allegiant (Divergent, #2.5) | `original_title` |
| 17860217 | Trust in Me (Wait for You, #1.5) | `isbn` |
| 17860217 | Trust in Me (Wait for You, #1.5) | `isbn13` |
| 17880708 | Fueled (Driven, #2) | `isbn` |
| 17880708 | Fueled (Driven, #2) | `isbn13` |
| 17880714 | Crashed (Driven, #3) | `isbn` |
| 17880714 | Crashed (Driven, #3) | `isbn13` |
| 17899392 | First Love | `language_code` |
| 17903381 | Diary ng Panget | `isbn` |
| 17903381 | Diary ng Panget | `isbn13` |
| 17903381 | Diary ng Panget | `original_title` |
| 17925397 | A Castle of Sand (A Shade of Vampire, #3) | `isbn` |
| 17925397 | A Castle of Sand (A Shade of Vampire, #3) | `isbn13` |
| 17925397 | A Castle of Sand (A Shade of Vampire, #3) | `original_title` |
| 17927395 | A Court of Mist and Fury (A Court of Thorns and Roses, #2) | `isbn` |
| 17927395 | A Court of Mist and Fury (A Court of Thorns and Roses, #2) | `isbn13` |
| 17930773 | Found in You (Fixed, #2) | `isbn` |
| 17930773 | Found in You (Fixed, #2) | `isbn13` |
| 17934385 | Tempting Fate | `original_title` |
| 17948485 | Friend-Zoned (Friend-Zoned, #1) | `isbn` |
| 17948485 | Friend-Zoned (Friend-Zoned, #1) | `isbn13` |
| 17948485 | Friend-Zoned (Friend-Zoned, #1) | `original_title` |
| 17950614 | UnDivided (Unwind, #4) | `isbn` |
| 17950614 | UnDivided (Unwind, #4) | `isbn13` |
| 17970255 | Into the Deep (Into the Deep, #1) | `isbn` |
| 17970255 | Into the Deep (Into the Deep, #1) | `isbn13` |
| 17973653 | Shine Not Burn (Shine Not Burn, #1) | `isbn` |
| 17973653 | Shine Not Burn (Shine Not Burn, #1) | `isbn13` |
| 17977710 | Twisted (Tangled, #2) | `isbn` |
| 17977710 | Twisted (Tangled, #2) | `isbn13` |
| 17985262 | CyberStorm | `isbn` |
| 17985262 | CyberStorm | `isbn13` |
| 17989312 | The Sisterhood | `isbn` |
| 17989312 | The Sisterhood | `isbn13` |
| 17989312 | The Sisterhood | `original_title` |
| 17999892 | The Atlantis Gene (The Origin Mystery, #1) | `isbn` |
| 17999892 | The Atlantis Gene (The Origin Mystery, #1) | `isbn13` |
| 18045473 | Last Train to Istanbul | `isbn` |
| 18045473 | Last Train to Istanbul | `isbn13` |
| 18053782 | Take a Chance (Rosemary Beach, #7; Chance, #1) | `isbn` |
| 18053782 | Take a Chance (Rosemary Beach, #7; Chance, #1) | `isbn13` |
| 18071296 | Willing Captive | `isbn` |
| 18071296 | Willing Captive | `isbn13` |
| 18076876 | Reaper's Legacy (Reapers MC, #2) | `isbn` |
| 18076876 | Reaper's Legacy (Reapers MC, #2) | `isbn13` |
| 18080889 | Worth the Fight (MMA Fighter, #1) | `isbn` |
| 18080889 | Worth the Fight (MMA Fighter, #1) | `isbn13` |
| 18080923 | The Traitor (Divergent, #0.4) | `original_title` |
| 18089551 | Tall, Tatted and Tempting (The Reed Brothers, #1) | `isbn` |
| 18089551 | Tall, Tatted and Tempting (The Reed Brothers, #1) | `isbn13` |
| 18089551 | Tall, Tatted and Tempting (The Reed Brothers, #1) | `original_title` |
| 18090061 | Big Girl Panties | `original_title` |
| 18104607 | Beautiful Oblivion (The Maddox Brothers, #1) | `isbn` |
| 18104607 | Beautiful Oblivion (The Maddox Brothers, #1) | `isbn13` |
| 18105011 | Sweet Home (Sweet Home, #1) | `isbn` |
| 18105011 | Sweet Home (Sweet Home, #1) | `isbn13` |
| 18105011 | Sweet Home (Sweet Home, #1) | `original_title` |
| 18108281 | The King (Black Dagger Brotherhood, #12) | `isbn` |
| 18108281 | The King (Black Dagger Brotherhood, #12) | `isbn13` |
| 18108795 | High Heat (Jack Reacher #17.5) | `isbn` |
| 18108795 | High Heat (Jack Reacher #17.5) | `isbn13` |
| 18108877 | Timebound (The Chronos Files, #1) | `isbn` |
| 18108877 | Timebound (The Chronos Files, #1) | `isbn13` |
| 18110808 | Fallen Crest Public (Fallen Crest High, #3) | `isbn` |
| 18110808 | Fallen Crest Public (Fallen Crest High, #3) | `isbn13` |
| 18110808 | Fallen Crest Public (Fallen Crest High, #3) | `original_title` |
| 18111281 | A Long Way Home | `isbn` |
| 18111281 | A Long Way Home | `isbn13` |
| 18114142 | A Fall of Marigolds | `original_title` |
| 18114142 | A Fall of Marigolds | `language_code` |
| 18115061 | Before Jamaica Lane (On Dublin Street, #3) | `isbn` |
| 18115061 | Before Jamaica Lane (On Dublin Street, #3) | `isbn13` |
| 18115061 | Before Jamaica Lane (On Dublin Street, #3) | `original_title` |
| 18129852 | Rival (Fall Away, #2) | `isbn` |
| 18129852 | Rival (Fall Away, #2) | `isbn13` |
| 18134249 | Ruin (Ruin, #1) | `isbn` |
| 18134249 | Ruin (Ruin, #1) | `isbn13` |
| 18134894 | Tears of Tess (Monsters in the Dark, #1) | `original_title` |
| 18138755 | Forever with You (Fixed, #3) | `isbn` |
| 18138755 | Forever with You (Fixed, #3) | `isbn13` |
| 18138755 | Forever with You (Fixed, #3) | `original_title` |
| 18138755 | Forever with You (Fixed, #3) | `language_code` |
| 18143977 | All the Light We Cannot See | `original_title` |
| 18144115 | All Fall Down | `original_title` |
| 18149927 | Beneath This Man (This Man, #2) | `isbn` |
| 18149927 | Beneath This Man (This Man, #2) | `isbn13` |
| 18163646 | Falling into Place | `isbn` |
| 18163646 | Falling into Place | `isbn13` |
| 18163646 | Falling into Place | `language_code` |
| 18191814 | A Blaze of Sun (A Shade of Vampire, #5) | `isbn` |
| 18191814 | A Blaze of Sun (A Shade of Vampire, #5) | `isbn13` |
| 18191814 | A Blaze of Sun (A Shade of Vampire, #5) | `original_title` |
| 18211536 | Rush Too Far (Rosemary Beach, #4; Too Far, #4) | `isbn` |
| 18211536 | Rush Too Far (Rosemary Beach, #4; Too Far, #4) | `isbn13` |
| 18221931 | Carter Reed (Carter Reed, #1) | `isbn` |
| 18221931 | Carter Reed (Carter Reed, #1) | `isbn13` |
| 18243828 | Jake Undone (Jake, #1) | `isbn` |
| 18243828 | Jake Undone (Jake, #1) | `isbn13` |
| 18243828 | Jake Undone (Jake, #1) | `original_title` |
| 18244799 | Hardwired (Hacker, #1) | `isbn` |
| 18244799 | Hardwired (Hacker, #1) | `isbn13` |
| 18246727 | Mud Vein | `isbn` |
| 18246727 | Mud Vein | `isbn13` |
| 18282800 | The Ladies' Room | `isbn` |
| 18282800 | The Ladies' Room | `isbn13` |
| 18282800 | The Ladies' Room | `original_title` |
| 18285151 | More Than This (More Than, #1) | `isbn` |
| 18285151 | More Than This (More Than, #1) | `isbn13` |
| 18285151 | More Than This (More Than, #1) | `original_title` |
| 18297707 | Tangled (Tangled, #1) | `isbn` |
| 18297707 | Tangled (Tangled, #1) | `isbn13` |
| 18301124 | Making Faces | `isbn` |
| 18301124 | Making Faces | `isbn13` |
| 18316089 | Lucky Us | `language_code` |
| 18323154 | المرحوم | `isbn` |
| 18323154 | المرحوم | `isbn13` |
| 18331807 | Vain (The Seven Deadly, #1) | `isbn` |
| 18331807 | Vain (The Seven Deadly, #1) | `isbn13` |
| 18331807 | Vain (The Seven Deadly, #1) | `original_title` |
| 18336965 | My Heart and Other Black Holes | `isbn` |
| 18336965 | My Heart and Other Black Holes | `isbn13` |
| 18337259 | A Game of Thrones: Comic Book, Issue 1 | `isbn` |
| 18337259 | A Game of Thrones: Comic Book, Issue 1 | `isbn13` |
| 18340482 | Until Trevor (Until, #2) | `isbn` |
| 18340482 | Until Trevor (Until, #2) | `isbn13` |
| 18340482 | Until Trevor (Until, #2) | `original_title` |
| 18341046 | Until November (Until, #1) | `isbn` |
| 18341046 | Until November (Until, #1) | `isbn13` |
| 18363068 | حبيبتي بكماء | `isbn` |
| 18363068 | حبيبتي بكماء | `isbn13` |
| 18363068 | حبيبتي بكماء | `original_title` |
| 18387597 | 2 ضباط | `isbn` |
| 18387597 | 2 ضباط | `isbn13` |
| 18405221 | Queen of Fire (Raven's Shadow, #3) | `isbn` |
| 18405221 | Queen of Fire (Raven's Shadow, #3) | `isbn13` |
| 18461986 | Deep (Stage Dive, #4) | `isbn` |
| 18461986 | Deep (Stage Dive, #4) | `isbn13` |
| 18465657 | The One & Only | `original_title` |
| 18468559 | Raw (RAW Family, #1) | `isbn` |
| 18468559 | Raw (RAW Family, #1) | `isbn13` |
| 18478222 | Twelve Years a Slave | `isbn` |
| 18478222 | Twelve Years a Slave | `isbn13` |
| 18500665 | End of Days (Penryn & the End of Days, #3) | `isbn` |
| 18500665 | End of Days (Penryn & the End of Days, #3) | `isbn13` |
| 18505836 | The Girl Who Came Home | `original_title` |
| 18607805 | Kindle Paperwhite User's Guide | `isbn` |
| 18607805 | Kindle Paperwhite User's Guide | `isbn13` |
| 18641982 | The Vacationers | `language_code` |
| 18655937 | Nash (Marked Men, #4) | `original_title` |
| 18655937 | Nash (Marked Men, #4) | `language_code` |
| 18656036 | The Fever | `language_code` |
| 18659623 | Through the Woods | `original_title` |
| 18667817 | Field of Prey (Lucas Davenport, #24) | `original_title` |
| 18667945 | #GIRLBOSS | `original_title` |
| 18668485 | The Initiate (Divergent, #0.2) | `isbn` |
| 18668485 | The Initiate (Divergent, #0.2) | `isbn13` |
| 18680106 | Hard as It Gets (Hard Ink, #1) | `isbn` |
| 18680106 | Hard as It Gets (Hard Ink, #1) | `isbn13` |
| 18711993 | فلتغفري | `isbn` |
| 18711993 | فلتغفري | `isbn13` |
| 18718848 | Mosquitoland | `isbn` |
| 18718848 | Mosquitoland | `isbn13` |
| 18739426 | The Bands of Mourning (Mistborn, #6) | `isbn` |
| 18739426 | The Bands of Mourning (Mistborn, #6) | `isbn13` |
| 18739485 | King (King, #1) | `original_title` |
| 18752959 | The Staff of Serapis (Percy Jackson & Kane Chronicles Crossover #2) | `original_title` |
| 18775203 | Rusty Nailed (Cocktail, #2) | `original_title` |
| 18781540 | Until Lilly (Until, #3) | `isbn` |
| 18781540 | Until Lilly (Until, #3) | `isbn13` |
| 18781540 | Until Lilly (Until, #3) | `original_title` |
| 18781543 | Until Nico (Until, #4) | `isbn` |
| 18781543 | Until Nico (Until, #4) | `isbn13` |
| 18781543 | Until Nico (Until, #4) | `original_title` |
| 18781543 | Until Nico (Until, #4) | `language_code` |
| 18799585 | Hidden (Bone Secrets. #1) | `isbn` |
| 18799585 | Hidden (Bone Secrets. #1) | `isbn13` |
| 18800655 | Terms of Enlistment (Frontlines #1) | `isbn` |
| 18800655 | Terms of Enlistment (Frontlines #1) | `isbn13` |
| 18806240 | Bone Gap | `isbn` |
| 18806240 | Bone Gap | `isbn13` |
| 18813530 | A Shadow of Light (A Shade of Vampire, #4) | `isbn` |
| 18813530 | A Shadow of Light (A Shade of Vampire, #4) | `isbn13` |
| 18813530 | A Shadow of Light (A Shade of Vampire, #4) | `original_title` |
| 18815695 | The Pecan Man | `isbn` |
| 18815695 | The Pecan Man | `isbn13` |
| 18815695 | The Pecan Man | `original_title` |
| 18815695 | The Pecan Man | `language_code` |
| 18819296 | Hidden | `isbn` |
| 18819296 | Hidden | `isbn13` |
| 18867685 | The Atlantis Plague (The Origin Mystery, #2) | `isbn` |
| 18867685 | The Atlantis Plague (The Origin Mystery, #2) | `isbn13` |
| 18892134 | The Son (Divergent, #0.3) | `isbn` |
| 18892134 | The Son (Divergent, #0.3) | `isbn13` |
| 18906484 | The Husband's Secret Free Preview | `isbn` |
| 18906484 | The Husband's Secret Free Preview | `isbn13` |
| 18906484 | The Husband's Secret Free Preview | `original_title` |
| 18943009 | Rock Bottom (Tristan & Danika, #2) | `isbn` |
| 18943009 | Rock Bottom (Tristan & Danika, #2) | `isbn13` |
| 18943009 | Rock Bottom (Tristan & Danika, #2) | `original_title` |
| 18982011 | The Line (Witching Savannah, #1) | `isbn` |
| 18982011 | The Line (Witching Savannah, #1) | `isbn13` |
| 19030845 | Batman: The Dark Knight Returns #1 | `isbn` |
| 19030845 | Batman: The Dark Knight Returns #1 | `isbn13` |
| 19095025 | Play (Stage Dive, #2) | `isbn` |
| 19095025 | Play (Stage Dive, #2) | `isbn13` |
| 19103097 | The Magician's Land (The Magicians, #3) | `isbn` |
| 19103097 | The Magician's Land (The Magicians, #3) | `isbn13` |
| 19286674 | Seventh Grave and No Body (Charley Davidson, #7) | `original_title` |
| 19351043 | Nimona | `isbn` |
| 19351043 | Nimona | `isbn13` |
| 19351490 | Grimm's Fairy Tales | `isbn` |
| 19351490 | Grimm's Fairy Tales | `isbn13` |
| 19549841 | Seraphina (Seraphina, #1) | `isbn` |
| 19549841 | Seraphina (Seraphina, #1) | `isbn13` |
| 19747756 | House | `isbn` |
| 19747756 | House | `isbn13` |
| 20299683 | Rat Queens, Vol. 1: Sass & Sorcery | `original_title` |
| 20316309 | في قلبي أنثى عبرية | `isbn` |
| 20316309 | في قلبي أنثى عبرية | `isbn13` |
| 20317106 | هيبتا | `isbn` |
| 20317106 | هيبتا | `isbn13` |
| 20329634 | Lines of Departure (Frontlines, #2) | `isbn` |
| 20329634 | Lines of Departure (Frontlines, #2) | `isbn13` |
| 20348781 | Loving Mr. Daniels | `isbn` |
| 20348781 | Loving Mr. Daniels | `isbn13` |
| 20423680 | The Last Town (Wayward Pines, #3) | `isbn` |
| 20423680 | The Last Town (Wayward Pines, #3) | `isbn13` |
| 20438825 | Vanished (Callahan & McLane #1) | `isbn` |
| 20438825 | Vanished (Callahan & McLane #1) | `isbn13` |
| 20438825 | Vanished (Callahan & McLane #1) | `original_title` |
| 20439328 | How to Be Both | `isbn` |
| 20439328 | How to Be Both | `isbn13` |
| 20509356 | Sand Omnibus (Sand, #1-5) | `isbn` |
| 20509356 | Sand Omnibus (Sand, #1-5) | `isbn13` |
| 20525628 | How to Build a Girl | `isbn` |
| 20525628 | How to Build a Girl | `isbn13` |
| 20559676 | Killing Sarai (In the Company of Killers, #1) | `isbn` |
| 20559676 | Killing Sarai (In the Company of Killers, #1) | `isbn13` |
| 20575434 | Rain Reign | `original_title` |
| 20603820 | The Will (Magdalene, #1) | `isbn` |
| 20603820 | The Will (Magdalene, #1) | `isbn13` |
| 20613920 | Under Locke | `isbn` |
| 20613920 | Under Locke | `isbn13` |
| 20620995 | Take Me with You | `isbn` |
| 20620995 | Take Me with You | `isbn13` |
| 20620995 | Take Me with You | `original_title` |
| 20639274 | Archer's Voice | `isbn` |
| 20639274 | Archer's Voice | `isbn13` |
| 20646604 | Night Owl (Night Owl, #1) | `isbn` |
| 20646604 | Night Owl (Night Owl, #1) | `isbn13` |
| 20646604 | Night Owl (Night Owl, #1) | `original_title` |
| 20685373 | Without You, There Is No Us: My Time with the Sons of North Korea's Elite | `language_code` |
| 20758175 | The Life We Bury | `language_code` |
| 20761374 | Reasonable Doubt: Volume 1 (Reasonable Doubt, #1) | `isbn` |
| 20761374 | Reasonable Doubt: Volume 1 (Reasonable Doubt, #1) | `isbn13` |
| 20797535 | A Better World (Brilliance Saga, #2) | `isbn` |
| 20797535 | A Better World (Brilliance Saga, #2) | `isbn13` |
| 20803953 | Bully (Fall Away, #1) | `isbn` |
| 20803953 | Bully (Fall Away, #1) | `isbn13` |
| 20803953 | Bully (Fall Away, #1) | `language_code` |
| 20803962 | Until You (Fall Away, #1.5) | `isbn` |
| 20803962 | Until You (Fall Away, #1.5) | `isbn13` |
| 20803962 | Until You (Fall Away, #1.5) | `language_code` |
| 20820995 | Deadline (Virgil Flowers, #8) | `original_title` |
| 20820995 | Deadline (Virgil Flowers, #8) | `language_code` |
| 20821376 | Belzhar | `original_title` |
| 20821376 | Belzhar | `language_code` |
| 20829994 | Percy Jackson's Greek Gods (A Percy Jackson and the Olympians Guide) | `isbn` |
| 20829994 | Percy Jackson's Greek Gods (A Percy Jackson and the Olympians Guide) | `isbn13` |
| 20871704 | Before I Go | `original_title` |
| 20871704 | Before I Go | `language_code` |
| 20874139 | I Am Livia | `isbn` |
| 20874139 | I Am Livia | `isbn13` |
| 20874139 | I Am Livia | `original_title` |
| 20886354 | Skin Deep (Legion, #2) | `isbn` |
| 20886354 | Skin Deep (Legion, #2) | `isbn13` |
| 20894857 | Sleep Tight | `isbn` |
| 20894857 | Sleep Tight | `isbn13` |
| 20912424 | The War that Saved My Life (The War That Saved My Life #1) | `original_title` |
| 20980373 | Reasonable Doubt: Volume 2 (Reasonable Doubt, #2) | `isbn` |
| 20980373 | Reasonable Doubt: Volume 2 (Reasonable Doubt, #2) | `isbn13` |
| 21104828 | The Lake House | `isbn` |
| 21104828 | The Lake House | `isbn13` |
| 21219083 | The One That Got Away | `isbn` |
| 21219083 | The One That Got Away | `isbn13` |
| 21394850 | أقوم قيلا | `isbn` |
| 21394850 | أقوم قيلا | `isbn13` |
| 21394850 | أقوم قيلا | `original_title` |
| 21411058 | Bad Romeo (Starcrossed, #1) | `isbn` |
| 21411058 | Bad Romeo (Starcrossed, #1) | `isbn13` |
| 21411887 | You Were Mine (Rosemary Beach, #9) | `original_title` |
| 21414439 | Truthwitch (The Witchlands, #1) | `isbn` |
| 21414439 | Truthwitch (The Witchlands, #1) | `isbn13` |
| 21418017 | The Space Between (Outlander, #7.5) | `isbn` |
| 21418017 | The Space Between (Outlander, #7.5) | `isbn13` |
| 21418017 | The Space Between (Outlander, #7.5) | `original_title` |
| 21420473 | The Fixed Trilogy (Fixed, #1-3) | `isbn` |
| 21420473 | The Fixed Trilogy (Fixed, #1-3) | `isbn13` |
| 21420473 | The Fixed Trilogy (Fixed, #1-3) | `original_title` |
| 21456940 | 1919 | `isbn` |
| 21456940 | 1919 | `isbn13` |
| 21473305 | Dominic (Slater Brothers, #1) | `isbn` |
| 21473305 | Dominic (Slater Brothers, #1) | `isbn13` |
| 21473305 | Dominic (Slater Brothers, #1) | `original_title` |
| 21483760 | Spell or High Water (Magic 2.0, #2) | `original_title` |
| 21518647 | Axel (Corps Security, #1) | `isbn` |
| 21518647 | Axel (Corps Security, #1) | `isbn13` |
| 21518647 | Axel (Corps Security, #1) | `language_code` |
| 21518679 | Cage (Corps Security, #2) | `isbn` |
| 21518679 | Cage (Corps Security, #2) | `isbn13` |
| 21518679 | Cage (Corps Security, #2) | `original_title` |
| 21530229 | The Job (Fox and O'Hare, #3) | `original_title` |
| 21531503 | What I Know for Sure | `original_title` |
| 21795430 | Promised (One Night, #1) | `original_title` |
| 21843117 | Scoring Wilder | `isbn` |
| 21843117 | Scoring Wilder | `isbn13` |
| 21849362 | The Shadows (Black Dagger Brotherhood, #13) | `isbn` |
| 21849362 | The Shadows (Black Dagger Brotherhood, #13) | `isbn13` |
| 21853628 | Every Fifteen Minutes | `original_title` |
| 21857294 | Reasonable Doubt: Volume 3 (Reasonable Doubt, #3) | `isbn` |
| 21857294 | Reasonable Doubt: Volume 3 (Reasonable Doubt, #3) | `isbn13` |
| 21873331 | If I Stay Collection (If I Stay, #1-2) | `original_title` |
| 21943246 | Black Ice | `original_title` |
| 21943246 | Black Ice | `language_code` |
| 21956060 | Monster in His Eyes (Monster in His Eyes, #1) | `isbn` |
| 21956060 | Monster in His Eyes (Monster in His Eyes, #1) | `isbn13` |
| 21956060 | Monster in His Eyes (Monster in His Eyes, #1) | `original_title` |
| 21981841 | Corrupt (Devil's Night, #1) | `original_title` |
| 22009741 | The Woman Who Stole My Life | `isbn` |
| 22009741 | The Woman Who Stole My Life | `isbn13` |
| 22020052 | It Ain't Me, Babe (Hades Hangmen, #1) | `isbn` |
| 22020052 | It Ain't Me, Babe (Hades Hangmen, #1) | `isbn13` |
| 22020052 | It Ain't Me, Babe (Hades Hangmen, #1) | `original_title` |
| 22027055 | One Lavender Ribbon | `isbn` |
| 22027055 | One Lavender Ribbon | `isbn13` |
| 22027459 | The Atlantis World (The Origin Mystery, #3) | `isbn` |
| 22027459 | The Atlantis World (The Origin Mystery, #3) | `isbn13` |
| 22131009 | Where There's Smoke | `isbn` |
| 22131009 | Where There's Smoke | `isbn13` |
| 22151696 | Lullabies | `original_title` |
| 22296542 | Addicted to You (Addicted, #1) | `isbn` |
| 22296542 | Addicted to You (Addicted, #1) | `isbn13` |
| 22299763 | Crooked Kingdom (Six of Crows, #2) | `isbn` |
| 22299763 | Crooked Kingdom (Six of Crows, #2) | `isbn13` |
| 22319275 | Yellow Crocus | `isbn` |
| 22319275 | Yellow Crocus | `isbn13` |
| 22319275 | Yellow Crocus | `original_title` |
| 22341276 | The Glass Magician (The Paper Magician Trilogy, #2) | `language_code` |
| 22381326 | Half a War (Shattered Sea, #3) | `isbn` |
| 22381326 | Half a War (Shattered Sea, #3) | `isbn13` |
| 22381892 | Killing Patton: The Strange Death of World War II's Most Audacious General | `isbn` |
| 22381892 | Killing Patton: The Strange Death of World War II's Most Audacious General | `isbn13` |
| 22428828 | Welcome to Shadowhunter Academy (Tales from the Shadowhunter Academy, #1) | `isbn` |
| 22428828 | Welcome to Shadowhunter Academy (Tales from the Shadowhunter Academy, #1) | `isbn13` |
| 22428828 | Welcome to Shadowhunter Academy (Tales from the Shadowhunter Academy, #1) | `original_title` |
| 22443261 | The Rithmatist (The Rithmatist, #1) | `isbn` |
| 22443261 | The Rithmatist (The Rithmatist, #1) | `isbn13` |
| 22457201 | Hardpressed (Hacker, #2) | `isbn` |
| 22457201 | Hardpressed (Hacker, #2) | `isbn13` |
| 22457201 | Hardpressed (Hacker, #2) | `original_title` |
| 22471294 | Black Lies | `isbn` |
| 22471294 | Black Lies | `isbn13` |
| 22474626 | Hard Limit (Hacker, #4) | `isbn` |
| 22474626 | Hard Limit (Hacker, #4) | `isbn13` |
| 22474626 | Hard Limit (Hacker, #4) | `language_code` |
| 22551743 | The Truth According to Us | `original_title` |
| 22554204 | Lumberjanes, Vol. 1: Beware the Kitten Holy | `original_title` |
| 22571612 | Crash & Burn (Tessa Leoni, #3) | `original_title` |
| 22600903 | Where I Belong (Alabama Summer, #1) | `isbn` |
| 22600903 | Where I Belong (Alabama Summer, #1) | `isbn13` |
| 22609310 | Confess | `original_title` |
| 22611920 | The Hook Up (Game On, #1) | `isbn` |
| 22611920 | The Hook Up (Game On, #1) | `isbn13` |
| 22669832 | Bright Side (Bright Side, #1) | `isbn` |
| 22669832 | Bright Side (Bright Side, #1) | `isbn13` |
| 22669832 | Bright Side (Bright Side, #1) | `original_title` |
| 22674493 | NYPD Red 3 (NYPD Red, #3) | `language_code` |
| 22693182 | Where They Found Her | `original_title` |
| 22693222 | The Residence: Inside the Private World of the White House | `language_code` |
| 22738563 | We Should All Be Feminists | `isbn` |
| 22738563 | We Should All Be Feminists | `isbn13` |
| 22744701 | My Sister's Grave (Tracy Crosswhite #1) | `isbn` |
| 22744701 | My Sister's Grave (Tracy Crosswhite #1) | `isbn13` |
| 22816087 | Seveneves | `isbn` |
| 22816087 | Seveneves | `isbn13` |
| 22836957 | The Revenant | `language_code` |
| 22840421 | My Lady Jane (The Lady Janies, #1) | `isbn` |
| 22840421 | My Lady Jane (The Lady Janies, #1) | `isbn13` |
| 22857396 | Sweet Addiction (Sweet Addiction, #1) | `isbn` |
| 22857396 | Sweet Addiction (Sweet Addiction, #1) | `isbn13` |
| 22886612 | Nemesis Games (The Expanse, #5) | `isbn` |
| 22886612 | Nemesis Games (The Expanse, #5) | `isbn13` |
| 22895264 | Wicked (A Wicked Saga, #1) | `isbn` |
| 22895264 | Wicked (A Wicked Saga, #1) | `isbn13` |
| 22914448 | The Dead Key | `isbn` |
| 22914448 | The Dead Key | `isbn13` |
| 22914448 | The Dead Key | `original_title` |
| 22915460 | The Glassblower | `isbn` |
| 22915460 | The Glassblower | `isbn13` |
| 22918050 | The Heir (The Selection, #4) | `isbn` |
| 22918050 | The Heir (The Selection, #4) | `isbn13` |
| 22923997 | Overruled (The Legal Briefs, #1) | `isbn` |
| 22923997 | Overruled (The Legal Briefs, #1) | `isbn13` |
| 22931009 | Kindle User's Guide | `isbn` |
| 22931009 | Kindle User's Guide | `isbn13` |
| 22931009 | Kindle User's Guide | `original_title` |
| 23012475 | The Knockoff | `original_title` |
| 23012475 | The Knockoff | `language_code` |
| 23014603 | Those Girls | `original_title` |
| 23014603 | Those Girls | `language_code` |
| 23122175 | The Friend Zone (Game On, #2) | `isbn` |
| 23122175 | The Friend Zone (Game On, #2) | `isbn13` |
| 23158207 | How Google Works | `isbn` |
| 23158207 | How Google Works | `isbn13` |
| 23207027 | Three Dark Crowns (Three Dark Crowns, #1) | `isbn` |
| 23207027 | Three Dark Crowns (Three Dark Crowns, #1) | `isbn13` |
| 23212667 | All the Missing Girls | `isbn` |
| 23212667 | All the Missing Girls | `isbn13` |
| 23245587 | Summer Secrets | `original_title` |
| 23245587 | Summer Secrets | `language_code` |
| 23245594 | Beach Town | `original_title` |
| 23245594 | Beach Town | `language_code` |
| 23252517 | The Law of Moses (The Law of Moses, #1) | `isbn` |
| 23252517 | The Law of Moses (The Law of Moses, #1) | `isbn13` |
| 23281640 | Gathering Prey (Lucas Davenport, #25) | `language_code` |
| 23287179 | Orphan Number Eight | `original_title` |
| 23355069 | Hero (Hero, #1) | `isbn` |
| 23355069 | Hero (Hero, #1) | `isbn13` |
| 23357188 | Bound by Honor (Born in Blood Mafia Chronicles, #1) | `isbn` |
| 23357188 | Bound by Honor (Born in Blood Mafia Chronicles, #1) | `isbn13` |
| 23398961 | The Sound of Glass | `original_title` |
| 23481669 | Maude | `isbn` |
| 23481669 | Maude | `isbn13` |
| 23481669 | Maude | `original_title` |
| 23481669 | Maude | `language_code` |
| 23485372 | The Master Magician (The Paper Magician Trilogy, #3) | `isbn` |
| 23485372 | The Master Magician (The Paper Magician Trilogy, #3) | `isbn13` |
| 23492288 | Hidden Bodies (You, #2) | `isbn` |
| 23492288 | Hidden Bodies (You, #2) | `isbn13` |
| 23492613 | Eight Hundred Grapes | `language_code` |
| 23492661 | Maybe in Another Life | `language_code` |
| 23492673 | Primates of Park Avenue | `original_title` |
| 23545800 | Kaleidoscope Hearts (Hearts, #1) | `isbn` |
| 23545800 | Kaleidoscope Hearts (Hearts, #1) | `isbn13` |
| 23566909 | The Marvels | `original_title` |
| 23587984 | Maybe Not (Maybe, #1.5) | `isbn` |
| 23587984 | Maybe Not (Maybe, #1.5) | `isbn13` |
| 23602562 | Our Souls at Night | `language_code` |
| 23647129 | For the Love: Fighting for Grace in a World of Impossible Standards | `language_code` |
| 23675858 | Departure | `isbn` |
| 23675858 | Departure | `isbn13` |
| 23692271 | Sapiens: A Brief History of Humankind | `isbn` |
| 23692271 | Sapiens: A Brief History of Humankind | `isbn13` |
| 23714532 | Beautiful Sacrifice (The Maddox Brothers, #3) | `isbn` |
| 23714532 | Beautiful Sacrifice (The Maddox Brothers, #3) | `isbn13` |
| 23714544 | Beautiful Burn (The Maddox Brothers, #4) | `isbn` |
| 23714544 | Beautiful Burn (The Maddox Brothers, #4) | `isbn13` |
| 23743603 | Miramont's Ghost | `isbn` |
| 23743603 | Miramont's Ghost | `isbn13` |
| 23743603 | Miramont's Ghost | `original_title` |
| 23745132 | Wreckage | `isbn` |
| 23745132 | Wreckage | `isbn13` |
| 23745132 | Wreckage | `original_title` |
| 23745189 | The Mermaid's Sister | `isbn` |
| 23745189 | The Mermaid's Sister | `isbn13` |
| 23844390 | The Pact | `isbn` |
| 23844390 | The Pact | `isbn13` |
| 23844390 | The Pact | `original_title` |
| 24044596 | Kulti | `isbn` |
| 24044596 | Kulti | `isbn13` |
| 24044596 | Kulti | `original_title` |
| 24044596 | Kulti | `language_code` |
| 24228353 | Trail of Broken Wings | `isbn` |
| 24228353 | Trail of Broken Wings | `isbn13` |
| 24378015 | Never Never (Never Never, #1) | `isbn` |
| 24378015 | Never Never (Never Never, #1) | `isbn13` |
| 24422492 | Never Never: Part Two (Never Never, #2) | `original_title` |
| 24429934 | The Einstein Prophecy | `isbn` |
| 24429934 | The Einstein Prophecy | `isbn13` |
| 24429934 | The Einstein Prophecy | `original_title` |
| 24445517 | Maybe Someday (Maybe, #1) | `isbn` |
| 24445517 | Maybe Someday (Maybe, #1) | `isbn13` |
| 24473465 | The English Spy (Gabriel Allon, #15) | `isbn` |
| 24473465 | The English Spy (Gabriel Allon, #15) | `isbn13` |
| 24473763 | Radiance (Wraith Kings, #1) | `isbn` |
| 24473763 | Radiance (Wraith Kings, #1) | `isbn13` |
| 24480276 | The Versions of Us | `isbn` |
| 24480276 | The Versions of Us | `isbn13` |
| 24488476 | The Fate of Ten (Lorien Legacies, #6) | `isbn` |
| 24488476 | The Fate of Ten (Lorien Legacies, #6) | `isbn13` |
| 24488476 | The Fate of Ten (Lorien Legacies, #6) | `original_title` |
| 24504274 | Pucked (Pucked, #1) | `original_title` |
| 24631990 | Silent Scream (D.I. Kim Stone, #1) | `isbn` |
| 24631990 | Silent Scream (D.I. Kim Stone, #1) | `isbn13` |
| 24709327 | Scion of Ikshvaku (RamChandra, #1) | `original_title` |
| 24819476 | Winter Stroll (Winter #2) | `language_code` |
| 24859245 | Stranger Child (DCI Tom Douglas, #4) | `isbn` |
| 24859245 | Stranger Child (DCI Tom Douglas, #4) | `isbn13` |
| 24859245 | Stranger Child (DCI Tom Douglas, #4) | `original_title` |
| 24902492 | Ruby | `language_code` |
| 24903031 | Blood Kiss (Black Dagger Legacy, #1) | `original_title` |
| 24903919 | Depraved Heart (Kay Scarpetta, #23) | `language_code` |
| 24920901 | The Deal (Off-Campus, #1) | `isbn` |
| 24920901 | The Deal (Off-Campus, #1) | `isbn13` |
| 24937499 | Her Final Breath (Tracy Crosswhite, #2) | `isbn` |
| 24937499 | Her Final Breath (Tracy Crosswhite, #2) | `isbn13` |
| 24937499 | Her Final Breath (Tracy Crosswhite, #2) | `original_title` |
| 24950845 | Tricky Twenty-Two (Stephanie Plum, #22) | `original_title` |
| 24961498 | The Midwife's Revolt (The Midwife Series, #1) | `isbn` |
| 24961498 | The Midwife's Revolt (The Midwife Series, #1) | `isbn13` |
| 24961498 | The Midwife's Revolt (The Midwife Series, #1) | `original_title` |
| 24961531 | The Color of Secrets | `isbn` |
| 24961531 | The Color of Secrets | `isbn13` |
| 24961531 | The Color of Secrets | `original_title` |
| 24961531 | The Color of Secrets | `language_code` |
| 25005214 | Queen Song (Red Queen, #0.1) | `language_code` |
| 25041504 | After You (Me Before You, #2) | `isbn` |
| 25041504 | After You (Me Before You, #2) | `isbn13` |
| 25056528 | Sincerely, Carter (Sincerely Carter, #1) | `isbn` |
| 25056528 | Sincerely, Carter (Sincerely Carter, #1) | `isbn13` |
| 25056528 | Sincerely, Carter (Sincerely Carter, #1) | `original_title` |
| 25056528 | Sincerely, Carter (Sincerely Carter, #1) | `language_code` |
| 25065522 | Wildflower | `original_title` |
| 25066591 | Cross Justice (Alex Cross, #23) | `language_code` |
| 25104491 | The Prettiest One | `isbn` |
| 25104491 | The Prettiest One | `isbn13` |
| 25104491 | The Prettiest One | `original_title` |
| 25153134 | Follow You Home | `isbn` |
| 25153134 | Follow You Home | `isbn13` |
| 25228579 | The Perfect Son | `isbn` |
| 25228579 | The Perfect Son | `isbn13` |
| 25316313 | A Dark Lure | `isbn` |
| 25316313 | A Dark Lure | `isbn13` |
| 25316313 | A Dark Lure | `original_title` |
| 25387351 | Rogue Lawyer | `original_title` |
| 25387351 | Rogue Lawyer | `language_code` |
| 25422234 | Notorious RBG: The Life and Times of Ruth Bader Ginsburg | `original_title` |
| 25430584 | The Guest Room | `original_title` |
| 25451852 | Dawn of Wonder (The Wakening, #1) | `isbn` |
| 25451852 | Dawn of Wonder (The Wakening, #1) | `isbn13` |
| 25454883 | Never Never: Part Three (Never Never, #3) | `isbn` |
| 25454883 | Never Never: Part Three (Never Never, #3) | `isbn13` |
| 25454883 | Never Never: Part Three (Never Never, #3) | `original_title` |
| 25507925 | Binge | `isbn` |
| 25507925 | Binge | `isbn13` |
| 25507925 | Binge | `language_code` |
| 25558608 | A Torch Against the Night (An Ember in the Ashes, #2) | `isbn` |
| 25558608 | A Torch Against the Night (An Ember in the Ashes, #2) | `isbn13` |
| 25564446 | The Air He Breathes (Elements, #1) | `isbn` |
| 25564446 | The Air He Breathes (Elements, #1) | `isbn13` |
| 25564446 | The Air He Breathes (Elements, #1) | `language_code` |
| 25614984 | Spark Joy: An Illustrated Master Class on the Art of Organizing and Tidying Up | `original_title` |
| 25624089 | Killing Reagan: The Violent Assault That Changed a Presidency | `isbn` |
| 25624089 | Killing Reagan: The Violent Assault That Changed a Presidency | `isbn13` |
| 25690958 | Year of Yes: How to Dance It Out, Stand In the Sun and Be Your Own Person | `isbn` |
| 25690958 | Year of Yes: How to Dance It Out, Stand In the Sun and Be Your Own Person | `isbn13` |
| 25690958 | Year of Yes: How to Dance It Out, Stand In the Sun and Be Your Own Person | `original_title` |
| 25693079 | Crooked Little Lies | `isbn` |
| 25693079 | Crooked Little Lies | `isbn13` |
| 25693079 | Crooked Little Lies | `original_title` |
| 25693079 | Crooked Little Lies | `language_code` |
| 25711641 | Tyrant (King, #2) | `isbn` |
| 25711641 | Tyrant (King, #2) | `isbn13` |
| 25711641 | Tyrant (King, #2) | `original_title` |
| 25773504 | Most Wanted | `original_title` |
| 25801299 | After Anna | `isbn` |
| 25801299 | After Anna | `isbn13` |
| 25802884 | Hollywood Dirt (Hollywood Dirt, #1) | `isbn` |
| 25802884 | Hollywood Dirt (Hollywood Dirt, #1) | `isbn13` |
| 25817531 | What She Knew | `language_code` |
| 25828204 | F*ck Love | `isbn` |
| 25828204 | F*ck Love | `isbn13` |
| 25828204 | F*ck Love | `original_title` |
| 25828204 | F*ck Love | `language_code` |
| 25837338 | The Girl from Krakow | `isbn` |
| 25837338 | The Girl from Krakow | `isbn13` |
| 25837341 | The Good Neighbor | `isbn` |
| 25837341 | The Good Neighbor | `isbn13` |
| 25837341 | The Good Neighbor | `original_title` |
| 25866725 | Broken Grace | `isbn` |
| 25866725 | Broken Grace | `isbn13` |
| 25866725 | Broken Grace | `original_title` |
| 25883848 | The Hating Game | `isbn` |
| 25883848 | The Hating Game | `isbn13` |
| 25899336 | When Breath Becomes Air | `isbn` |
| 25899336 | When Breath Becomes Air | `isbn13` |
| 25912358 | A Thousand Boy Kisses | `isbn` |
| 25912358 | A Thousand Boy Kisses | `isbn13` |
| 26061591 | Extreme Prey (Lucas Davenport, #26) | `isbn` |
| 26061591 | Extreme Prey (Lucas Davenport, #26) | `isbn13` |
| 26061591 | Extreme Prey (Lucas Davenport, #26) | `original_title` |
| 26114516 | The Weekenders | `original_title` |
| 26114516 | The Weekenders | `language_code` |
| 26158341 | The Girl With No Past | `isbn` |
| 26158341 | The Girl With No Past | `isbn13` |
| 26192467 | First Comes Love | `original_title` |
| 26214866 | In the Clearing (Tracy Crosswhite, #3) | `isbn` |
| 26214866 | In the Clearing (Tracy Crosswhite, #3) | `isbn13` |
| 26214866 | In the Clearing (Tracy Crosswhite, #3) | `original_title` |
| 26224667 | Wrong (Wrong, #1) | `isbn` |
| 26224667 | Wrong (Wrong, #1) | `isbn13` |
| 26583370 | Life and Other Near-Death Experiences | `isbn` |
| 26583370 | Life and Other Near-Death Experiences | `isbn13` |
| 26583370 | Life and Other Near-Death Experiences | `original_title` |
| 27152124 | Dirty English (English, #1) | `isbn` |
| 27152124 | Dirty English (English, #1) | `isbn13` |
| 27161845 | Here's to Us | `original_title` |
| 27207654 | Blood Defense (Samantha Brinkman, #1) | `isbn` |
| 27207654 | Blood Defense (Samantha Brinkman, #1) | `isbn13` |
| 27207654 | Blood Defense (Samantha Brinkman, #1) | `original_title` |
| 27209486 | Modern Lovers | `language_code` |
| 27239265 | The Short Drop (Gibson Vaughn, #1) | `isbn` |
| 27239265 | The Short Drop (Gibson Vaughn, #1) | `isbn13` |
| 27239265 | The Short Drop (Gibson Vaughn, #1) | `original_title` |
| 27252717 | The Score (Off-Campus, #3) | `isbn` |
| 27252717 | The Score (Off-Campus, #3) | `isbn13` |
| 27362503 | It Ends with Us | `isbn` |
| 27362503 | It Ends with Us | `isbn13` |
| 27401883 | When I'm Gone | `isbn` |
| 27401883 | When I'm Gone | `isbn13` |
| 27406436 | The Baller: A Down and Dirty Football Novel | `isbn` |
| 27406436 | The Baller: A Down and Dirty Football Novel | `isbn13` |
| 27419654 | The Last Girl (The Dominion Trilogy, #1) | `isbn` |
| 27419654 | The Last Girl (The Dominion Trilogy, #1) | `isbn13` |
| 27419654 | The Last Girl (The Dominion Trilogy, #1) | `original_title` |
| 27423283 | The Moonlit Garden | `isbn` |
| 27423283 | The Moonlit Garden | `isbn13` |
| 27810589 | A Death in Sweden | `isbn` |
| 27810589 | A Death in Sweden | `isbn13` |
| 27810589 | A Death in Sweden | `original_title` |
| 27810589 | A Death in Sweden | `language_code` |
| 27821486 | Don't You Cry | `language_code` |
| 27824826 | The Dry (Aaron Falk, #1) | `isbn` |
| 27824826 | The Dry (Aaron Falk, #1) | `isbn13` |
| 27864391 | The Danish Girl | `isbn` |
| 27864391 | The Danish Girl | `isbn13` |
| 27868677 | The House by the Lake | `isbn` |
| 27868677 | The House by the Lake | `isbn13` |
| 27868677 | The House by the Lake | `original_title` |
| 28233082 | The Girl In The Ice (Detective Erika Foster, #1) | `isbn` |
| 28233082 | The Girl In The Ice (Detective Erika Foster, #1) | `isbn13` |
| 28240855 | The Girl You Lost | `isbn` |
| 28240855 | The Girl You Lost | `isbn13` |
| 28240855 | The Girl You Lost | `original_title` |
| 28262024 | The Goal (Off-Campus, #4) | `original_title` |
| 28449270 | Today Will Be Different | `original_title` |
| 28449270 | Today Will Be Different | `language_code` |
| 28477789 | Stuck-Up Suit | `isbn` |
| 28477789 | Stuck-Up Suit | `isbn13` |
| 28587957 | Small Great Things | `original_title` |
| 28678119 | Paper Princess (The Royals, #1) | `isbn` |
| 28678119 | Paper Princess (The Royals, #1) | `isbn13` |
| 28698036 | Secret History (Mistborn, #3.5) | `isbn` |
| 28698036 | Secret History (Mistborn, #3.5) | `isbn13` |
| 28802599 | The Light of the Fireflies | `isbn` |
| 28802599 | The Light of the Fireflies | `isbn13` |
| 28802599 | The Light of the Fireflies | `original_title` |
| 28959148 | We're All Damaged | `isbn` |
| 28959148 | We're All Damaged | `isbn13` |
| 28959148 | We're All Damaged | `original_title` |
| 29103028 | The Queen's Poisoner (Kingfountain, #1) | `isbn` |
| 29103028 | The Queen's Poisoner (Kingfountain, #1) | `isbn13` |
| 29104680 | Punk 57 | `isbn` |
| 29104680 | Punk 57 | `isbn13` |
| 29104680 | Punk 57 | `language_code` |
| 29354916 | The Whistler | `isbn` |
| 29354916 | The Whistler | `isbn13` |
| 29367958 | The Wall of Winnipeg and Me | `isbn` |
| 29367958 | The Wall of Winnipeg and Me | `isbn13` |
| 29430013 | The Trespasser (Dublin Murder Squad #6) | `original_title` |
| 29430788 | Faithful | `original_title` |
| 29610595 | Too Late | `isbn` |
| 29610595 | Too Late | `isbn13` |
| 29610595 | Too Late | `original_title` |
| 29632984 | The Things We Wish Were True | `isbn` |
| 29632984 | The Things We Wish Were True | `isbn13` |
| 29632984 | The Things We Wish Were True | `original_title` |
| 29639736 | Everything We Keep (Everything We Keep, #1) | `isbn` |
| 29639736 | Everything We Keep (Everything We Keep, #1) | `isbn13` |
| 29780253 | Born a Crime: Stories From a South African Childhood | `original_title` |
| 29925715 | The Sister | `isbn` |
| 29925715 | The Sister | `isbn13` |
| 29981261 | The Butterfly Garden (The Collector #1) | `isbn` |
| 29981261 | The Butterfly Garden (The Collector #1) | `isbn13` |
| 29991719 | Royally Screwed (Royally, #1) | `isbn` |
| 29991719 | Royally Screwed (Royally, #1) | `isbn13` |
| 30002998 | Two By Two | `isbn` |
| 30002998 | Two By Two | `isbn13` |
| 30065028 | Fantastic Beasts and Where to Find Them: The Original Screenplay | `isbn` |
| 30065028 | Fantastic Beasts and Where to Find Them: The Original Screenplay | `isbn13` |
| 30253700 | Anti-Stepbrother | `isbn` |
| 30253700 | Anti-Stepbrother | `isbn13` |
| 30253700 | Anti-Stepbrother | `original_title` |
| 30314465 | No Man's Land (John Puller, #4) | `isbn` |
| 30314465 | No Man's Land (John Puller, #4) | `isbn13` |
| 30364931 | Neighbor Dearest | `isbn` |
| 30364931 | Neighbor Dearest | `isbn13` |
| 30364931 | Neighbor Dearest | `original_title` |
| 30364931 | Neighbor Dearest | `language_code` |
| 30831912 | Norse Mythology | `isbn` |
| 30831912 | Norse Mythology | `isbn13` |
| 30839185 | Vicious (Sinners of Saint, #1) | `isbn` |
| 30839185 | Vicious (Sinners of Saint, #1) | `isbn13` |
| 31140847 | Bossman | `isbn` |
| 31140847 | Bossman | `isbn13` |
| 31140847 | Bossman | `original_title` |
| 31176886 | The Chemist | `isbn` |
| 31176886 | The Chemist | `isbn13` |
| 31194270 | Evelyn, After | `isbn` |
| 31194270 | Evelyn, After | `isbn13` |
| 31538647 | Hogwarts: An Incomplete and Unreliable Guide (Pottermore Presents, #3) | `isbn` |
| 31538647 | Hogwarts: An Incomplete and Unreliable Guide (Pottermore Presents, #3) | `isbn13` |
| 32848471 | Egomaniac | `original_title` |
| 32848471 | Egomaniac | `language_code` |
| 33288638 | Wait for It | `isbn` |
| 33288638 | Wait for It | `isbn13` |
| 90010001 | The Lantern Keeper's Daughter | `image_url` |
| 90010001 | The Lantern Keeper's Daughter | `small_image_url` |
| 90010002 | Salt and Ember | `image_url` |
| 90010002 | Salt and Ember | `small_image_url` |
| 90010003 | A Field Guide to Quiet Places | `image_url` |
| 90010003 | A Field Guide to Quiet Places | `small_image_url` |
| 90010004 | Winter Orchard | `image_url` |
| 90010004 | Winter Orchard | `small_image_url` |
| 90010005 | The Cartographer's Error | `image_url` |
| 90010005 | The Cartographer's Error | `small_image_url` |
| 90010006 | Notes from the Night Ferry | `isbn` |
| 90010006 | Notes from the Night Ferry | `image_url` |
| 90010006 | Notes from the Night Ferry | `small_image_url` |
| 90010007 | Small Hours | `isbn` |
| 90010007 | Small Hours | `isbn13` |
| 90010007 | Small Hours | `image_url` |
| 90010007 | Small Hours | `small_image_url` |
| 90010008 | The Glass Aviary | `isbn` |
| 90010008 | The Glass Aviary | `isbn13` |
| 90010008 | The Glass Aviary | `image_url` |
| 90010008 | The Glass Aviary | `small_image_url` |
| 90010009 | Borrowed Light | `isbn` |
| 90010009 | Borrowed Light | `isbn13` |
| 90010009 | Borrowed Light | `image_url` |
| 90010009 | Borrowed Light | `small_image_url` |
| 90010010 | Untitled Manuscript | `isbn` |
| 90010010 | Untitled Manuscript | `isbn13` |
| 90010010 | Untitled Manuscript | `image_url` |
| 90010010 | Untitled Manuscript | `small_image_url` |
| 90010011 | Tides of Marrow Bay | `image_url` |
| 90010011 | Tides of Marrow Bay | `small_image_url` |
| 90010012 | The Long Walk Home | `image_url` |
| 90010012 | The Long Walk Home | `small_image_url` |
| 90010014 | An Atlas of Small Kindnesses | `image_url` |
| 90010014 | An Atlas of Small Kindnesses | `small_image_url` |

</details>

## Open questions for the group

None of these is decided by rules.md, so neither build is wrong. These are choices to agree on if the databases should match:

1. Store a missing value as no value (NULL) or as blank text?
2. Trim a value that is only spaces?
3. Store an ISBN-10's `X` check character uppercase or as written?
4. File `no-usable-isbn` under `isbn` or `isbn13`?
5. One shared list of warning names (e.g. `lost-precision` or `float-precision-lost`, `bad-length` or `wrong-length`, `bad-characters` or `invalid-characters`).
6. A 9-digit `isbn` whose zero-padded form fails the check digit: a bad check digit, or the wrong length?
