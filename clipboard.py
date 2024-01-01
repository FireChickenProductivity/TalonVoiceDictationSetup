from talon import Module, actions, clip, settings

module = Module()

clipboard_operation_delay_setting_name = 'fire_chicken_dictation_clipboard_operation_delay'
clipboard_operation_delay = 'user.' + clipboard_operation_delay_setting_name
module.setting(
    clipboard_operation_delay_setting_name,
    type = int,
    default = 200,
    desc = 'How long dictation commands should pause when doing copying and pasting'
)

@module.action_class
class Actions:
   def fire_chicken_dictation_get_selected_text() -> str:
        '''Obtains the selected text through the clipboard'''
        with clip.revert():
            actions.edit.copy()
            wait_long_enough_to_let_clipboard_revert_properly()
            result = clip.text()
        return result


def wait_long_enough_to_let_clipboard_revert_properly():
	actions.sleep(f'{settings.get(clipboard_operation_delay)}ms')