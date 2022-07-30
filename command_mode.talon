mode: command
-
^(dictate|drafting) [this|here]$:
    user.fire_chicken_dictation_enable_dictation_mode_from_command_mode()
    user.fire_chicken_dictation_start_new_draft()