"""Utils Test Exercise 5."""

__author__ = "730466477"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens() -> None:
    """Use Case #1."""
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]


def test_only_evens_2() -> None:
    """Edge Case #1."""
    test_list: list[int] = []
    assert only_evens(test_list) == []


def test_only_evens_3() -> None:
    """Use Case #2."""
    test_list: list[int] = [5, 10, 15, 20, 25, 30, 35, 40]
    assert only_evens(test_list) == [10, 20, 30, 40]


def test_sub() -> None:
    """Use Case #1."""
    given_list: list[int] = [10, 20, 30, 40]
    assert sub(given_list, 0, 4) == [10, 20, 30, 40]


def test_sub2() -> None:
    """Edge Case #1."""
    given_list: list[int] = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33]
    assert sub(given_list, 8, -5) == []


def test_sub_3() -> None:
    """Use Case #2."""
    given_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8]
    assert sub(given_list, 1, 8) == [2, 3, 4, 5, 6, 7, 8]


def test_sub_4() -> None:
    """Edge Case #2."""
    given_list: list[int] = []
    assert sub(given_list, -1, 0) == []


def test_concat() -> None:
    """Use Case #1."""
    first_list: list[int] = [1, 2, 3]
    second_list: list[int] = [4, 5, 6]
    assert concat(first_list, second_list) == [1, 2, 3, 4, 5, 6]


def test_concat2() -> None:
    """Edge Case #1."""
    first_list: list[int] = [-100 % 8]
    second_list: list[int] = []
    assert concat(first_list, second_list) == [4]


def test_concat3() -> None:
    """Use Case #2."""
    first_list: list[int] = [2, 4, 6, 8]
    second_list: list[int] = [10, 12, 14, 16]
    assert concat(first_list, second_list) == [2, 4, 6, 8, 10, 12, 14, 16]

    
def test_concat4() -> None:
    """Edge Case #2."""
    first_list: list[int] = []
    second_list: list[int] = []
    assert concat(first_list, second_list) == []