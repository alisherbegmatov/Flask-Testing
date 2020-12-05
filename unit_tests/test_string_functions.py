import pytest

from string_functions import *

def test_greeting_jeremy():
    """Test for greet_by_name"""
    # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

    # Step 2: Decide what the expected outcome is for the scenario
    expected = 'Hello, Jeremy!'

    # Step 3: Call the function being tested to get its actual output
    actual = greet_by_name('Jeremy')

    # Step 4: Compare expected & actual outcomes. If they match, the test passes
    assert actual == expected

def test_greeting_dani():
    """Test for greet_by_name"""
    expected = 'Hello, Dani!'
    actual = greet_by_name('Dani')
    assert actual == expected

def test_reverse_long():
    """Test reversing a long string."""
    expected = 'Meredith'
    actual = reverse('htidereM')
    assert actual == expected

def test_reverse_short():
    """Test reversing a short string."""
    expected = 'Murphy'
    actual = reverse('yhpruM')
    assert actual == expected

def test_reverse_words_long():
    """Test reversing words in a long string."""
    expected = '?uoy era woH !yeH'
    actual = reverse_worlds('Hey! How are you?')
    assert actual == expected

def test_reverse_words_short():
    """Test reversing words in a short string."""
    expected = '!llew gniod uoy epoh I'
    actual = reverse_worlds('I hope you doing well!')
    assert actual == expected

def test_sarcastic_long():
    """Test sarcastic-ifying a long string."""
    expected = 'ReTuRnS tHe SaRcAsTiC vErSiOn Of A sTrInG'
    actual = sarcastic('Returns the sarcastic version of a string')
    assert actual == expected

def test_sarcastic_short():
    """Test sarcastic-ifying a short string."""
    expected = 'Yeah?'
    actual = ('Yeah?')
    assert actual == expected

def find_longest_word():
    with pytest.raises(Exception):
        expected = 'Bug'
        actual = sarcastic('Bug')
        assert actual == expected

# run the tests
if __name__ == '__main__':
    unittest.main()
