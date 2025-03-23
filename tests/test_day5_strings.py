import exercises.day5_strings as strings

def test_count_letter_occurrences():
    assert strings.count_letter_occurrences("hello", "l") == 2

def test_is_palindrome():
    assert strings.is_palindrome("racecar") is True
    assert strings.is_palindrome("hello") is False

def test_count_vowels():
    assert strings.count_vowels("hello") == 2
    assert strings.count_vowels("xyz") == 0

def test_is_substring():
    assert strings.is_substring("hello", "ell") is True
    assert strings.is_substring("cat", "dog") is False

