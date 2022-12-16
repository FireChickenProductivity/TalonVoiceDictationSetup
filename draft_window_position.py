from talon import Module, actions

module = Module()
@module.action_class
class Actions:
    def fire_chicken_draft_window_compute_position() -> int:
        ''''''
        actions.edit.extend_line_start()
        selected_text = actions.user.fire_chicken_dictation_get_selected_text()
        actions.edit.right()
        position = len(selected_text.split(' ')) + 1
        return position
    
    def fire_chicken_draft_window_go_to_position(position: int):
        ''''''
        actions.edit.extend_line_start()
        if position > 0:
            for i in range(position - 1):
                actions.edit.word_right()

    def fire_chicken_draft_window_clear_draft_window_anchors_and_return_to_original_position(start_anchor: str, ending_anchor: str = ''):
        ''''''
        original_position = actions.user.fire_chicken_draft_window_compute_position()
        actions.user.fire_chicken_dictation_sleep_pre_anchor_move_delay()
        actions.user.draft_select(start_anchor, ending_anchor, 1)
        number_of_selected_words = compute_number_of_selected_words()
        actions.key('backspace')
        number_of_words_from_beginning = compute_number_of_selected_words_from_beginning()
        actions.edit.line_start()
        if deleted_text_before_original_position(original_position, number_of_selected_words, number_of_words_from_beginning):
            actions.user.fire_chicken_draft_window_go_to_position(original_position - number_of_selected_words)
        else:
            actions.user.fire_chicken_draft_window_go_to_position(original_position)

def compute_number_of_selected_words():
    selected_text = actions.user.fire_chicken_dictation_get_selected_text()
    selected_text_without_trailing_spaces = selected_text.strip()
    number_of_words = selected_text_without_trailing_spaces.count(' ') + 1
    print(f'number_of_words: {number_of_words}')
    return number_of_words

def compute_number_of_selected_words_from_beginning():
    actions.edit.extend_line_start()
    number_of_words = compute_number_of_selected_words()
    return number_of_words

def deleted_text_before_original_position(original_position, number_of_deleted_words, number_of_words_from_beginning_after_deletion):
    return number_of_words_from_beginning_after_deletion + number_of_deleted_words < original_position
