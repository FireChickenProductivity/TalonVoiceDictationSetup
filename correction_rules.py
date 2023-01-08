from talon import resource, actions
import os
from pathlib import Path
import csv

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

    def find_position_coordinates_in_string(self, text: str):
        word_start: int = len(text) - 1
        for i in range(self.words_left):
            word_start = self._find_position_word_left(text, word_start)
        start: int = word_start + self.characters_right
        ending: int = start + self.number_of_characters - 1
        return start, ending

    def _find_position_word_left(self, text: str, current_index: int):
        non_space_character_encountered: bool = False
        first_character_is_space: bool = False
        first_character: str = text[current_index - 1]
        if first_character.isspace():
            first_character_is_space = True
        else:
            non_space_character_encountered = True

        for index in range(current_index - 1, 0, -1):
            character: str = text[index - 1]
            if character.isspace():
                if first_character_is_space:
                    if non_space_character_encountered:
                        return index
                else:
                    return index
            else:
                non_space_character_encountered = True
        return 0

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
    
STANDARD_CASING = ''
EXACT_CASING = 'exact'

class SimpleCorrectionRule:
    def __init__(self, original: str, replacement: str, case_override: str):
        self.original = original
        self.replacement = replacement
        self.case_override = case_override
    
    @staticmethod
    def make_from_row(row):
        original: str = row[0].lower()
        replacement: str = row[1]
        case_override: str = STANDARD_CASING
        if len(row) > 2:
            case_override = row[2]
        rule = SimpleCorrectionRule(original, replacement, case_override)
        return rule
    
    def get_original(self):
        return self.original
    
    def get_replacement(self):
        return self.replacement
    
    def compute_correction(self, relative_position, text: str) -> Correction:
        replacement = self.get_replacement()
        if self.case_override == STANDARD_CASING:
            replacement = return_copy_of_string_with_same_capitalization_as(replacement, text)
        correction = Correction(relative_position, self.get_original(), replacement)
        return correction
    
    def __str__(self) -> str:
        return f'(SimpleCorrectionRule: "{self.original}" to "{self.replacement}" with casing "{self.case_override}")'
    
    def __repr__(self) -> str:
        return self.__str__()

def get_correction_file_names():
    correction_directory = Path(__file__).parents[0] / "correction_data"
    relative_names = os.listdir(correction_directory)
    absolute_names = []
    for name in relative_names:
        absolute_names.append(os.path.join(correction_directory, name))
    return absolute_names

class SimpleCorrectionRules:
    def __init__(self):
        self.rules = {}
        file_names = get_correction_file_names()
        for file in file_names:
            self.add_rules_from_file(file)
    
    def add_rules_from_file(self, name):
        with resource.open(str(name), "r") as file:
            reader = csv.reader(file)
            for row in reader:
                self.add_rule_from_row(row)
            
    def add_rule_from_row(self, row):
        rule: SimpleCorrectionRule = SimpleCorrectionRule.make_from_row(row)
        if self.is_rule_new(rule):
            if rule.get_original() not in self.rules:
                self.rules[rule.get_original()] = []
            self.rules[rule.get_original()].append(rule)

    def is_rule_new(self, rule: SimpleCorrectionRule):
        if rule.get_original() not in self.rules:
            return True
        for existing_rule in self.rules[rule.get_original()]:
            if existing_rule.get_replacement() == rule.get_replacement():
                return False
        return True
    
    def compute_corrections_for_text(self, text: str, relative_text_position):
        corrections = []
        lower_case_text: str = text.lower()
        if lower_case_text in self.rules:
            for rule in self.rules[lower_case_text]:
                correction = rule.compute_correction(relative_text_position, text)
                corrections.append(correction)
        return corrections

        
def compute_possible_corrections_for_substring(text: str, relative_text_position):
    result = []
    homophones = actions.user.homophones_get(text)
    if homophones != None and len(text) > 1:
        for homophone in homophones:
            if homophone != text:
                replacement_text: str = return_copy_of_string_with_same_capitalization_as(homophone, text)
                result.append(Correction(relative_text_position, text, replacement_text))
    simple_corrections = simple_correction_rules.compute_corrections_for_text(text, relative_text_position)
    if len(simple_corrections) > 0:
        result.extend(simple_corrections)
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
simple_correction_rules: SimpleCorrectionRules = SimpleCorrectionRules()
