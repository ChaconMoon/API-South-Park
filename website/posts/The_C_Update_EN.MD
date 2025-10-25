![Header](/blog/images/C_Update.webp){.header_image}
# The C Update {.blog_entry_title}

This is the first data update since the website's creation, the C update (I don't know how to name character updates, for now it stays with the initial until I come up with something better.)
{.blog_intro}

The main change in this update is the addition of all characters from the TV show whose names begin with C. This currently excludes the movie and Paramount Plus specials, which will be added in a future update, although characters that have appeared in the show after the movie or a special will be included.

## Main update changes {.blog_title}

- Addition of show characters whose names begin with C
- Change in development blog thumbnails. They now display their title in the thumbnail, as shown in this case.

![Thumbnail Example](/blog/images/C_Update.webp){.body_image}

- Reordering of development blog articles, previously sorted from oldest to newest, now from newest to oldest.

The API has an Easter Egg at ID 210, which is the ID between family characters and alphabetically ordered characters, serving as a separator. This Easter Egg was previously the character "Carlos" but his ID has been changed to match his alphabetical order [ID: 444](/api/characters/444). Now this Easter Egg is the character Charlie Brown, who now has [ID: 210](/api/characters/210)

## Bug Fixes {.blog_title}

### Database errors {.blog_subtitle}

The following character records that had no image have been updated:

- [Shelly Marsh ID: 17](/api/characters/17)

- [Murray Broflovski ID: 23](/api/characters/23)

- [Alexandra Cartman ID: 36](/api/characters/36)

- [Karen McCormick ID: 50](/api/characters/50)

- [Thomas Tucker ID: 56](/api/characters/56)

- [Barney ID: 68](/api/characters/68)

- [Mrs. Anderson ID: 76](/api/characters/76)

- [Chad Handler ID: 120](/api/characters/120)

- [Louis Handler ID: 121](/api/characters/121)

- [Alexis Testaburger ID: 190](/api/characters/190)

- [Satan ID: 193](/api/characters/193)

- [Ali Khamenei ID: 239](/api/characters/239)

- [Barack Hussein Obama II ID: 283](/api/characters/283)

- [Bloods (Gang) ID: 346](/api/characters/346)

- [Brad Morgan ID: 380](/api/characters/380)

### The following alter ego records with missing images have been fixed {.blog_subtitle}

- [Shielmaiden Wendy -> Character: 188, AlterEgo: 2](/api/characters/188/alteregos/2)

- [Fastpass -> Character: 199, AlterEgo: 5](/api/characters/199/alteregos/5)

### Typographical corrections {.blog_subtitle}

- The Spanish word "serie" has been replaced with "show" throughout the project.

### Website errors {.blog_subtitle}

- Fixed the error where the 404 error page was returning a 200 response code.

## Added Tests {.blog_title}

- Added a test that checks all existing character images
- Added a test that checks existing alter ego images