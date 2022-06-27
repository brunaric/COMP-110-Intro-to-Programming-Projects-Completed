"""Dictionary Test."""


import pytest
from dictionary import invert
from dictionary import favorite_color
from dictionary import count
__author__ = "730466477"
                                          

def test_invert() -> None:
    """Use Case #1."""
    test_dictionary: dict[str, str] = {"a": "1", "b": "2"}
    assert invert(test_dictionary) == {"1": "a", "2": "b"}


def test_invert_2() -> None:
    """Use Case #2."""
    test_dictionary: dict[str, str] = {"Sally": "ran", "Jack": "jumped"}
    assert invert(test_dictionary) == {"ran": "Sally", "jumped": "Jack"}


def test_invert_3() -> None:
    """Edge Case #1."""
    test_dictionary: dict[str, str] = {"COMP": "110", "ECON": "101"}
    assert invert(test_dictionary) == {"110": "COMP", "101": "ECON"}


def test_invert_4() -> None:
    """Edge Case #2."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color() -> None:
    """Use Case #1."""
    test_dictionary: dict[str, str] = {"bruna": "purple", "sally": "brown", "jack": "red", "kurt": "purple"}
    assert favorite_color(test_dictionary) == "purple"


def test_favorite_color_2() -> None:
    """Use Case #2."""
    test_dictionary: dict[str, str] = {"Anyone super cool": "carolina blue", "Smart people": "carolina blue", "worst person ever": "duke blue"}
    assert favorite_color(test_dictionary) == "carolina blue"


def test_favorite_color_3() -> None:
    """Edge Case #1."""
    test_dictionary: dict[str, str] = {"a": "red", "b": "red", "c": "black", "d": "black", "e": "yellow"}
    assert favorite_color(test_dictionary) == "red"


def test_count() -> None:
    """Use Case #1."""
    test_list: list[str] = ["1", "1", "2", "2", "3", "3", "4", "4", "4", "4"]
    assert count(test_list) == {"1": 2, "2": 2, "3": 2, "4": 4}


def test_count_2() -> None:
    """Use Case #2."""
    test_list: list[str] = ["bruna", "bruna", "carolina"]
    assert count(test_list) == {"bruna": 2, "carolina": 1}


def test_count_3() -> None:
    """Edge Case #1."""
    test_list: list[str] = []
    assert count(test_list) == {}
