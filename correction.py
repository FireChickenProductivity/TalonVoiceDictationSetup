from talon import Module, actions, imgui
from .correction_rules import *

text_to_correct = ''
corrections = []
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
            update_text_to_correct(correction)
            
def update_text_to_correct(correction: Correction):
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
    global last_phrase
    global text_to_correct
    global corrections
    if new_phrase != last_phrase:
        last_phrase = new_phrase
        text_to_correct = last_phrase
        corrections = compute_possible_corrections_for_text(text_to_correct)
    gui.text("Correction Menu")
    gui.line()
    gui.text(text_to_correct)
    gui.line()
    for index, correction in enumerate(corrections, 1):
        gui.text(f'{index}: {correction.original} to {correction.replacement}')
