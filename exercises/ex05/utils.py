"""Function Skeletons and Implementations for Exercise 5."""

__author__ = "730466477"


def only_evens(given: list[int]) -> list[int]:
    """Returns only even elements of a given list."""
    i: int = 0
    evens: list[int] = list()
    while i < len(given):
        if given[i] % 2 == 0:
            evens.append(given[i])
        i += 1
    return evens


def sub(given_list: list[int], start_index: int, end_index: int) -> list[int]:
    """Returns a list that is constructed from the indexes of a given list defined by parameters start_index and end_index."""
    i: int = start_index
    new_list: list[int] = []
    if i < 0:
        i = 0
    if end_index > len(given_list):
        end_index = len(given_list)
    if given_list == [] or len(given_list) == 0 or start_index > len(given_list) or end_index <= 0:
        return []
    while i < end_index:
        new_list.append(given_list[i])      
        i += 1
    return new_list


def concat(first: list[int], second: list[int]) -> list[int]:
    """Returns a list made up of the elements of the first parameter list and the second parameter list."""
    i: int = 0
    final_list: list[int] = list()
    while i < 1:
        final_list = first + second
        i += 1
    return final_list
