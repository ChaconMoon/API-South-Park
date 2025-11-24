# Update 0.3 (The Force of chance) {.blog_entry_title}

Changes in Version 0.3
{.blog_intro}

## New Endpoints (Random Endpoints) {.blog_title}

Now all the endpoints of the API have a function that returns a random item from the database:

- [Characters]

  -> [Random Character](/api/characters/random) `/api/characters/random`

  -> [Random Character (Excluding Famous Guests)](/api/characters/random?exclude_famous_guests=true) `/api/characters/random?exclude_famous_guests=true`

- [Families]

  -> [Random Family](/api/families/random) `/api/families/random`

- [Alter Egos]

  -> [Random Alter Ego](/api/alteregos/random) `/api/alteregos/random`

  -> [Random Alter Ego (Specific Character if exists) e.g., Stan](/api/alteregos/random?character=4)  
  `/api/alteregos/random?character=ID`

  To see all available characters, click [here](/api/characterswithalterego).

- [Specials]

  -> [Random Special](/api/specials/random) `/api/specials/random`

- [Episodes]

  -> [Random Episode](/api/episodes/random) `/api/episodes/random`

  -> [Random Episode (Excluding Paramount Plus Exclusives)](/api/episodes/random?exclude_paramount_plus=true) `/api/episodes/random?exclude_paramount_plus=true`

  -> [Random Episode (Excluding Censored)](/api/episodes/random?exclude_censored=true) `/api/episodes/random?exclude_censored=true`

  These two parameters can be combined, and the result is all the episodes available on the official website.

  -> [Only Available Episodes](/api/episodes/random?exclude_paramount_plus=true&exclude_censored=true) `/api/episodes/random?exclude_paramount_plus=true&exclude_censored=true`

- [Albums]

  -> [Random Album](/api/albums/random) `/api/albums/random`

  -> [Random Album (Excluding unavailable albums)](/api/albums/random?exclude_not_available=true) `/api/albums/random?exclude_not_available=true`

- [Songs]

  -> [Random Song](/api/songs/random) `/api/songs/random`

  -> [Random Song (Excluding unavailable songs)](/api/songs/random?exclude_not_available=true) `/api/songs/random?exclude_not_available=true`

- [Games]

  -> [Random Game](/api/games/random) `/api/games/random`

- [Chinpokomon]

  -> [Random Chinpokomon](/api/chinpokomons/random) `/api/chinpokomons/random`

## Database Update {.blog_title}

### (F Characters) {.blog_subtitle}

All the characters from the TV show whose names start with F [ID 697](/api/characters/697) -> [ID 741](/api/characters/741)

### Fixes in the database {.blog_subtitle}

- In the Characters database, all characters that had a null value in the "famous_guest" field now have it set to False. This error only affected the database; in the response, null values are shown as false.

- [Satan Family](/api/families/42): The image now shows Satan and Damien instead of a placeholder image.

- [The Clintons](/api/families/58): The image now shows Hillary and Bill Clinton.  
  *Note: Hillary Clinton is not in the database yet.*

- [The Handlers](/api/families/21): The image has been added.
*Note: This image has a low resolution, is the best image that I found.*

- [The McArthurs](/api/families/23): The image has been added.

- [The McDonalds](/api/families/54): The Image has been added.

### Change in character classification criteria {.blog_subtitle}

Previously, it wasn’t very clear which characters should be considered famous guests and which should not. I’ve finally unified the criteria, and this will be the definitive rule: **any real person or real entity, any copyrighted fictional character, or any religious figure will be classified as a famous guest**, except for those who, in the series, have meaningful character development or a long-standing presence. Some examples follow:

→ Jesus, [Satan](/api/characters/193), Santa Claus, Moses, and God will **not** be considered famous guests because they have their own personalities and character development within the series, and God’s design is original to South Park.

→ Characters like [Buddha](/api/characters/406) and the remaining members of the “Super Best Friends” who were not mentioned in the first point **are considered famous guests**, as they do not have character development in the show.

→ The holograms of Michael Jackson, [Elvis Presley (Hologram)](/api/characters/677), and the Tupac hologram will be considered famous guests because they are based on real holograms.

→ Any character seen in [Imaginationland](/api/episodes/163) will be considered a famous guest, except for those listed in the first point.

→ Characters based on internet memes are considered famous guests.

### Typographical Errors fixed: {.blog_subtitle}

- censured has been corrected to censored.
- avalible has been corrected to available.