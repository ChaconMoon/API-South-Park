# Update 0.7 (K Update) {.blog_entry_title}

Changes in Version 0.7
{.blog_intro}

## New Characters {.blog_title}

49 new characters added.

- characters from [Kanye West (character 1000)](/api/characters/1000) to [Kylo Ren (character 1048)](/api/characters/1048)

## Bug Fixes {.blog_title}

- A spelling error regarding the word "item" was fixed: /api/fortnite/item/1/image -> /api/fortnite/items/1/image
- The Fortnite item [Cheesy Poofs](/api/fortnite/items/3/) wasn't added in the original update.

## Changes to the Endpoints of the Fortnite Update {.blog_title}

- Filter by type. Example (skin): [/api/fortnite/cosmetics/?type=Skin](/api/fortnite/cosmetics/?type=Skin)
- Filter by price. Example (1500 V-Bucks): [/api/fortnite/cosmetics/?price=1500](/api/fortnite/cosmetics/?price=1500)
- Filter by rarity. Example (Epic): [/api/fortnite/cosmetics/?rarity=Epic](/api/fortnite/cosmetics/?rarity=Epic)

(These filters can be combined.)

Now, Fortnite cosmetics can be retrieved as a list: [/api/fortnite/cosmetics/](/api/fortnite/cosmetics/)

Now you can search the item database:
[/api/fortnite/items/?search=Kenny](/api/fortnite/items/?search=Kenny)