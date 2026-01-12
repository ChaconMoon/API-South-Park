# Update 0.6 (J Update) {.blog_entry_title}

Changes in Version 0.6
{.blog_intro}

## Changes in project structure {.blog_title}

### Nre Docker data folder. {.blog_subtitle}

Now the Docker data folder is located in __/var/lib/southpark-api/__ this is the recomendade route in Linux production systems, this route can been changed in the Docker Compose.

### Changes in API Response {.blog_subtitle}

The images paths of the Families and Episodes have been significally changes, now the images are sending via streaming response and the image now is created and sent to the response, this image can be modified before send it, this is used to create smaller image and allow to load it with lazy loading, this change is now used by the index that use the small size of the images.

Example of families:

- [/api/families/1/image/1?size=large](/api/families/1/image/1?size=large) Large size 1280 x 720.
- [/api/families/1/image/1?size=medium](/api/families/1/image/1?size=medium) Medium size 960 x 540.
- [/api/families/1/image/1?size=small](/api/families/1/image/1?size=small) Small size 640 x 480.

Example of episode:

- [/api/episodes/1/thumbnail?size=large](/api/episodes/1/thumbnail?size=large) Large size 1280 x 720.
- [/api/episodes/1/thumbnail?size=medium](/api/episodes/1/thumbnail?size=medium) Medium size 960 x 540.
- [/api/episodes/1/thumbnail?size=small](/api/episodes/1/thumbnail?size=small) Small size 640 x 480.

__*This change is currently a experimental feature, the old URL currently works, in the nexts updates this change will be added to the all endpoints bethween I test if this is a good opction and optimize it.*__

## New Endpoint: {.blog_title}

Added a new endpoint that contains the butters punishments 'ButtersPunishments'. 

This endpoint returns:
- The ID of the punishment.
- The Episode where butters was punishmented
- The reason of the punsihment

Example: 

-> [/api/butterspunishments/1](/api/butterspunishments/1)

This endpoint can return metadata, but at the moment can't return a list.

-> [/api/butterspunishments/1?metadata=true](/api/butterspunishments/1?metadata=true)


## Database Update {.blog_title}

### Added all characters that their name starts with J {.blog_subtitle}

All the characters from the TV show whose names start with J have been added:

- Characters [869](/api/characters/869) `/api/characters/798` to Character [997](/api/characters/997) `/api/characters/997`

- Families [82](/api/families/82) `/api/families/82` to Family [88](/api/families/88) `/api/families/88`