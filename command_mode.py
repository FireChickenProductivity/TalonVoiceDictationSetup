from talon import actions, Module

module = Module()

@module.action_class
class Actions:
    def fire_chicken_dictation_enable_dictation_mode_from_command_mode():
        '''Enables dictation mode from command mode mimicking the knausj dictation mode command'''
        actions.mode.disable("command")
        actions.mode.enable("dictation")
        actions.user.code_clear_language_mode()
        actions.mode.disable("user.gdb")