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

    def print_most_common_words(self, length):
        print(f"Top {length} most common words:")
        total_words = sum(self.stats["word_counts"].values())
        sorted_words = sorted(self.stats["word_counts"].items(), key=lambda item: item[1], reverse=True)
        for i ,(word,count) in enumerate(sorted_words[:length], start=1):
            print(f" {i:>2}. {word:<20} {count:>6} times ( {(count/total_words)*100:.1f}%)")

    def print_word_length_stats(self):
        print("Word length statistics:")
        print(f"  Shortest word: {self.stats["shortest_word"]} characters")
        print(f"  Longest word: {self.stats["longest_word"]} characters")
        print(f"  Average word length: {self.calculate_average_word_length():.1f} characters")

    def get_word_count_for_frequency(self, frequency):
        return sum(1 for value in self.stats["word_counts"].values() if value == frequency)

    def calculate_average_word_length(self):
        total_characters = 0
        total_words = 0
        for word,count in self.stats["word_counts"].items():
            total_characters += (len(word)*count)
            total_words += count
        return total_characters / total_words
            
