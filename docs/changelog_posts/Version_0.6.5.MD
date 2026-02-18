# Update 0.6.5 (Fortnite Update) {.blog_entry_title}

Changes in Version 0.6.5
{.blog_intro}

## New Endpoints {.blog_title}

2 new endpoints have been added:  **"Fortnite Cosmetics" and "Fortnite Items"**

- Items: `http://<your-ip>/api/fortnite/items/<ID>` (1 or 2)
- Cosmetics: `http://<your-ip>/api/fortnite/cosmetics/<ID>` (1 to 33)

_These endpoints don't support list view or the use of filters; this will be added in a future update._

## Changes in the database {.blog_title}

New tables in the database:

- Fortnite Cosmetic Rarities: Contains the rarities used by the cosmetics.
- Fortnite Cosmetic Types: Contains the types of the cosmetics.

(These two tables exist to be used in the future to filter the cosmetics)

- Fortnite Cosmetics: Contains the cosmetics.
- Fortnite Items: Contains the items that you can use in battle.

(These tables are used by the endpoints)

## Fixes {.blog_title}

The changelog for version 0.6 wasn't on the index; this error has now been corrected.