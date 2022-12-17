from talon import Module, actions, imgui

class RelativeTextPosition:
    def __init__(self, words_left: int, characters_right: int, number_of_characters: int):
        self.words_left = words_left
        self.characters_right = characters_right
        self.number_of_characters = number_of_characters
    
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
                result.append(Correction(relative_text_position, text, homophone))
    return result

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
