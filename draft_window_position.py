from talon import Module, actions

module = Module()
@module.action_class
class Actions:
    def fire_chicken_draft_window_compute_position() -> int:
        ''''''
        actions.edit.extend_line_start()
        selected_text = actions.user.fire_chicken_dictation_get_selected_text()
        actions.edit.right()
        position = len(selected_text)
        print(selected_text)
        return position
    
    def fire_chicken_draft_window_go_to_position(position: int):
        ''''''
        actions.user.file_start()
        if position > 0:
            for i in range(position - 1):
                actions.edit.right()


