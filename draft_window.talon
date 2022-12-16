# These are active when we have focus on the draft window
title:Talon Draft
and mode: dictation
-
settings():
  # Enable 'Smart dictation mode', see https://github.com/knausj85/knausj_talon/pull/356
  user.context_sensitive_dictation = 1

# Replace a single word with a phrase
replace <user.draft_anchor> with <user.text>:
  user.draft_select("{draft_anchor}")
  result = user.formatted_text(text, "NOOP")
  insert(result)

# Position cursor before word
(pre | cursor | cursor before) <user.draft_anchor>:
  user.draft_position_caret("{draft_anchor}")

pre pre <number_small> <user.draft_anchor>:
  user.draft_position_caret("{draft_anchor}")
  edit.right()
  repeat(number_small - 1)

# Position cursor after word
(post | cursor after) <user.draft_anchor>:
  user.draft_position_caret("{draft_anchor}", 1)

post post <number_small> <user.draft_anchor>:
  user.draft_position_caret("{draft_anchor}", 1)
  edit.left()
  repeat(number_small - 1)

trim trim <user.draft_anchor>:
  user.draft_position_caret("{draft_anchor}", 1)
  key(backspace)

trim trim <number_small> <user.draft_anchor>:
  user.draft_position_caret("{draft_anchor}", 1)
  key(backspace)
  repeat(number_small - 1)

# Select a whole word
(take | select) <user.draft_anchor>:
  user.draft_select("{draft_anchor}")

^(phone phone|fun fun) <user.draft_anchor>$:
  user.draft_select("{draft_anchor}")
  user.homophones_show_selection()

^(phone phone|fun fun) hide$:
  user.homophones_hide()

bring bring <user.draft_anchor>:
  original_position = user.fire_chicken_draft_window_compute_position()
  user.fire_chicken_dictation_sleep_pre_anchor_move_delay()
  user.draft_select("{draft_anchor}")
  text = user.fire_chicken_dictation_get_selected_text()
  user.fire_chicken_draft_window_go_to_position(original_position)
  insert(' ' + text)
  

bring bring <user.draft_anchor> (through | past) <user.draft_anchor>:
  original_position = user.fire_chicken_draft_window_compute_position()
  user.fire_chicken_dictation_sleep_pre_anchor_move_delay()
  user.draft_select("{draft_anchor_1}", "{draft_anchor_2}")
  text = user.fire_chicken_dictation_get_selected_text()
  user.fire_chicken_draft_window_go_to_position(original_position)
  insert(' ' + text)

# Select a range of words
(take | select) <user.draft_anchor> (through | past) <user.draft_anchor>:
  user.draft_select("{draft_anchor_1}", "{draft_anchor_2}")

# Delete a word
(change | clear) <user.draft_anchor>:
  user.draft_select("{draft_anchor}", "", 1)
  key(backspace)

chuck <user.draft_anchor>:
  user.fire_chicken_draft_window_clear_draft_window_anchors_and_return_to_original_position("{draft_anchor}")

# Delete a range of words
(change | clear) <user.draft_anchor> (through | past) <user.draft_anchor>:
  user.draft_select(draft_anchor_1, draft_anchor_2, 1)
  key(backspace)

chuck <user.draft_anchor> (through | past) <user.draft_anchor>:
  user.fire_chicken_draft_window_clear_draft_window_anchors_and_return_to_original_position(draft_anchor_1, draft_anchor_2)

# reformat word
<user.formatters> word <user.draft_anchor>:
  user.draft_select("{draft_anchor}", "", 1)
  user.formatters_reformat_selection(user.formatters)

# reformat range
<user.formatters> <user.draft_anchor> (through | past) <user.draft_anchor>:
    user.draft_select(draft_anchor_1, draft_anchor_2, 1)
    user.formatters_reformat_selection(user.formatters)

