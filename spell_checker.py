from spellchecker import SpellChecker

class SpellingChecker:
    def __init__(self):
        self.spell = SpellChecker()
        self.stats = {}

    def check_spelling(self, line_number, word_array):
        misspelled = self.spell.unknown(word_array)
        if len(misspelled) > 0:
            self.stats[line_number] = misspelled

    def get_mispelled_stats(self):
        return self.stats