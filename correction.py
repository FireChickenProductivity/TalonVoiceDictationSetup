from talon import Module, actions, imgui

class RelativeTextPosition:
    def __init__(self, words_left: int, characters_right: int, number_of_characters: int):
        self.words_left = words_left
        self.characters_right = characters_right
        self.number_of_characters = number_of_characters
    
    def select_text(self):
        for i in range(self.words_left):
            actions.edit.word_left()
        for i in range(self.characters_right):
            actions.edit.right()
        for i in range(self.number_of_characters):
            actions.edit.extend_right()

    def __str__(self):
        return f'{self.characters_right} words left {self.characters_right} characters right {self.number_of_characters} characters'
    
    def __repr__(self):
        return self.__str__()


class Correction:
    def __init__(self, relative_position, original: str, replacement: str):
        self.relative_position = relative_position
        self.original = original
        self.replacement = replacement
    
    def __str__(self):
        return f'(Correction: "{self.original}" to "{self.replacement}" at {self.relative_position})'

    def __repr__(self):
        return self.__str__()

def compute_possible_corrections_for_substring(text: str, relative_text_position):
    result = []
    homophones = actions.user.homophones_get(text)
    if homophones != None:
        for homophone in homophones:
            if homophone != text:
                replacement_text: str = return_copy_of_string_with_same_capitalization_as(homophone, text)
                result.append(Correction(relative_text_position, text, replacement_text))
    return result

def return_copy_of_string_with_same_capitalization_as(original: str, text_with_target_capitalization: str) -> str:
    copy: str = original[:]
    if text_with_target_capitalization[0].isupper():
        copy = original[0].upper()
        if len(original) > 1:
            copy += original[1:]
    all_upper_case: bool = True
    all_lowercase: bool = True
    for character in text_with_target_capitalization:
        if character.isalpha():
            if character.isupper():
                all_lowercase = False
            else:
                all_upper_case = False
    if all_upper_case:
        copy = original.upper()
    if all_lowercase:
        copy = original.lower()
    return copy

def compute_possible_corrections_for_text(text: str):
    corrections = []
    words_left_for_index = compute_words_left_list(text)
    characters_right_for_index = compute_characters_right_list(text, words_left_for_index)
    for i in range(len(text)):
        for j in range(i, len(text)):
            position = RelativeTextPosition(words_left_for_index[i], characters_right_for_index[i], j - i + 1)
            corrections.extend(compute_possible_corrections_for_substring(text[i:j+1], position))
    return corrections

def compute_words_left_list(text: str):
    result = []
    last_character = ''
    words_left = 1
    text_without_trailing_spaces_to_the_right = text.rstrip()
    for i in range(len(text_without_trailing_spaces_to_the_right) - 1, -1, -1):
        character = text_without_trailing_spaces_to_the_right[i]
        if character == ' ' and last_character != ' ':
            words_left += 1
        last_character = character
        result.append(words_left)
    result.reverse()
    return result

def compute_characters_right_list(text: str, words_left_list):
    result = []
    characters_since_last_word = 0
    last_word_count = words_left_list[0] + 1
    for i in range(len(text)):
        if words_left_list[i] != last_word_count:
            last_word_count = words_left_list[i]
            characters_since_last_word = 0
        else:
            characters_since_last_word += 1
        result.append(characters_since_last_word)
    return result


module = Module()
@module.action_class
class Actions:
    def fire_chicken_show_correction_menu():
        ''''''
        gui.show()
    
    def fire_chicken_hide_correction_menu():
        ''''''
        gui.hide()
    
    def fire_chicken_make_correction(number: int):
        ''''''
        if number - 1 < len(corrections):
            correction = corrections[number - 1]
            position = correction.relative_position
            position.select_text()
            actions.insert(correction.replacement)


corrections = []
last_phrase = ''
@imgui.open(y=0)
def gui(gui: imgui.GUI):
    new_phrase = actions.user.get_last_phrase()
    global last_phrase
    global corrections
    if new_phrase != last_phrase:
        last_phrase = new_phrase
        corrections = compute_possible_corrections_for_text(last_phrase)
    gui.text("Correction Menu")
    gui.line()
    for index, correction in enumerate(corrections, 1):
        gui.text(f'{index}: {correction.original} to {correction.replacement}')
