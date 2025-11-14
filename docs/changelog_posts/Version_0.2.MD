# Update 0.2 (E Update) {.blog_entry_title}

Changes in version 0.2
{.blog_intro}
## New Endpoint {.blog_title}
- Added the Endpoint [All Characters with alteregos](/api/characterswithalterego) Retruns all the characters that have a alterego.

## Changes in Endpoints {.blog_title}

- The Chinpokomon Endpoint has been renamed: "/chinpokomon/" to "/chinpokomons/"
- The Chinpokomon endpoint now can send metadata: [link](/api/chinpokomons/1?metadata=true)

## Items added to the Database [Database Update]: {.blog_title}

### [NEW EPISODE] {.blog_subtitle}

- [The Episode 329 (Sora not sorry)](/api/episodes/329) has been added.

- The Characters [Bluey Heeler](/api/characters/695) and [Droopy Dog (Cartoon)](/api/characters/696) has been added.

### [CHARACTERS] {.blog_subtitle}
- The Characters of the TV Show that their name starts with E has been added: [ID: 658](/api/characters/658) -> [ID: 694](/api/characters/694)

### [FAMILIES] {.blog_subtitle}
- Added two new families: [Family 71 (The Hollis)](/api/families/71) and [Family 72 (Japanese Imperial Family)](/api/families/72)

### [ALTEREGOS] {.blog_subtitle}

Now ["Dougie O'Connell"](/api/characters/622) has his alteregos in the database: ([Link](/api/characters/622/alteregos))

### Fixed this missing files: {.blog_subtitle}

- [Family 62 (Joline / Chantal Family) Image](/img/families/Joline_Family.png)

- [Family 63 (The Browns) Image](/img/families/The_Browns.png)

- [Family 64 (Runs with promise) Image](/img/families/Runs_With_Promis_Family.png)

- [Family 65 (Christine / Dennis Family) Image](/img/families/Christine_Dennis_Family.png)

- [Family 66 (Christophe Family) Image](/img/families/Christophe_Family.png)

- [Family 67 (The McCains) Image](/img/families/The_McCains.png)

- [Family 68 (The Fitzsimmons) Image](/img/families/The_Fitzsimmons.png)

- [Family 69 (The Solokovs) Image](/img/families/The_Solokovs.png)

- [Family 70 (The Weatherhead foster family) Image](/img/families/The_Weatherheads.png)

### Fixes of wrong data: {.blog_subtitle}

- The Characters of [The Stevens](/api/families/36) have a incorrect ID in the family ID, this is now fixed.
- [The Burch Family](/api/families/10) second image name has been fixed.
- The image's name of [Chinpokomon 2](/api/chinpokomons/2) and [Chinpokomon 26](/api/chinpokomons/26) has been fixed

### Fixes in responses: {.blog_subtitle}

- [The Chinpokomon Endpoint](/api/chinpokomons/1) Now retruns the correct status code in responses 404 and 500.
- [The Key of the Game Endpoint that returns the number of games](/api/games/1/?metadata=true) has been changed to "total_games_in_database"

## Internal Changes: {.blog_title}

- Now All Endpoints have thier data tests and response tests

