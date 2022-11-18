mode: command
-
^(dictate|drafting)$:
    user.fire_chicken_enable_dictation_mode_and_draft_window_from_command_mode()

^(dictate|drafting) <user.raw_prose>$:
    user.fire_chicken_enable_dictation_mode_and_draft_window_from_command_mode()
    user.dictation_insert(raw_prose)

^draft this$:
    user.fire_chicken_enable_dictation_mode_editing_of_selected_text_through_draft_window_from_command_mode()

^draft line$:
    edit.select_line()
    user.fire_chicken_enable_dictation_mode_editing_of_selected_text_through_draft_window_from_command_mode()

^<user.fire_chicken_dictation_common_sentence_start> <user.raw_prose>$:
    user.fire_chicken_dictation_launch_dictation_drafting_with_common_sentence_start(fire_chicken_dictation_common_sentence_start, raw_prose)
