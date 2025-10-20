import importlib
import re

class CharacterAnalyser:
    def __init__(self):
        self.stats = {
            "character_count":0,
            "space_count": 0
        }

    def analyse_character(self, line):
        for char in line.strip():
            if char != " ":
                self.stats["character_count"] += 1
            else:
                self.stats["space_count"] += 1
        