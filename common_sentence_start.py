from talon import Module, actions, Context

module = Module()
module.tag('fire_chicken_common_sentence_start', desc = 'Allows commands that switch to dictation drafting when saying a common sentence start')
module.list('fire_chicken_dictation_common_sentence_start', desc = 'Words commonly used to start a sentence')

context = Context()
context.lists['user.fire_chicken_dictation_common_sentence_start'] = {
    'I': 'I',
    'This': 'This',
    'That': 'That',
    'Is': 'Is',
    'The': 'The',
    'We': 'We',
    'Why': 'Why',
    'Would': 'Would',
    'Will': 'Will',
    'If': 'If',
    'Does': 'Does',
    'Do': 'Do',
    'When': 'When',
    'Could': 'Could',
    'A': 'A',
    'An': 'An',
    'How': 'How',
    'My': 'My',
    'It': 'It',
    'You': 'You',
    'Because': 'Because',
    'Nonetheless': 'Nonetheless',
    'Unless': 'Unless',
    'As': 'As',
    'He': 'He',
    'She': 'She',
    'They': 'They',
    'My': 'My',
    'His': 'His',
    'Her': 'Her',
}

@module.capture(rule = '{user.fire_chicken_dictation_common_sentence_start}')
def fire_chicken_dictation_common_sentence_start(m) -> str:
    return m.fire_chicken_dictation_common_sentence_start

@module.action_class
class Actions:
    def fire_chicken_dictation_launch_dictation_drafting_with_common_sentence_start(start: str, additional_text: str):
        '''Switches to dictation mode drafting and inserts the specified text'''
        actions.user.fire_chicken_enable_dictation_mode_and_draft_window_from_command_mode()
        actions.user.dictation_insert(start)
        actions.user.dictation_insert(additional_text)

