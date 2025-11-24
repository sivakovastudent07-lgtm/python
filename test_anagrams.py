import pytest
from anagrams import are_anagrams

def test_simple_anagrams():
    assert are_anagrams("listen", "silent") is True

def test_not_anagrams():
    assert are_anagrams("hello", "world") is False

def test_same_string():
    assert are_anagrams("abc", "abc") is True

def test_different_lengths():
    assert are_anagrams("abc", "ab") is False

def test_empty_strings():
    assert are_anagrams("", "") is True

def test_with_repeated_letters():
    assert are_anagrams("aabbcc", "abcabc") is True

def test_non_anagram_same_letters_different_counts():
    assert are_anagrams("aab", "abb") is False