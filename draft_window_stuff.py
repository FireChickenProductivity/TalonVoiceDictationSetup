from talon import Module, actions, clip

module = Module()

draft_submit_delay = module.setting(
    'fire_chicken_dictation_draft_submit_delay',
    type = int,
    default = 200,
    desc = 'How long to wait between closing the draft window and submitting the draft window draft in milliseconds', 
)

draft_paste_delay = module.setting(
    'fire_chicken_dictation_draft_paste_delay',
    type = int,
    default = 200,
    desc = 'How long to wait after pasting the draft window text to let the clipboard revert properly',
)

pre_anchor_move_delay = module.setting(
    'fire_chicken_dictation_pre_anchor_move_delay',
    type = int,
    default = 200,
    desc = 'How long to wait before moving to an anchor under certain circumstances to avoid bugs',
)

def sleep_draft_submit_delay():
    sleep_delay_setting_amount(draft_submit_delay)
def sleep_draft_paste_delay():
    sleep_delay_setting_amount(draft_paste_delay)
def sleep_pre_anchor_move_delay():
    sleep_delay_setting_amount(pre_anchor_move_delay)

def sleep_delay_setting_amount(setting):
    actions.sleep(f'{setting.get()}ms')

@module.action_class
class Actions:
    def fire_chicken_dictation_draft_submit():
        '''Submits the draft window draft using the delay setting'''
        content = actions.user.draft_get_text()
        actions.user.fire_chicken_dictation_close_draft()
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
    def fire_chicken_dictation_send_draft_text_with_keypress(keypress: str):
        '''Submits the draft window text, does the specified keypress, reopens the draft window, and then selects the text there'''
        actions.user.fire_chicken_dictation_draft_submit()
        actions.key(keypress)
        start_new_draft()
    def fire_chicken_dictation_send_draft_text_with_new_line_and_save():
        '''Submits the draft window text, starts a newline, saves, reopens the draft window, and then selects the text there'''
        actions.user.fire_chicken_dictation_draft_submit_with('\n')   
        actions.edit.save()
        start_new_draft()
    def fire_chicken_dictation_start_new_draft():
        '''Opens the draft window and selects all the text'''
        start_new_draft()
    def fire_chicken_draft_submit_through_pasting():
        '''Submits the draft window draft through pasting'''
        with clip.revert():
            content = actions.user.draft_get_text()
            clip.set_text(content)
            actions.user.draft_hide()
            sleep_draft_submit_delay()
            actions.edit.paste()
            sleep_draft_paste_delay()
    def fire_chicken_dictation_draft_edit_selected_text():
        '''Opens the draft window with the currently selected text'''
        selected_text: str = actions.edit.selected_text()
        actions.user.draft_show(selected_text)
    def fire_chicken_dictation_insert_draft_window_text():
        '''Types the draft window draft'''
        content = actions.user.draft_get_text()
        actions.insert(content)
    def fire_chicken_dictation_sleep_pre_anchor_move_delay():
        ''''''
        sleep_pre_anchor_move_delay()
    def fire_chicken_dictation_close_draft():
        ''''''
        close_draft()
    
def start_new_draft():
    open_draft()
    actions.edit.select_all()

def open_draft():
    actions.user.draft_hide()
    actions.user.draft_show()
    actions.user.fire_chicken_show_correction_menu()

def close_draft():
    actions.user.draft_hide()
    actions.user.fire_chicken_hide_correction_menu()

