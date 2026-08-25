![Header](/blog/images/The_K_Update_EN.webp){.header_image}
# The K Update {.blog_entry_title}

Phew... It has been a long time, 5 months actually. During the first half of 2026, life has been crazy, at least for me. I started studying English and got my B2 Level, and after that, I began a professional degree to become a programming teacher in Spain. Life has its twists and turns, and in the midst of all this, I built a website for an association in Spain, so I didn't have the time to continue developing the API. But... I'm back!
{.blog_intro}

![Im Back](/blog/images/IM_BACK.gif){.body_image_compacted}

## API Updates {.blog_title}

### New Characters {.blog_subtitle}

Starting with the new characters whose names start with K, characters from [Kanye West (character 1000)](/api/characters/1000) to [Kylo Ren (character 1048)](/api/characters/1048) have been added. Officially, we have more than 1000 characters in the API and we are just getting through the Ks. There is still a long way to go; when the API is finished, there will be more than 2500 characters. This will be especially true for the letter M, as there are a lot of Mr. (someone) or Mrs. (someone). In fact, I'll let you know in advance that the M update will be divided into two parts, much like Minecraft's Caves & Cliffs update: there will be Misters and Misses Part 1 and Misters and Misses Part 2.

### Bug Fixes {.blog_subtitle}

The bugs from the Fortnite update have been fixed:

- A spelling error regarding the word "item" was fixed: /api/fortnite/item/1/image -> /api/fortnite/items/1/image
- The Fortnite item [Cheesy Poofs](/api/fortnite/items/3/) wasn't added in the original update.

### Changes to the Endpoints of the Fortnite Update {.blog_subtitle}

The option to filter the results of the Fortnite cosmetic endpoints has been added.

- Filter by type. Example (skin): [/api/fortnite/cosmetics/?type=Skin](/api/fortnite/cosmetics/?type=Skin)
- Filter by price. Example (1500 V-Bucks): [/api/fortnite/cosmetics/?price=1500](/api/fortnite/cosmetics/?price=1500)
- Filter by rarity. Example (Epic): [/api/fortnite/cosmetics/?rarity=Epic](/api/fortnite/cosmetics/?rarity=Epic)

(These filters can be combined.)

Now, Fortnite cosmetics can be retrieved as a list: [/api/fortnite/cosmetics/](/api/fortnite/cosmetics/)

Now you can search the item database:
[/api/fortnite/items/?search=Kenny](/api/fortnite/items/?search=Kenny)

## Farewell {.blog_title}

I know it might seem a bit weird to continue developing the API after so much time, but I'm still looking for a way to fund a server for it. Since no one is using the API right now, it's hard to find motivation. Even so, I am passionate about this project and I will fight however I can to push it forward.

For now, I can say that it has served me well as a programming teacher. It gives me the perfect example to show how to deploy a complete project. In fact, if I had developed this project back when I was a student, I almost certainly would have landed a job.

I look at my students' projects, and while they obviously have much less complexity, they are at a pretty good level—they just need to be more solid.

I consider this project solid enough to be treated as a totally serious endeavor, even though I still have a lot to improve. But I guarantee you that I will finish the API, and most importantly, I will make a name for myself with it. Right now I might be a nobody, but someday I will be somebody.

We will be back with Season 29. Anything could happen.