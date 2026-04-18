import pytest

def format_name(name):
    first, last = name.split()
    return f"{last}, {first}"

def test_format_name():
    assert format_name("John Doe") == "Doe, John"
    assert format_name("Jane Smith") == "Smith, Jane"
    assert format_name("Alice Johnson") == "Johnson, Alice"

def test_format_name_empty_string():
    with pytest.raises(ValueError):
        format_name("")

def test_format_name_single_word():
    with pytest.raises(ValueError):
        format_name("John")

def test_format_name_multiple_words():
    with pytest.raises(ValueError):
        format_name("John Doe Smith")
