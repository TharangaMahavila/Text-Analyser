import re
import textwrap
import shutil

def get_word_array(line):
    words = re.split(r"[ ,;:!?]+", line.strip())
    words = [word.lower() for word in words if word]
    return words

def wrap_text(text, lines):
    terminal_width = shutil.get_terminal_size((80, 20)).columns
    wrapped = textwrap.wrap(text, width=terminal_width)
    if len(wrapped) > lines:
        wrapped[lines-1] = wrapped[lines-1].rstrip() + "..."
        return "\n".join(wrapped[:lines])
    else:
        return "\n".join(wrapped)