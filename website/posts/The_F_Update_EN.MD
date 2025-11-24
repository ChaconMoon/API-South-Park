![Header](/blog/images/The_F_Update.webp){.header_image}
# The Force of chance Update {.blog_entry_title}

Welcome to the development blog for version 0.3 of the API! In this update, we've added all the characters from the series whose names start with F, as well as the ability to get random results from every endpoint.
{.blog_intro}

## New Endpoints {.blog_title}

Now, all API endpoints include an option to retrieve a random record under different conditions.

- [Random character](/api/characters/random) `/api/characters/random`
- [Random character (excluding famous guests)](/api/characters/random?exclude_famous_guests=true) `/api/characters/random?exclude_famous_guests=true`

All these endpoints follow the structure: `api/'category'/random`. For alter egos, the category is `alteregos`.

You can see more details in the [changelog](/changelog/Version_0.3).

These endpoints are designed to be used in bots or programs that require random results, making their development much easier.

## New characters in the database {.blog_title}

All characters from the series whose names start with F have been added: from [ID 697](/api/characters/697) to [ID 741](/api/characters/741).

## Changes in API responses {.blog_title}

Due to the new filters for random characters, I have established clear criteria for what is and isn't a famous guest. In summary: "Any character who hasn't had a prominent role in the series and is a real or fictional person or entity will be considered a guest, excluding those who have had their own development or whom South Park has reinterpreted in another way."

*In the future, characters meeting these criteria will be reviewed and assigned the corresponding value.*

Typographical errors in the words "AVAILABLE" and "CENSORED" have also been corrected.

In addition, missing photos have been added for all families.

## Developer's note {.blog_title}

Personally, I consider this one of the most important updates for the API, mainly because one of the uses I want to encourage is the creation of bots that request random characters for games on Discord or Twitter. I myself have the idea of developing a bot to test the API, and thanks to this update, I'll be able to do it.

The next update should include the next episode of the series, characters whose names start with G, and some other new features.

To finish: if you're reading this, I want to let you know that the API now has an official Twitter account, where updates and curiosities about the development will be posted. I invite you to follow me there: [@SouthParkAPI](https://x.com/SouthParkAPI)