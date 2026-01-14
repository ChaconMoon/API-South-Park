![Header](/blog/images/The_J_Update.webp){.header_image}
# The J Update {.blog_entry_title}
Welcome to the first update of 2026, the J update or version 0.6. This update brings all the characters whose names start with J, a new endpoint related to Butters, and changes in image processing.
{.blog_intro}

## Additions to the API {.blog_title}

### New Characters {.blog_subtitle}
The main novelty of this update is all the game characters whose names start with J: from Character 869 [J.J Abrams] [/api/characters/869](/api/characters/869) to [Justin Trudeau] [/api/characters/997](/api/characters/997). We are about to reach 1000 characters in the API; I have already completed more than half of the progress, so I might finish soon. Hehe.

### New Endpoint (Butters' Punishments) {.blog_subtitle}
A new endpoint 'butterspunishments' has been added, which contains a list of punishments Butters has suffered throughout the series. Although I may have missed some, if so, I will add them.

For example:

- [/api/butterspunishments/1](/api/butterspunishments/1) Butters is punished for making a face in the school photo.
- [/api/butterspunishments/15](/api/butterspunishments/15) Butters is punished for giving Cartman a hickey.

This endpoint can return metadata, but it cannot yet show the complete list.

### Changes in Image Processing (Episodes and Families) {.blog_subtitle}

The way images for families and episodes are returned has changed. The category links now have a format similar to this:

- [/api/episodes/1/thumbnail](/api/episodes/1/thumbnail) Episode images.
- [/families/1/image/1](/families/1/image/1) Image 1 of family 1.

Now, instead of accessing the file directly on the server, the file is generated and modified before being sent, allowing alterations to be sent via parameters.

- [/api/families/1/image/1?size=large](/api/families/1/image/1?size=large) Large size 1280 x 720.
- [/api/families/1/image/1?size=medium](/api/families/1/image/1?size=medium) Medium size 960 x 540.
- [/api/families/1/image/1?size=small](/api/families/1/image/1?size=small) Small size 640 x 480.

The same sizes apply to video thumbnails. If nothing is specified or '?size=original' is used, the original image is retrieved at 1920 x 1080.

I'm considering adding an even smaller size.

This change is currently in an experimental phase; it has not replaced the old links, which will continue to work until this leaves the experimental phase. However, they are no longer visible in the response.

The purpose of releasing it experimentally is to evaluate whether such a change is feasible, and if the cost to the server for processing the image is worth the bandwidth reduction.

Additionally, images are now sent via byte streaming, so they can be loaded "lazily," allowing the section to load while the image is being downloaded.

In fact, this change is already applied on the website, and you can see how the images of families and episodes load gradually and use the "small" resolution.

In the following updates, it will be implemented in the rest of the endpoints as I optimize and evaluate its reliability.

The next update will be released next week; it will be a mini-version, instead of version 0.7 it will be version 0.6.5. This update will consist of a new endpoint and the addition of a new table to the API.

More news coming soon.

I wish you all a very good start to the year!
