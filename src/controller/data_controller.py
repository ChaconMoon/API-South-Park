"""
Module written by Carlos Chacón.

This module translate an array in the Postgre database and returns a Python array
"""


def parse_array_to_list(values: str, is_url: bool = False, base_url=""):
    """
    Get a list with a values of the Postgre database and return it at an array

    Params:
        values (str): The list with the values
        is_url (bool): Determine if a the list of the values are URLs
        base_url (str): The base URL used to create the reference URL
    """
    if not values or values is None:
        return None

    # Clean the string
    value_str = str(values).strip()

    # If the string is None or Empty return a empty array.
    if value_str in ["{}", "None", ""]:
        return []

    # Remove the dictionary and array chars in string.
    value_str = value_str.strip("{}[]'")

    # If the string is None or Empty return a empty array.
    if not value_str:
        return []

    # Split the elements using the comma, removes the invert commas.
    items = []
    for item in value_str.split(","):
        clean_item = item.strip().strip("\"'")

        # If the element is a URL add the base url and return it, else return it without changes.
        if clean_item:
            if is_url:
                clean_item = base_url.strip("/") + clean_item
            items.append(clean_item)

    return items
