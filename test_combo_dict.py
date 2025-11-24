import pytest
from combo_dict import combine_dicts

def test_simple_merge():
    assert combine_dicts({"a": 1}, {"b": 2}) == {"a": 1, "b": 2}

def test_overlapping_keys():
    assert combine_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) == {"a": 1, "b": 3, "c": 4}

def test_empty_first():
    assert combine_dicts({}, {"x": 5}) == {"x": 5}

def test_both_empty():
    assert combine_dicts({}, {}) == {}

def test_order_preserved():
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    result = combine_dicts(d1, d2)
    assert list(result.keys()) == ["a", "b", "c", "d"]

def test_order_with_overlap():
    d1 = {"a": 1, "b": 2, "c": 3}
    d2 = {"b": 99, "d": 4}
    result = combine_dicts(d1, d2)
    # 'b' остаётся на позиции из d1, но значение берётся из d2
    assert list(result.keys()) == ["a", "b", "c", "d"]
    assert result["b"] == 99