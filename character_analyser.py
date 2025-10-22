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
        stats["Letters"] = {
            "count":total_letters,
            "percentage":round((total_letters/total_characters)*100, 1)
        }
        stats["Digits"] = {
            "count":self.stats["digit_count"],
            "percentage":round((self.stats["digit_count"]/total_characters)*100, 1)
        }
        stats["Spaces"] = {
            "count":self.stats["space_count"],
            "percentage":round((self.stats["space_count"]/total_characters)*100, 1)
        }
        stats["Punctuation"] = {
            "count":self.stats["punctuation_count"],
            "percentage":round((self.stats["punctuation_count"]/total_characters)*100, 1)
        }
        return stats

    def get_most_common_letters(self, length):
        total_characters = self.get_total_characters()
        sorted_letters = sorted(self.stats["letter_count"].items(), key=lambda item: item[1], reverse=True)
        letters = {}
        for letter,count in sorted_letters[:length]:
            letters[letter] = {
                "count":count,
                "percentage":round((count/total_characters)*100, 1)
            }
        return letters

    def get_total_characters(self, with_space=True):
        without_space = sum(self.stats["letter_count"].values()) + self.stats["digit_count"] + self.stats["punctuation_count"]
        if with_space:
            return without_space + self.stats["space_count"]
        else:
            return without_space
        