"""Dictionaries to be tested."""


__author__ = "730466477"


def invert(initial_dictionary: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary where the keys and values are inverted."""
    new_dictionary: dict[str, str] = {}
    for key in initial_dictionary:
        if initial_dictionary[key] in new_dictionary:
            raise KeyError("Duplicate key values are not allowed!")
        new_dictionary[initial_dictionary[key]] = key
        
    return new_dictionary


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the most listed color in the dictionary."""
    color_count: dict[str, int] = {}
    for name in dictionary:
        color = dictionary[name]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    max_count: int = 0
    max_color: str = ""
    for color in color_count:
        if max_count < color_count[color]:
            max_color = color
            max_count = color_count[color]    
    return max_color
         

def count(given_list: list[str]) -> dict[str, int]:
    """Returns a dictionary showing how many times each value shows up in a list."""
    counted_dict: dict[str, int] = {}
    for item in given_list:
        if item in counted_dict:
            counted_dict[item] += 1
        else:
            counted_dict[item] = 1
    
    return counted_dict

    
