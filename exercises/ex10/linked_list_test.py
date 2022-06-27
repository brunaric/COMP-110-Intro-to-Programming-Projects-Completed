"""Tests for linked list utils."""

import pytest
from exercises.ex10.linked_list import Node, last
from exercises.ex10.linked_list import value_at
from exercises.ex10.linked_list import max
from exercises.ex10.linked_list import linkify
from exercises.ex10.linked_list import scale

__author__ = "730466477"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(5, None)))
    assert last(linked_list) == 5


def test_value_at() -> None:
    """Use Case."""
    data = (Node(1, Node(2, Node(3, None))))
    assert value_at(data, 1) == 2


def test_value_at_2() -> None:
    """Edge Case."""
    with pytest.raises(IndexError):
        value_at((Node(1, Node(2, Node(3, None)))), 3)


def test_max() -> None:
    """Use Case."""
    test = (Node(50, Node(80, Node(120, None))))
    assert max(test) == 120


def test_max_2() -> None:
    """Edge Case."""
    with pytest.raises(ValueError):
        max(None)

def test_linkify() -> None:
    """Use Case."""
    test = [10, 20, 30, 40]
    assert linkify(test) == 10 -> 20 -> 30 -> 40 -> None


def test_linkify_1() -> None:
    test = []
    assert linkify(test) == None


def test_scale() -> None:
    """Use Case."""
    assert scale(linkify([10, 20, 30, 40]), 20) ==  200  -> 400 -> 600 -> 800 -> None


def test_scale_1() -> None:
    """Edge Case."""
    assert scale(None, 1) == None