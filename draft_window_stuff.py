from talon import Module, actions

module = Module()

draft_submit_delay = module.setting(
    'fire_chicken_dictation_draft_submit_delay',
    type = int,
    default = 200,
    desc = 'How long to wait between closing the draft window and submitting the draft window draft in milliseconds', 
)

def sleep_draft_submit_delay():
    actions.sleep(f'{draft_submit_delay.get()}ms')

@module.action_class
class Actions:
    def fire_chicken_dictation_draft_submit():
        '''Submits the draft window draft using the delay setting'''
        content = actions.user.draft_get_text()
        actions.user.draft_hide()
        sleep_draft_submit_delay()
        actions.insert(content)
    def fire_chicken_dictation_draft_submit_with(ending: str):
        '''Submits the draft window using the delay setting and inserts the ending text'''
        actions.user.fire_chicken_dictation_draft_submit()
        actions.insert(ending)
    def fire_chicken_dictation_send_draft_text_with_ending(ending: str):
        '''Submits the draft window text alongside the ending text, reopens the draft window, and then selects the text there'''
        actions.user.fire_chicken_dictation_draft_submit_with(ending)
        start_new_draft()
    def fire_chicken_dictation_start_new_draft():
        '''Opens the draft window and selects all the text'''
        start_new_draft()
    
def start_new_draft():
    open_draft()
    actions.edit.select_all()

def open_draft():
    actions.user.draft_hide()
    actions.user.draft_show()

