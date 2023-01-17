from talon import Module, actions, imgui, Context
from .correction_rules import *

module = Module()
automatically_show_correction_menu = module.setting(
    'fire_chicken_automatically_show_correction_menu',
    type = int,
    default = 1,
    desc = 'Whether or not to automatically show the correction menu under certain circumstances. A value of 0 means false, and other values mean true.'
)

def should_automatically_show_correction_menu():
    return automatically_show_correction_menu.get() != 0

module.tag('fire_chicken_correction')
correction_context = Context()

def activate_correction_tag():
    global correction_context
    correction_context.tags = ['user.fire_chicken_correction']

def deactivate_correction_tag():
    global correction_context
    correction_context.tags = []

text_to_correct = ''
text_to_correct_override = ''
corrections = []
@module.action_class
class Actions:
    def fire_chicken_show_correction_menu():
        '''Used to automatically open the correction menu in certain contexts'''
        if should_automatically_show_correction_menu():
            show_correction_menu()
        
    def fire_chicken_show_correction_menu_manually():
        '''Used to manually open the correction menu'''
        show_correction_menu()
    
    def fire_chicken_hide_correction_menu():
        ''''''
        gui.hide()
        deactivate_correction_tag()
    
    def fire_chicken_make_correction(number: int):
        ''''''
        if number - 1 < len(corrections):
            correction = corrections[number - 1]
            position = correction.relative_position
            position.select_text()
            actions.insert(correction.replacement)
            update_text_to_correct_with_correction(correction)
    
    def fire_chicken_correct_word_left(number: int):
        ''''''
        actions.user.words_left(number - 1)
        actions.edit.extend_word_left()
        actions.user.fire_chicken_correct_selected_text()

    def fire_chicken_correct_word_right(number: int):
        ''''''
        actions.user.words_right(number - 1)
        actions.edit.extend_word_right()
        actions.user.fire_chicken_correct_selected_text()

    def fire_chicken_correct_line():
        ''''''
        actions.edit.select_line()
        actions.user.fire_chicken_correct_selected_text()

    def fire_chicken_correct_selected_text():
        ''''''
        selected_text: str = actions.user.fire_chicken_dictation_get_selected_text()
        actions.user.fire_chicken_override_correction_text(selected_text.strip())
        actions.user.fire_chicken_show_correction_menu_manually()
        actions.edit.right()
        
    def fire_chicken_override_correction_text(new_correction_text: str):
        ''''''
        global text_to_correct_override
        text_to_correct_override = new_correction_text

def show_correction_menu():
    gui.show()
    activate_correction_tag()

def update_text_to_correct_with_correction(correction: Correction):
    global text_to_correct
    position: RelativeTextPosition = correction.relative_position
    original_text_start, original_text_ending = position.find_position_coordinates_in_string(text_to_correct)
    correction_ending = original_text_ending
    text_to_correct = text_to_correct[:original_text_start] + correction.replacement + text_to_correct[correction_ending + 1:]
    global corrections
    corrections = compute_possible_corrections_for_text(text_to_correct)

last_phrase = ''
@imgui.open(y=0)
def gui(gui: imgui.GUI):
    new_phrase = actions.user.get_last_phrase()
    global last_phrase, text_to_correct, corrections, text_to_correct_override
    try:
        if new_phrase != last_phrase:
            last_phrase = new_phrase
            text_to_correct = last_phrase
            corrections = compute_possible_corrections_for_text(text_to_correct)
        if text_to_correct_override != '':
            text_to_correct = text_to_correct_override
            text_to_correct_override = ''
            corrections = compute_possible_corrections_for_text(text_to_correct)
    except Exception as exception:
        print('Correction system failure!')
        print(exception)
    gui.text("Correction Menu")
    gui.line()
    gui.text(text_to_correct)
    gui.line()
    for index, correction in enumerate(corrections, 1):
        gui.text(f'{index}: {correction.original} to {correction.replacement}')
