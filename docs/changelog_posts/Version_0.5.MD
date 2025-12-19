# Update 0.5 (Christmas Update) {.blog_entry_title}

Changes in Version 0.5
{.blog_intro}

## Changes in project structure {.blog_title}

The raw queries in the source code of the API have been refactored to ORM queries. This change will make it easier to update the database responses in the future, obfuscate the database structure, and make heavy queries much faster.

## New Endpoints: {.blog_title}

Parity changes in these endpoints: Families, Groups, Chinpokomon, Games, Albums, and Episodes. These endpoints now allow searching for elements by name:

Example: `http://localhost:8000/api/groups?search=Kids&limit=5` returns the first five groups that contain "kids". This is not case-sensitive.

Now all the elements have an endpoint that returns all the elements of the table:

Example: `http://localhost:8000/api/albums` returns all the albums.

Example: `http://localhost:8000/api/characters?limit=50` returns the first 50 characters.

`At the moment, the songs endpoint does not have these options because the albums contain all the songs, but this may be implemented in a future update.`

**THIS UPDATE SIGNIFICANTLY CHANGES THE STRUCTURE OF THE API. IT'S POSSIBLE THAT I'VE FORGOTTEN SOMETHING. IF THERE ARE ANY MISSING FEATURES, THEY WILL BE ADDED IN A FUTURE UPDATE.**

## Database Updates {.blog_title}

### Added Episode 331 (End of Season 28) {.blog_subtitle}

- Added episode 331 to the API [here](/api/episodes/331) `/api/episodes/331`

- Added Character 797 ([The Antichrist](/api/characters/797)) `/api/characters/797`

__*Project Director's note about this update: In the wikis I use for this API, the Satan baby (The Antichrist) is not counted as a character. It is the first case in the show where a character dies before being born (excluding the N**i fetus from Stick of Truth). I have investigated this, and in the USA, a dead fetus is considered a stillbirth at the twentieth week, but it is not a legal person. Nevertheless, this status of stillbirth made me feel like I should include it in the API, with the particularity that its age is 0. I was thinking about setting the age to -1, but this could crash some software if there is a negative number in the age field.*__

### Added Characters whose names start with H and I {.blog_subtitle}

All the characters from the TV show whose names start with H or I have been added:

- Characters [798](/api/characters/798) `/api/characters/798` to Character [868](/api/characters/868) `/api/characters/868`

- Families [79](/api/families/79) `/api/families/79` to Family [81](/api/families/81) `/api/families/81`

## Change in Endpoints. {.blog_title}

Now the characters' response contains a list of the groups that include them. If a character has no groups, it returns `None`.