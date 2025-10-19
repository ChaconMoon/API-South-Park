![Header](/blog/images/6_7_Episode.webp){.header_image}
# The 6-7 Update {.blog_entry_title}

This is the development blog about the update for episode 1 of season 28, episode 327 of the series.
{.blog_intro}

Although this episode doesn't add much to the API in its current state, I find it necessary to comment on some changes it brings. Episode 326 brought 2 new characters to the API as they started with A and B, I had to add them automatically since those are the 2 letters currently covered by the API. Here no character debuts, but I do have to make some changes.

## Changes Affecting the Current API {.blog_title}

### New Episode {.blog_subtitle}

Episode 327 (Twisted Christian) has been added, marking the beginning of season 28. It can be found [here](/api/episodes/327)

Additionally, with a new episode added, the "last episode" endpoint now refers to episode 328. [last episode](/api/lastepisode)

![Last Episode Screenshot](/blog/images/Last_Episode_327.webp){.body_image}

### Strong Christian Woman {.blog_subtitle}

This episode has changed a character "Strong Woman" [ID 163](/api/characters/163). In this episode, she had a design change and name change to "Strong Christian Woman" with a design showing she had surgery. I considered this change significant enough to treat it like the Token to Tolkien change and consider it a name change, so her character has been updated in the API and the operated design has been added as a second design.

I did this because my purpose is to keep the API updated to the current state of the series, and this includes updating the character files.

However, for now, since I don't know how long this design will last, I'll leave the Strong Christian Woman design as the second design and her normal design as the first. If by the end of season 28 she hasn't changed back, I'll change the order of appearance of the designs. Following that same logic, if they change her design back to normal, I'll undo the name change.

## Future API Changes {.blog_title}

The only new character that appeared in this episode is "Peggy Pockbottom", although she doesn't have a Wiki entry yet so I'll have to wait. I'll add her when I add the characters starting with P to the API. Additionally, with the same letter, "Peter Thiel" had a redesign in this episode, so when I add the character to the database, it will be with the design from this episode.