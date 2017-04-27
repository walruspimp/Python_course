#!/usr/bin/env python
"""
In this exercise we will develop function to analyse the words in a text.
As an example we will use the play Hamlet by William Shakespeare. We already
loaded the Hamlet text for you. You just have to implement the functions 
below in order to analyse the text:
"""

# load the text of Hamlet into the variable hamlet
with open('data/hamlet.txt', 'r') as f:
    hamlet = f.read()

"""
How many words is Hamlet made of? Implement the function count_number_of_words, which counts
the number of words in a given text.
"""


def count_number_of_words(text):
    """ Counts the number of words (separated by white spaces or newlines) in a text """
    pass


"""
Next we would like to know which are the most common words used in the play. In order to do this,
we first have to do some pre-processing. One problem is that for a computer two words in different
capitalization (e.g. home and Home) are not the same. Therefore we will convert the whole play to
lower case characters.
"""


def convert_to_lowercase(text):
    pass


"""
Another problem for our computations punctuation and special characters in the text (. , - etc), which
have to be removed. Implement the following function doing this.
"""


def remove_punctuation(text):
    pass


"""
Next we can implement the function that counts occurrence of each word in a text. The function is supposed
to return a dictionary, in which each word is a key and the value is the number of occurrences of the word.
"""


from collections import Counter


def occurrence_of_words(text):
    pass


"""
We would like to know what are the most common words in Hamlet. Implement a function to find  the
N=10 most occurring words from the dictionary returned by occurrence_of_words. The function should return
a list in which each entry is a tuple consisting of the number of occurrences of the word and the word
(no_occurrences, word).
Hint: a dictionary cannot be sorted, convert the dictionary to a data-structure that can be sorted first.
"""


def get_most_occurring_words(count_dictionary, number=10):
    pass


"""
If you computed the most occurring words in Hamlet, you can see that the first words are stop words such as
the, and, or. For a word analysis to be interesting we have to remove these words. We have already loaded you
a list of these stop words below. Implement the function remove_forbidden_words, which removes all stop words
from a given text.
"""

# load a list of stop words
with open('data/stop_words.txt', 'r') as f:
    stop_words = f.read().split()


def remove_forbidden_words(text, forbidden):
    pass


"""
From here on unit tests.
Do not modify this code!
"""


def test_count_number_of_words():
    txt1 = 'Long live the king!'
    txt2 = 'Stay! speak, speak! I charge thee, speak! \n\nExit Ghost'
    txt3 = ''
    assert count_number_of_words(txt1) == 4
    assert count_number_of_words(txt2) == 9
    assert count_number_of_words(txt3) == 0


def test_convert_to_lowercase():
    txt1 = 'CAPITAL'
    txt2 = 'CaPiTal'
    assert convert_to_lowercase(txt1) == 'capital'
    assert convert_to_lowercase(txt2) == 'capital'


def test_remove_punctuation():
    txt1 = 'Long live the king!'
    txt2 = 'text without Punctuation'
    txt3 = '!?.:,.;'
    assert remove_punctuation(txt1) == 'Long live the king'
    assert remove_punctuation(txt2) == 'text without Punctuation'
    assert remove_punctuation(txt3) == ''


def test_occurrence_of_words():
    txt1 = 'stay speak speak i charge thee speak \n\nexit ghost'
    txt2 = ''
    txt3 = 'indeed i heard it not then it draws near the season'
    assert occurrence_of_words(txt1) == {'speak': 3, 'exit': 1, 'i': 1, 'charge': 1, 'stay': 1, 'thee': 1, 'ghost': 1}
    assert occurrence_of_words(txt2) == {}
    assert occurrence_of_words(txt3) == {'the': 1, 'it': 2, 'heard': 1, 'draws': 1, 'season': 1, 'indeed': 1, 'near': 1, 'then': 1, 'not': 1, 'i': 1}


def test_get_most_occurring_words():
     d1 = {'speak': 1, 'exit': 3, 'ghost': 2}
     d2 = {'the': 1, 'indeed': 1, 'near': 2, 'not':3}
     assert get_most_occurring_words(d1, number=3) ==  [(3, 'exit'), (2, 'ghost'), (1, 'speak')]
     assert get_most_occurring_words(d2, number=4) == [(3, 'not'), (2, 'near'), (1, 'the'), (1, 'indeed')]
     assert get_most_occurring_words(d2, number=10) == [(3, 'not'), (2, 'near'), (1, 'the'), (1, 'indeed')]


def test_remove_forbidden_words():
    forbidden = ['and', 'to', 'where']
    txt1 = 'and shall I couple hell'
    txt2 = 'what means, and where they keep'
    txt3 = 'and shall I couple hell and and'
    assert remove_forbidden_words(txt1, forbidden) == 'shall I couple hell'
    assert remove_forbidden_words(txt2, forbidden) == 'what means, they keep'
    assert remove_forbidden_words(txt3, forbidden) == 'shall I couple hell'


if __name__ == '__main__':
    from test_runner import run_tests
    run_tests()