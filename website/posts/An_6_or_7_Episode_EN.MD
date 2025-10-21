![Header](/blog/images/6_7_Episode.webp){.header_image}
# The 6-7 Update {.blog_entry_title}

This is the development blog about the update for episode 1 of season 28, episode 327 of the series.
{.blog_intro}

Although this episode doesn't add much to the API in its current state, I find it necessary to discuss some changes it brings. Episode 326 brought 2 new characters to the API, and since they started with A and B, I had to add them automatically as these are the 2 letters currently covered by the API. In this episode, no new characters debut, but I do have to make some changes.

## Changes Affecting the Current API State {.blog_title}

### New Episode {.blog_subtitle}

Episode 327 (Twisted Christian) has been added, marking the beginning of season 28. It can be found [here](/api/episodes/327)

Additionally, with the addition of a new episode, the "last episode" endpoint now refers to episode 327. [last episode](/api/lastepisode)

![Last Episode Screenshot](/blog/images/Last_Episode_327.webp){.body_image}

### Strong Christian Woman {.blog_subtitle}

This episode has changed a character "Strong Woman" [ID 163](/api/characters/163). In this episode, she has undergone a design change and name change, becoming "Strong Christian Woman" with a post-surgery design. I've considered this change significant enough to treat it like the Token to Tolkien change and consider it a name change, so her character has been updated in the API and the operated design has been added as a second design.

I've done this because my goal is to keep the API updated to the current state of the series, and this includes updating the character profiles.

However, for now, since I don't know how long this design will last, I'll leave the Strong Christian Woman design as the second design and keep her normal design as the first. If by the end of season 28 she hasn't changed back, I'll switch the order of the designs. Following the same logic, if they change her design back to normal, I'll undo the name change.

## Changes Affecting the Future API {.blog_title}

The only new character that appeared in this episode is "Peggy Pockbottom". I'll add her when I implement characters starting with P. Additionally, "Peter Thiel" (also starting with P) has had a redesign in this episode, so when I add the character to the database, it will be with the design from this episode.