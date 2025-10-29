![Header](/blog/images/Index_Optimization_Part1_ES.webp){.header_image}
# Index Optimization — Part 1 {.blog_entry_title}

This development blog entry is about an update I made to the website's index. Since its creation, I knew it loaded very slowly; this was because the page loaded entirely from the beginning and, moreover, it's dynamic with the API: all character cards are generated on the fly. The problem was that it made about 50 requests at once. This caused the website to load slowly because it wouldn't finish until processing all 50 requests.
{.blog_intro}

I've optimized this so that the website only makes the necessary requests; that is, it now only loads what you're seeing. For example, in this case, it's only loading the 12 requests it needs.

![Header](/blog/images/Characters_Loaded_Index_1.webp){.body_image}

Now, when loading, it only needs to load a maximum of 20% of the original content, which has greatly improved server loading. However, the problem now is the time it takes to process API requests. When serving the website, I opted for the cheapest way to put it into production; this has resulted in using a server with 0.5GB of RAM and a processor thread with low availability. Because of this, the API is so slow that it takes 6 seconds to process a request; with 12 requests, that's more than a minute to load the index, compared to less than 1 second it takes on my machine.

![Header](/blog/images/Example_Remote_Server_1.webp){.body_image}

![Header](/blog/images/Example_LocalHost_Server_1.webp){.body_image}

I've let some people test the local version and it seems they liked it, but it's not something I would have exposed permanently: first, to not reveal my public IP, and second, to not have the computer running all the time.

I've been doing the math, and to have this equipment deployed with acceptable availability would cost me approximately €30-40 per month, a cost that I see as excessive, especially for something that's still in development and I don't know how long it will take; I would like to finish it by March.

Buying a Raspberry Pi 5 and self-hosting it with a reverse proxy seems like an increasingly better option; I don't think this will scale enough to need dedicated hosting. And if it eventually does, I suppose it will be because it has succeeded.

I will try to continue optimizing this project as much as possible. Images are no longer a problem in terms of loading, at least not as big as before. I will keep you informed.

Goodbye. Thank you very much for reading this.