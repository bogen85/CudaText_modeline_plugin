# CudaText: lexer_file=Python; tab_size=4; tab_spaces=Yes; newline=LF;

import os
from cudatext import *
from http import cookies

MODE_KEY = " CudaText: "
MODE_KEY_LEN = len(MODE_KEY)
MODE_LABEL = MODE_KEY.strip()
MAX_READ_LINES = 5

def mode_message(e):
    print(f'{__name__}: {MODE_LABEL} {e.strip()}')

def to_bool(x0):
    x = x0.lower()
    if x in ("on", "yes", "1", "true", "enable", "enabled"):
        return (True, True)
    if x in ("off", "no", "0", "false", "disable", "disabled"):
        return (True, False)
    mode_message(f'bool value {x0} not understood')
    return (False, False)

def to_pos_int(x0):
    if x0.isdigit():
        return (True, int(x0))
    mode_message(f'{x0} is not a valid positive integer')
    return (False, 0)

def newline_prop(x0):
    x = x0.lower()
    if x in ("lf", "crlf", "cr"):
        return (True, x)
    mode_message(f'Newline value {x0} not understood')
    return (False, "")

def to_string(x0):
    return (True, str(x0))

PROPERTY_SET = {
    "LEXER_FILE": (PROP_LEXER_FILE, to_string),
    "TAB_SIZE": (PROP_TAB_SIZE, to_pos_int),
    "TAB_SPACES": (PROP_TAB_SPACES, to_bool),
    "NEWLINE": (PROP_NEWLINE, newline_prop),
}


def do_find_modeline(ed):
    nlines = min(MAX_READ_LINES, ed.get_line_count())
    lines = [ed.get_text_line(i) for i in range(nlines)]

    for index, line in enumerate(lines):
        mk_index = line.find(MODE_KEY)
        if -1 != mk_index:
            mode_message(f'{ed.get_filename()}:{index+1}: {line}')
            modeline = line[mk_index+MODE_KEY_LEN:]
            modes = cookies.SimpleCookie(modeline)

            for prop0 in modes:
                prop = prop0.upper()

                if prop in PROPERTY_SET:
                    prop_name, validate = PROPERTY_SET[prop]
                    valid, value = validate(modes[prop0].value)
                    if valid:
                        mode_message(f'{prop} = {value}')
                        ed.set_prop(prop_name, value)
                    else:
                        mode_message(f'{value} is invalid for {prop}')
                    continue

                mode_message(f'key "{prop0}" ({prop}) is unknown')

            return

class Command:
    def on_open(self, ed_self):
        do_find_modeline(ed_self)
    def on_save(self, ed_self):
        do_find_modeline(ed_self)
