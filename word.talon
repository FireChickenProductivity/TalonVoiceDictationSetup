app: Microsoft Word
-
settings():
  # Enable 'Smart dictation mode', see https://github.com/knausj85/knausj_talon/pull/356
  user.context_sensitive_dictation = 1

draft paragraph:
    key(ctrl-down)
    key(ctrl-shift-up)
    user.fire_chicken_enable_dictation_mode_editing_of_selected_text_through_draft_window_from_command_mode()

pause:
    key(alt-tab)
    sleep(0.5)
    key(space)
    sleep(0.5)
    key(alt-tab) 

change down:
    key(alt-tab)
    sleep(0.5)
    key(pagedown)
    sleep(0.5)
    key(alt-tab)

    