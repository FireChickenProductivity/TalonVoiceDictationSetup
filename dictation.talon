mode: dictation
and not mode: command
-
<user.raw_prose>$: user.dictation_insert(raw_prose)
<user.word>: 
    sleep(0.1)
    user.dictation_insert(word)
<user.letter> <user.letter> <user.letters>:
    initial_letters = letter_1 + letter_2
    user.dictation_insert(initial_letters + letters)
ship <user.letter> <user.letter> <user.letters>:
    initial_letters = letter_1 + letter_2
    capital_letters = user.formatted_text(initial_letters + letters, "ALL_CAPS")
    user.dictation_insert(capital_letters)