mode: dictation
and not mode: user.exam_mode
-
#Standard knausj recent list commands with different ways of saying them
recent recent: user.toggle_phrase_history()
(repeat repeat|peat peat) <number_small>: user.insert_with_history(user.get_recent_phrase(number_small))
recent recent copy <number_small>: clip.set_text(user.get_recent_phrase(number_small))