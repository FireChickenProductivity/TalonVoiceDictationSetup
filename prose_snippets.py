from talon import Context
from .user_settings import get_list_from_csv

context = Context()
context.matches = r'''
not mode: sleep
'''

_knausj_snippets = {
    "spacebar": " ",
    "new line": "\n",
    "new paragraph": "\n\n",
    # Curly quotes are used to obtain proper spacing for left and right quotes, but will later be straightened.
    "open quote": "“",
    "close quote": "”",
}

_default_additional_snippets = {
       #My additions
    'open paren': ' (',
    'open pren': ' (',
    'close paren': ')',
    'close pren': ')',
}

_snippets = get_list_from_csv(
    'additional_snippets.csv',
    headers = ('Snippet', 'Spoken Form'),
    default = _default_additional_snippets,

)

_snippets.update(_knausj_snippets)
context.lists['user.prose_snippets'] = _snippets
