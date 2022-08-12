mode: dictation
-
all caps <user.raw_prose>:
    auto_insert(user.formatted_text(raw_prose, 'all cap'))
title case <user.raw_prose>:
    auto_insert(user.formatted_text(raw_prose, 'title'))
form form <user.format_text>:
    user.dictation_insert_raw(format_text)
