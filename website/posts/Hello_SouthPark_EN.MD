![Header](/blog/images/Hello_South_Park.webp){.header_image}
# Hello, South Park {.blog_entry_tittle}

This is the first entry of the API development blog.
{.blog_intro}

I have finally decided to treat this API as a living project: while the application is in beta, the API will remain operational during its development. I believe this has both advantages and disadvantages, both for me and for users.

- I'll be able to work and test the API live and receive feedback.
- Greater involvement on my part knowing that it's evolving.
- Having a more serious project, with an update history and a changelog.
- Possibility of making a more solid and better organized project.

The downside is that I won't be able to guarantee that the API will always be compatible with the changes that arise until reaching version 1; after that, I will version the API.

## Changes in this update {.blog_title}

### Development Blog {.blog_subtitle}
The main change in this website is this development blog itself. As this is a project that will be kept alive, I see it necessary to have a blog telling about the updates. This blog is created thanks to a dynamic pagination system that I've created using the website's backend. This structure is capable of interpreting Markdown files like the one I'm writing right now. These files have a specific format that is converted to HTML with classes that I later format with CSS, and it has a list of all the articles I want to show, so I can be working on an article that's in the code but not published.

![Markdown Document](/blog/images/Markdown_Dev_Blog.webp){.body_image}

For now, I'm very happy with this result, although I'll be changing and modifying it according to the needs of the moment. I'm not yet very aware of its limitations as it's something entirely homemade. I'll keep improving it.

Although at the time of writing this it only has 2 articles so it's not visible, but it has a pagination system that generates pages according to the number of articles. In this example, I've generated 16 articles by copying and pasting the same one (I'm not going to write that much), and it creates 2 pages of 6 articles and an additional one with 4, that is, 16 articles in 3 pages.

![Blog Index](/blog/images/Blog_index.webp){.body_image}

### 404 NOT FOUND {.blog_subtitle}

During the development of the blog page, the need arose to ensure that users don't end up on empty websites and strange places, so I had to create a not found route page, it's the following.

![404 Page](/blog/images/Page_404.webp){.body_image}

This page has my South Park avatar with a sign. I was going to do it with Stan, Kyle, Kenny, and Cartman but for now, I haven't found how to do it and make it look good.

This page has 4 designs: 3 designs that have a 33% chance of appearing and one secret one that has a 1% chance of appearing.

![404 Avatars](/blog/images/404_Avatars.webp){.body_image}

As I like to add some intrigue, you can see it here or if you can't wait for it to appear, hehe: [Secret Avatar](/img/website/Cartel_NOT_FOUND_Charlie_Brown.webp)

Also, you can return to the website or blog directly from here.

### Developer's Message {.blog_subtitle}

I acknowledge that I'm achieving a much more solid project than I thought; I'm really enjoying how it looks and the possibilities I see in it. Although I'm aware that many parts can and should be automated, I'm enjoying it or at least trying to enjoy it.

The problem that the index takes too long to load is serious, and I'm considering multiple options to fix it, I'll take what I consider best or even combine several of them.

I want to see my projects as if they were my children and treat each one with the delicacy they deserve. I could dedicate myself to making small projects, but I like to see how something like this evolves over time.

I want to be able to feel proud of what I do and see that all the effort put into a project like this is worth it in the medium-long term.

The next update will come out on October 17-18, 2025, adding to the API the first episode of season 28. It will be something very small but I think I'll write a small article talking about it.