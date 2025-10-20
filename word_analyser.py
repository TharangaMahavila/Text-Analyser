import importlib
import re
import character_analyser

importlib.reload(character_analyser)

class WordAnalyser:
    def __init__(self):
        self.characterAnalyser = character_analyser.CharacterAnalyser()
        self.stats = {
            "word_count":0,
            "word_length":0,
            "unique_words": set()
        }

    def analyse_word(self, line):
        words = re.split(r"[ ,;:!?]+", line.strip())
        words = [word.lower() for word in words if word]
        self.stats["word_count"] += len(words)
        self.stats["unique_words"].update(words)
        self.characterAnalyser.analyse_character(line)
        