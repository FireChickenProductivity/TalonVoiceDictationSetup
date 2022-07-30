mode: dictation
-
<number_small> clear:
    edit.delete()
    repeat(number_small - 1)
clear <number_small>:
    key('delete')
    repeat(number_small - 1)
<number_small> clear <number_small>:
    edit.delete()
    repeat(number_small_1 - 1)
    key('delete')
    repeat(number_small_2 - 1)

<number_small> (word|words) clear:
    edit.extend_word_left()
    repeat(number_small - 1)
    edit.delete()
clear <number_small> (word|words):
    edit.extend_word_right()
    repeat(number_small - 1)
    edit.delete()

word clear:
    edit.extend_word_left()
    edit.delete()
clear word:
    edit.extend_word_right()
    edit.delete()

word <number_small> clear:
    edit.word_left()
    repeat(number_small - 1)
    edit.extend_word_right()
    edit.delete()
clear word <number_small>:
    edit.word_right()
    repeat(number_small - 1)
    edit.extend_word_left()
    edit.delete()