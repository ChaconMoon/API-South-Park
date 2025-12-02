![Header](/blog/images/The_G_Update.webp){.header_image}
# Group Update {.blog_entry_title}

Introducing API update 0.4, which adds episode 330, new characters whose names start with the letter 'G', and the creation of the groups endpoint.
{.blog_intro}

## New Groups Endpoint {.blog_title}

This update introduces a new endpoint dedicated to groups, allowing you to get a specific group by its ID or a random one.

- [Get a group by ID](/api/groups/1): `/api/groups/1`
- [Get a random group](/api/groups/random): `/api/groups/random`

It's important to note that not all groups list individual members. Some, like the [Afghan children](/api/groups/14), are treated as a single entity. The characters that make up these groups will be added to the database later, once the main alphabetical listing is complete. Their inclusion will depend on whether it's possible to obtain an individual image and a name. If they don't have an official name, they will be assigned a generic one (e.g., "Kyle-like Afghan Kid").

## Database Updates {.blog_title}

- All characters from the show whose names start with 'G' have been added: [ID 742](/api/characters/742) -> [ID 796](/api/characters/796).

- 4 new families have been added, including a fix for the missing Trump family. [ID 74](/api/families/74) -> [ID 78](/api/families/78)

## New Episode: Season 28 EP 4 'Turkey Trot' {.blog_title}

- Episode [330](/api/episodes/330) of the series has been added.

- This episode does not introduce any new characters that need to be included alphabetically; the new character it introduces will be added to the API when their turn comes alphabetically.

## API Response Changes {.blog_title}

- The `family` field in the character response now returns an object with the name and a direct URL to the family's endpoint. This change aims to improve consistency with other fields, such as songs in albums, and to minimize the number of requests needed to get a character's full information.
- The `group` field has been temporarily removed from characters. This field will be restructured in a future update to make its functionality consistent with the `family` field.

# Developer Notes {.blog_entry_title}

This is the first in a series of 'parity' updates, focused on making both the database and the API responses more consistent. Although it will be a long process, I am convinced that it will facilitate smoother development in the future.

It is likely that there will not be a new update next week to allow for more development time. My goal is to release the next version to coincide with the end of the current season.