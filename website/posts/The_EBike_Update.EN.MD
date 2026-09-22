![Header](/blog/images/The_Ebikes_Update_EN.webp){.header_image}
# The e-bikes Update {.blog_entry_title}

I'm arriving a bit in injury time, but I can finally say that this API is back up to date with the show. The South API welcomes South America with open arms and a hand on its chest.

This update is very small because I didn't want episodes 1 and 2 to pile up on me, so I thought it was best to push back the character update to the next version (0.9) and drop a "surprise" or two along the way. But this blog entry is about version 0.8, so let's get into it!
{.blog_intro}

## Added to the API {.blog_title}

### New Characters {.blog_subtitle}

Character 1049 has been added: [Keller's Bike Shop Owner](/api/characters/1049).

### New Episode {.blog_subtitle}

Episode 332 of the show has been added: "[South American Biker Gangs](/api/episodes/332)".

## Changes to the API {.blog_title}

### New field: Does it have a website entry? {.blog_subtitle}

While working on the API, I stumbled into the "issue" that this is the very first episode that doesn't actually have a page on the official South America Studios (South Park Studios) website. It surprised me, as it hadn't happened once since I started developing the API. Considering this might keep happening in the future, I created a new field in the database's episodes table to specify whether an episode has a entry on the website—since that was what I previously used as a reference point. If they add the website entry in future updates, I'll update the record for that episode, though my plan is to keep the field just in case.

## Developer Reflection {.blog_title}

Although it might look like a small update (and it is), I admit I've been feeling a bit lazy. I spent a good chunk of time figuring out what to do with the API for this new season: whether to finish up the character database or add cool new endpoints. My original idea was to completely rename the API from "South Park API" to "South America API." Even though it could end up being wildly confusing, my goal with this API has always been to stay as up to date with the show as possible, and that includes changes like these. However, going through the trouble of changing names, descriptions, and even old blog posts would have been way too drastic. On top of that, I'd have to check which episodes changed their synopses one by one to update the records, so that option is completely ruled out (the words "South Park" appear 347 times across the entire API, counting that last one).

The next update will be for episode 333 of the series, which currently has neither a synopsis nor a trailer (wonder what it'll be about...). Along with that, I hope to have enough time to finish the characters whose names start with the letter L and a new endpoint I'm cooking up. It should be out by mid-next week—ideally before the next episode airs, but it'll depend on when I finish it. Although I'm struggling to find the motivation to keep working on the API and it's starting to feel like a slog, I hope it becomes more enjoyable over time.