from ..correction import *
from talon import app

def assert_can_compute_word_left_correctly_for(text: str, expected):
    actual = compute_words_left_list(text)
    assert actual == expected, f'Expected word left for {text} to be {expected} but received {actual}!'

def can_compute_words_left_for_single_word():
    expected = [1, 1, 1, 1]
    text = 'word'
    assert_can_compute_word_left_correctly_for(text, expected)

def can_compute_words_left_for_two_words():
    expected = [2, 2, 2, 2, 2, 1, 1, 1, 1]
    text = 'word word'
    assert_can_compute_word_left_correctly_for(text, expected)

def can_compute_words_left_can_handle_multiple_consecutive_spaces():
    expected = [2, 2, 2, 2, 2, 2, 1, 1, 1, 1]
    text = 'word  word'
    assert_can_compute_word_left_correctly_for(text, expected)

def assert_can_compute_characters_right_correctly_for(text: str, expected):
    words_left_list = compute_words_left_list(text)
    actual = compute_characters_right_list(text, words_left_list)
    assert actual == expected, f'Expected characters right for {text} to be {expected} but received {actual}!'

def can_compute_characters_right_correctly_for_single_word():
    expected = [0, 1, 2, 3]
    text = 'word'
    assert_can_compute_characters_right_correctly_for(text, expected)

def can_compute_characters_right_correctly_for_two_words():
    expected = [0, 1, 2, 3, 4, 0, 1, 2, 3]
    text = 'word word'
    assert_can_compute_characters_right_correctly_for(text, expected)

def corrections_match(corrections1, corrections2):
    if len(corrections1) != len(corrections2):
        return False
    for i in range(len(corrections1)):
        if not correction_matches(corrections1[i], corrections2[i]):
            return False
    return True

def correction_matches(correction1: Correction, correction2: Correction):
    return str(correction1) == str(correction2)

def assert_compute_possible_corrections_for_sub_string_correctly_handles(text: str, position: RelativeTextPosition, expected):
    corrections = compute_possible_corrections_for_substring(text, position)
    assert corrections_match(corrections, expected), f'With text {text} expected \n{expected} \nbut received \n{corrections}!'

def can_compute_possible_corrections_for_sub_string_handle_to():
    position = RelativeTextPosition([1, 1], [0, 1], 2)
    original = 'to'
    expected = [Correction(position, original, 'too'), Correction(position, original, 'two')]
    assert_compute_possible_corrections_for_sub_string_correctly_handles('to', position, expected)
    

def assert_find_position_word_left_correctly_handles(text: str, current_index: int, expected: int):
    position: RelativeTextPosition = RelativeTextPosition(0, 0, 0)
    actual = position._find_position_word_left(text, current_index)
    assert actual == expected, f'Expected word left to be {expected} and not {actual}'

def can_find_word_left_position_for_word_characters_after_space():
    text = 'word word'
    expected = 5
    for starting_index in range(6, 9):
        assert_find_position_word_left_correctly_handles(text, starting_index, expected)

def can_find_word_left_position_for_word_characters_after_multiple_spaces():
    text = 'word  \t \n word'
    expected = 10
    for starting_index in range(11, 14):
        assert_find_position_word_left_correctly_handles(text, starting_index, expected)
    

def can_find_word_left_position_for_space_characters_after_word():
    text = 'word word  \t \n'
    expected = 5
    for starting_index in range(10, 14):
        assert_find_position_word_left_correctly_handles(text, starting_index, expected)

def can_find_word_left_position_for_first_word():
    text = 'word \t \n'
    expected = 0
    for starting_index in range(len(text)):
        assert_find_position_word_left_correctly_handles(text, starting_index, expected)

def run_tests():
    can_compute_words_left_for_single_word()
    can_compute_words_left_for_two_words()
    can_compute_words_left_can_handle_multiple_consecutive_spaces()
    can_compute_characters_right_correctly_for_single_word()
    can_compute_characters_right_correctly_for_two_words()
    can_compute_possible_corrections_for_sub_string_handle_to()
    can_find_word_left_position_for_word_characters_after_space()
    can_find_word_left_position_for_word_characters_after_multiple_spaces()
    can_find_word_left_position_for_space_characters_after_word()
    can_find_word_left_position_for_first_word()

app.register('ready', run_tests)