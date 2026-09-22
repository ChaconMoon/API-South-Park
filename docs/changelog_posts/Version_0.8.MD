# Update 0.8 (E-bike Update){.blog_entry_title}

Changes in Version 0.8
{.blog_intro}

## New Character {.blog_title}

Added 1 new character:

- [Keller's Bike Shop Owner (/api/characters/1049)](/api/characters/1049)

## Starting Season 29

Added Episode 332:

- [South American Biker Gangs (/api/episodes/332)](/api/episodes/332)

## Changes to the Episode Endpoint

Episode 332 is the first episode since I started developing this API that does not have a page on the official website, though it does have clip clips available.

To handle this, I added a new boolean column to the `Episodes` database table named `has_website_url`. For episodes missing an official page, the JSON response will now return `"NO WEBSITE URL"` (or `null`) in the `website_url` field instead of a URL.
