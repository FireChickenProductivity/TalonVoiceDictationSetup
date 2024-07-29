mode: dictation
-
all caps <user.raw_prose>:
    auto_insert(user.formatted_text(raw_prose, 'ALL_CAPS'))
title case <user.raw_prose>:
    auto_insert(user.formatted_text(raw_prose, 'CAPITALIZE_ALL_WORDS'))
form form <user.format_text>:
    user.dictation_insert_raw(format_text)
word word <user.word>: user.insert_with_history(user.word)
press ship <user.letters>:
    user.insert_formatted(letters, "ALL_CAPS")
ship ship <user.letters>:
    result = user.formatted_text(letters, "ALL_CAPS")
    user.dictation_insert_raw(result)