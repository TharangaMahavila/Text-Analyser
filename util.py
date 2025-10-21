import re

def get_word_array(line):
    words = re.split(r"[ ,;:!?]+", line.strip())
    words = [word.lower() for word in words if word]
    return words
