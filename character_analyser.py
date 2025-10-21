import importlib
import re
import string

class CharacterAnalyser:
    def __init__(self):
        self.stats = {
            "letter_count":{},
            "digit_count":0,
            "punctuation_count":0,
            "space_count": 0
        }

    def analyse_character(self, line):
        for char in line.strip():
            if char != " ":
                if char.isdigit():
                    self.stats["digit_count"] += 1
                elif char in string.punctuation:
                    self.stats["punctuation_count"] += 1
                else:
                    if char in self.stats["letter_count"]:
                        self.stats["letter_count"][char] += 1
                    else:
                        self.stats["letter_count"][char] = 1           
            else:
                self.stats["space_count"] += 1

    def get_character_type_distribution(self):
        total_letters = sum(self.stats["letter_count"].values())
        total_characters = self.get_total_characters()
        stats = {}
        stats["Letters"] = f"{total_letters:>6} ({(total_letters/total_characters)*100:.1f})%"
        stats["Digits"] = f"{self.stats["digit_count"]:>6} ({(self.stats["digit_count"]/total_characters)*100:.1f})%"
        stats["Spaces"] = f"{self.stats["space_count"]:>6} ({(self.stats["space_count"]/total_characters)*100:.1f})%"
        stats["Punctuation"] = f"{self.stats["punctuation_count"]:>6} ({(self.stats["punctuation_count"]/total_characters)*100:.1f})%"
        return stats

    def get_most_common_letters(self, length):
        total_characters = self.get_total_characters()
        sorted_letters = sorted(self.stats["letter_count"].items(), key=lambda item: item[1], reverse=True)
        letters = {}
        for i ,(letter,count) in enumerate(sorted_letters[:length], start=1):
            letters[letter] = f'{count:>6} times ({(count/total_characters)*100:.1f}%)'
        return letters

    def get_total_characters(self, with_space=True):
        without_space = sum(self.stats["letter_count"].values()) + self.stats["digit_count"] + self.stats["punctuation_count"]
        if with_space:
            return without_space + self.stats["space_count"]
        else:
            return without_space
        