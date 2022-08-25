mode: dictation
-
(go up|up up) <number_small>:
    edit.up()
    repeat(number_small - 1)
(go down|down down) <number_small>:
    edit.down()
    repeat(number_small - 1)
(go left|left left) <number_small>:
    edit.left()
    repeat(number_small - 1)
(go right|right right) <number_small>:
    edit.right()
    repeat(number_small - 1)

up up: edit.up()
down down: edit.down()
left left: edit.left()
right right: edit.right()

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
