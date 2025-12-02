# Update 0.4 (Groups Update) {.blog_entry_title}

Changes in Version 0.4
{.blog_intro}

## New endpoint {.blog_title}

- Added the endpoint [Groups](/api/groups/1). Return a group, Example The 4º grade boys.

- Added the endpoint [Groups (Random)](/api/groups/random). Returns a random group.

## Updates in the database: {.blog_title}

### Groups Update {.blog_subtitle}

- Added 96 groups to the database.

### Characters with G Update {.blog_subtitle}

- Added all the characters from the TV show that their name starts with G: [ID 742](/api/characters/742) -> [ID 796](/api/characters/796)

- Added Families: [ID 74](/api/families/74) -> [ID 78](/api/families/78)

## Fixes in database: {.blog_title}

- Added [Trump Family](/api/families/74)

## Change in responses: {.blog_title}

- The group param of the character has been deleted, it will return updated with the groups in a future update.

- The family param in characters has been modified to retrun a dict, this makes this section consistent with other endpoint.

## Internal changes: {.blog_title}

- The families, characters and songs now have a option to return a compact object, this dict only returns the name of a object and their URL.


