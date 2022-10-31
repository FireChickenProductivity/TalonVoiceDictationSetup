from talon import Context, Module

module = Module()
module.tag('fire_chicken_override_numbers', desc = 'Override dictation numbers')
module.list('fire_chicken_dictation_number_prefix', desc = 'Ways to start a number in dictation mode')

context = Context()
context.matches = r'''
tag: user.fire_chicken_override_numbers
'''
context.lists['user.fire_chicken_dictation_number_prefix'] = {
    'numeral': 'numeral',
    'numb': 'numb',
}

#The following code is largely taken from the knausj_talon configuration

@context.capture(rule="{user.fire_chicken_dictation_number_prefix} <user.number_string>")
def prose_simple_number(m) -> str:
    return m.number_string


@context.capture(rule="{user.fire_chicken_dictation_number_prefix} <user.number_string> (dot | point) <digit_string>")
def prose_number_with_dot(m) -> str:
    return m.number_string + "." + m.digit_string


@context.capture(rule="{user.fire_chicken_dictation_number_prefix} <user.number_string> colon <user.number_string>")
def prose_number_with_colon(m) -> str:
    return m.number_string_1 + ":" + m.number_string_2

