# Update 0.2 (E Update) {.blog_entry_title}

Changes in Version 0.2
{.blog_intro}

## New endpoint {.blog_title}

- Added the endpoint [All Characters with Alter Egos](/api/characterswithalterego). Returns all characters that have an alter ego.

## Changes in endpoints {.blog_title}

- The Chinpokomon endpoint has been renamed from "/chinpokomon/" to "/chinpokomons/".

- The Chinpokomon endpoint can now return metadata: [link](/api/chinpokomons/1?metadata=true).

## Items added to the database [Database Update]: {.blog_title}

### New episode {.blog_subtitle}

- [Episode 329 ("Sora Not Sorry")](/api/episodes/329) has been added.

- The characters [Bluey Heeler](/api/characters/695) and [Droopy Dog (Cartoon)](/api/characters/696) have been added.

### Characters {.blog_subtitle}

- Characters from the TV show whose names start with "E" have been added: [ID: 658](/api/characters/658) -> [ID: 694](/api/characters/694).

### Families {.blog_subtitle}

- Added two new families: [Family 71 (The Hollis)](/api/families/71) and [Family 72 (Japanese Imperial Family)](/api/families/72).

### Alter egos {.blog_subtitle}

- [Dougie O'Connell](/api/characters/622) now has his alter egos in the database: ([Link](/api/characters/622/alteregos)).

### Fixed missing files {.blog_subtitle}

- Fixed missing image for [Family 62 (Joline / Chantal Family)](/img/families/Joline_Family.png).
- Fixed missing image for [Family 63 (The Browns)](/img/families/The_Browns.png).
- Fixed missing image for [Family 64 (Runs With Promise)](/img/families/Runs_With_Promis_Family.png).
- Fixed missing image for [Family 65 (Christine / Dennis Family)](/img/families/Christine_Dennis_Family.png).
- Fixed missing image for [Family 66 (Christophe Family)](/img/families/Christophe_Family.png).
- Fixed missing image for [Family 67 (The McCains)](/img/families/The_McCains.png).
- Fixed missing image for [Family 68 (The Fitzsimmons)](/img/families/The_Fitzsimmons.png).
- Fixed missing image for [Family 69 (The Solokovs)](/img/families/The_Solokovs.png).
- Fixed missing image for [Family 70 (The Weatherhead foster family)](/img/families/The_Weatherheads.png).

### Fixes for incorrect data {.blog_subtitle}

- Characters of [The Stevens](/api/families/36) had an incorrect family ID; this is now fixed.
- The second image name for [The Burch Family](/api/families/10) has been fixed.
- The image names for [Chinpokomon 2](/api/chinpokomons/2) and [Chinpokomon 26](/api/chinpokomons/26) have been fixed.

### Response fixes {.blog_subtitle}

- The Chinpokomon endpoint (/api/chinpokomons/1) now returns the correct status codes for 404 and 500 responses.
- The key in the Games endpoint that returns the number of games (/api/games/1/?metadata=true) has been renamed to "total_games_in_database".

## Website changes {.blog_title}

- Created [The Changelog](/changelog).
- Added a button in the desktop index to go to the current changelog.

## Internal changes {.blog_title}

- All endpoints now have their data tests and response tests.

