![Header](/blog/images/Index_Optimization_Part2.webp){.header_image}
# Index Optimization — Part 2 {.blog_entry_title}

This blog entry is about discussing the second part of the index optimization.
{.blog_intro}

### Index Optimization. {.blog_subtitle}

I've ultimately decided to make the iframes that load on the main website static, which means that now the index page doesn't reflect the API's real-time state, only showing the state it had at the time of this update. However, this greatly speeds up the website's loading time, making it load quite fast despite the hosting server's limitations.

Nevertheless, the dynamic part of the website hasn't been removed from the code, it's just been commented out. So, as soon as I can afford better hosting, I can uncomment that part and the index will become dynamic again.

### Other Project Organization Improvements. {.blog_subtitle}

Besides these changes, other improvements have been made to the API code, including restructuring the endpoints within the code. Now all endpoints are categorized, making it easier for me to work by categories since everything is within the same folder. Additionally, the project's ``main`` function now only starts the application, that's its sole purpose; the entire API is now structured independently.

The data model within all endpoints has also been improved, and now all objects returned by the API inherit from the same object that requires them to implement the necessary methods, leaving all response formatting to the data model.

Furthermore, I've now implemented a pre-commit hook that forces me to comment and will ensure all code is better formatted before making changes on GitHub, which means updates might take longer to arrive, but they will be of higher quality.

### Future Project Improvements. {.blog_subtitle}

In addition to the previously mentioned improvements, the database connection will be enhanced in the future. Due to the rush at the project's start, database queries are currently hardcoded, which isn't the right approach. The proper way would be to use an ORM; this change will be made in the future, along with implementing interfaces for database connections to keep the database connection as abstracted as possible, aiming to have the most robust software possible.