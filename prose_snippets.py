from talon import Context

context = Context()
context.matches = r'''
not mode: sleep
'''

context.lists['user.prose_snippets'] = {
    "spacebar": " ",
    "new line": "\n",
    "new paragraph": "\n\n",
    # Curly quotes are used to obtain proper spacing for left and right quotes, but will later be straightened.
    "open quote": "“",
    "close quote": "”",
    #My additions
    'open paren': ' (',
    'open pren': ' (',
    'close paren': ')',
    'close pren': ')',
}
