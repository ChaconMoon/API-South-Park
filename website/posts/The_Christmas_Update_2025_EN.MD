![Header](/blog/images/Christmas_Update_2025.webp){.header_image}
# Christmas Update (2025) {.blog_entry_title}

Happy holidays, or happy day, you might be seeing this after Christmas. This is the 2025 Christmas update, and I'm already assuming there will be one in 2026, hopefully. Maintaining this API for a year would be a great achievement for me. Well, this will be the last update of the year and the last update of season 28. I think that even though it took 2 weeks, it will be a fairly complete update.
{.blog_intro}

## API Endpoint Updates {.blog_title}

Now all endpoints, except for songs, have an endpoint to get all records, as well as to limit the number of records and perform searches.

For example:

- Get all groups `http://<your_ip>/api/groups`
- Get the first 5 groups `http://<your_ip>/api/groups?limit=5`
- Get the first 3 groups containing 'The' `http://<your_ip>/api/groups?search=The&limit=3`

The reason this hasn't been done with songs is that the albums themselves contain the songs. Still, I might implement it in a future update.

## Content Updates {.blog_title}

### New Episode 331 (Season 28 Finale) {.blog_subtitle}

- Episode 331 ([The Crap Out](/api/episodes/331)) has been added.

- The Antichrist ([Satan's baby](/api/characters/797)) has been added as a character.

This is the first character in the series to have died before birth. I was hesitant about adding him, but since I started this API with the idea that he would be the last character of the season to be added, plus the fact that in the United States, a baby who dies after 20 weeks of pregnancy is considered a stillborn, I wanted to include him with the peculiarity of being 0 years old.

## Character Updates {.blog_title}

- All characters from the series whose names start with H or I have been added: [798](/api/characters/798) -> [868](/api/characters/868).

- 3 new families have been added: [79](/api/families/79) -> [81](/api/families/81).

## Internal API Update {.blog_title}

This is not visible to API users, but internally the way database queries are made has been changed. Now queries are done using an ORM model instead of raw queries, which greatly facilitates the creation of new endpoints, as the code has been simplified a lot. That is the reason why this update has taken 2-3 weeks. The next update will be out soon.

## Developer's Note {.blog_title}
I will probably take a short break during the Christmas period and will start 2026 with a new character update. In a way, it feels strange to have to wait 6 months for the next episode update. I trust I will have finished the API by then, or at least the characters, and also have found better hosting for the API. I feel that what I would most like to have achieved in that time is a renowned project. I have big plans for this project, and I hope they come true.

Happy holidays to everyone who sees this and a happy 2026.