"""
Module written by Carlos Chacón.

This module provides functionality to parse PostgreSQL array data types into Python lists.
It handles both regular arrays and arrays of URLs, with special processing for URL paths.
"""


def parse_array_to_list(values: str, is_url: bool = False, base_url: str = "") -> list:
    """
    Convert a PostgreSQL array string representation into a Python list.

    Handles PostgreSQL array formats like '{item1,item2}' or '[item1,item2]' and
    converts them into Python lists. For URL arrays, prepends the base_url to each item.

    Args:
        values (str): PostgreSQL array string to parse
        is_url (bool): Whether the array contains URL paths
        base_url (str): Base URL to prepend to URL paths

    Returns:
        list: Parsed list of values, or empty list if input is invalid
        None: If input is None or empty string

    Examples:
        Regular array:
            parse_array_to_list("{item1,item2}") -> ["item1", "item2"]

        URL array:
            parse_array_to_list("{/path1,/path2}", is_url=True, base_url="http://api.com")
            -> ["http://api.com/path1", "http://api.com/path2"]

        Empty/Invalid inputs:
            parse_array_to_list("{}") -> []
            parse_array_to_list(None) -> None
            parse_array_to_list("") -> None

    """
    if not values or values is None:
        return None

    # Clean the string
    value_str = str(values).strip()

    # If the string is None or Empty return a empty array
    if value_str in ["{}", "None", ""]:
        return []

    # Remove the dictionary and array chars in string
    value_str = value_str.strip("{}[]'")

    # If the string is None or Empty return a empty array
    if not value_str:
        return []

    # Split the elements using the comma, removes the invert commas
    items = []
    for item in value_str.split(","):
        clean_item = item.strip().strip("\"'")

        # If the element is a URL add the base url and return it,
        # else return it without changes
        if clean_item:
            if is_url:
                clean_item = base_url.strip("/") + clean_item
            items.append(clean_item)

    return items
