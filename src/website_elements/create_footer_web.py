"""
Module written by Carlos Chacón.

This Module defines the creator function to create the footer section
in the website.
"""


def create_footer() -> str:
    """
    Create the footer HTML section that contains the license information.

    Returns:
            ``str``: The string that defines the HTML code of the footer.

    """
    return """
        <div id="licence">
                        <h1>Licence</h1>
                        <p>
                                This API was created by Carlos Chacón <a href="https://github.com/ChaconMoon"
                                        class="footer_link">
                                        [https://github.com/ChaconMoon]
                                        </a> under a GPL 3.0
                                license
                                <a href="https://www.gnu.org/licenses/gpl-3.0.html"
                                        class="footer_link">[https://www.gnu.org/licenses/gpl-3.0.html]</a>.

                                All data for the API has been obtained directly from
                                 the website: <a
                                        href="https://southpark.wiki.gg/"
                                        class="footer_link">[https://southpark.wiki.gg/]</a>
                                under a CC BY-SA license <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.es"
                                        class="footer_link">[https://creativecommons.org/licenses/by-sa/4.0/deed.es]</a>.
                                Therefore,
                                this API can be forked, modified, and distributed
                                 as long as the authorship of both the data and
                                the API is properly attributed.
                                The characters, episodes, and the South Park brand
                                 are owned by Viacom Inc. and South Park
                                Digital Studios.
                        </p>
                </div>
        """
