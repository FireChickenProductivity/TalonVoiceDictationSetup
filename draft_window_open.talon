# These are available when the draft window is open, but not necessarily focussed
tag: user.draft_window_showing
and mode: dictation
-
draft hide: user.draft_hide()

draft submit:
  user.fire_chicken_dictation_draft_submit()
  # user.paste may be somewhat faster, but seems to be unreliable on MacOSX, see
  # https://github.com/talonvoice/talon/issues/254#issuecomment-789355238
  # user.paste(content)

push space: user.fire_chicken_dictation_send_draft_text_with_ending(' ')
push sentence: user.fire_chicken_dictation_send_draft_text_with_ending('. ')
push line: user.fire_chicken_dictation_send_draft_text_with_ending('\n')
push question: user.fire_chicken_dictation_send_draft_text_with_ending('? ')
push (exclaim|exclamation [(point|mark)]): user.fire_chicken_dictation_send_draft_text_with_ending('! ')
push (Para|paragraph|pair): user.fire_chicken_dictation_send_draft_text_with_ending('\n\t')
push sentence (Para|paragraph|pair): user.fire_chicken_dictation_send_draft_text_with_ending('.\n\t')

push (last|finished|done|finish|push):
  user.fire_chicken_dictation_draft_submit()
  user.fire_chicken_dictation_enable_command_mode_from_dictation_mode()

paste paste: 
  user.fire_chicken_draft_submit_through_pasting()
  user.fire_chicken_dictation_enable_command_mode_from_dictation_mode()

discard discard:
  user.draft_hide()
  user.fire_chicken_dictation_enable_command_mode_from_dictation_mode()
