mode: command
-
^(dictate|drafting)$:
    user.fire_chicken_enable_dictation_mode_and_draft_window_from_command_mode()

^(dictate|drafting) <user.raw_prose>:
    user.fire_chicken_enable_dictation_mode_and_draft_window_from_command_mode()
    user.dictation_insert(raw_prose)
