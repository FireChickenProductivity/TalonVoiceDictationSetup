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
    def fire_chicken_dictation_enable_command_mode_from_dictation_mode():
        '''Enables command mode from dictation mode'''
        actions.mode.disable("dictation")
        actions.mode.enable("command")
