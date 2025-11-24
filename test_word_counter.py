import pytest
from word_counter import count_words

def test_empty_string():
    assert count_words("") == 0

def test_only_spaces():
    assert count_words("   ") == 0

def test_normal_sentence():
    assert count_words("hello world") == 2

def test_single_word():
    assert count_words("python") == 1

def test_leading_and_trailing_spaces():
    assert count_words("  hello world  ") == 2

def test_multiple_spaces_between_words():
    assert count_words("one  two   three") == 3