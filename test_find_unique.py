import pytest
from find_unique import find_unique

def test_all_unique():
    assert find_unique([1, 2, 3]) == [1, 2, 3]

def test_no_unique():
    assert find_unique([1, 1, 2, 2]) == []

def test_some_unique():
    assert find_unique([1, 2, 2, 3, 4, 4]) == [1, 3]

def test_empty_list():
    assert find_unique([]) == []

def test_single_element():
    assert find_unique([42]) == [42]

def test_strings():
    assert find_unique(["a", "b", "a"]) == ["b"]

