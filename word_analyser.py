import importlib
import re
import character_analyser
import util

importlib.reload(character_analyser)
importlib.reload(util)

class WordAnalyser:
    def __init__(self):
        self.characterAnalyser = character_analyser.CharacterAnalyser()
        self.stats = {
            "word_counts":{},
            "shortest_word":1000,
            "longest_word":0
        }

    def analyse_word(self, line):
        words = util.get_word_array(line)
        for word in words:
            word = re.sub(r'[,.!?;:()"\'"]', '', word)
            if len(word) < self.stats["shortest_word"]:
                self.stats["shortest_word"] = len(word)
            if len(word) > self.stats["longest_word"]:
                self.stats["longest_word"] = len(word)
            if word in self.stats["word_counts"]:
                self.stats["word_counts"][word] += 1
            else:
                self.stats["word_counts"][word] = 1
        self.characterAnalyser.analyse_character(line)

    def get_most_common_words(self, length):
        total_words = sum(self.stats["word_counts"].values())
        sorted_words = sorted(self.stats["word_counts"].items(), key=lambda item: item[1], reverse=True)
        words = {}
        for word,count in sorted_words[:length]:
            words[word] = {
                "count":count,
                "percentage": round((count/total_words)*100, 1)
            }
        return words

    def get_word_length_stats(self):
        stats = {}
        stats["Shortest word"] = f"{self.stats["shortest_word"]} characters"
        stats["Longest word"] = f"{self.stats["longest_word"]} characters"
        stats["Average word length"] = f"{self.calculate_average_word_length():.1f} characters"
        return stats

    def get_word_count_for_frequency(self, frequency):
        return sum(1 for value in self.stats["word_counts"].values() if value == frequency)

    def calculate_average_word_length(self):
        total_characters = 0
        total_words = 0
        for word,count in self.stats["word_counts"].items():
            total_characters += (len(word)*count)
            total_words += count
        return total_characters / total_words
            