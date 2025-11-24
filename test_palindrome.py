import pytest
from is_palindrome import is_palindrome

def test_palindrome_word():
    assert is_palindrome("radar") is True

def test_ne_palindrome_word():
    assert is_palindrome("hello") is False

def test_palindrome_number():
    assert is_palindrome(121) is True

def test_ne_palindrome_number():
    assert is_palindrome(123) is False

def test_single_character():
    assert is_palindrome("a") is True
    assert is_palindrome(5) is True

def test_empty_string():
    assert is_palindrome("") is True

def test_palindrome_with_digits_and_letters():
    assert is_palindrome("a1a") is True
    assert is_palindrome("a1b") is False