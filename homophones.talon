mode: dictation
-
#These are the standard knauj homophone commands with different ways of saying them

phone phone <user.homophones_canonical>: user.homophones_show(homophones_canonical)
phone phone that: user.homophones_show_selection()
phone phone force <user.homophones_canonical>: user.homophones_force_show(homophones_canonical)
phone phone force: user.homophones_force_show_selection()
hide hide phone | hide phone phone: user.homophones_hide()
phone phone word:
  edit.select_word()
  user.homophones_show_selection()
phone phone [<user.ordinals>] word left:
  n = ordinals or 1
  user.words_left(n - 1)
  edit.extend_word_left()
  user.homophones_show_selection()
phone phone [<user.ordinals>] word right:
  n = ordinals or 1
  user.words_right(n - 1)
  edit.extend_word_right()
  user.homophones_show_selection()