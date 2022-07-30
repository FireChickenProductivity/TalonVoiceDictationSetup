mode: dictation
-
go up <number_small>:
    edit.up()
    repeat(number_small - 1)
go down <number_small>:
    edit.down()
    repeat(number_small - 1)
go left <number_small>:
    edit.left()
    repeat(number_small - 1)
go right <number_small>:
    edit.right()
    repeat(number_small - 1)

left <number_small> (word|words):
    edit.word_left()
    repeat(number_small - 1)
right <number_small> (word|words):
    edit.word_right()
    repeat(number_small - 1)

select left <number_small>:
    edit.extend_left()
    repeat(number_small - 1)
select right <number_small>:
    edit.extend_right()
    repeat(number_small - 1)
select up <number_small> [line|lines]:
    edit.extend_up()
    repeat(number_small - 1)
select down <number_small> [line|lines]:
    edit.extend_down()
    repeat(number_small - 1)