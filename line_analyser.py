import importlib
import re
import word_analyser
import util

importlib.reload(word_analyser)
importlib.reload(util)

class LineAnalyser:
    def __init__(self):
        self.wordAnalyser = word_analyser.WordAnalyser()
        self.inside_paragraph = False
        self.paragraph = ""
        self.stats = {
            "total_lines":0,
            "paragraph_count":0,
            "sentence_length":{},
        }

    def analyse_line(self, line):
        self.stats["total_lines"] += 1
        if line.strip():
            if not self.inside_paragraph:
                self.stats["paragraph_count"] += 1
                self.inside_paragraph = True
            self.paragraph += line.strip()
        else:
            sentences = re.split(r"[.!?]", self.paragraph)
            sentences = [sentence for sentence in sentences if sentence]
            for sentence in sentences:
                if sentence:
                    length = len(util.get_word_array(sentence))
                    if length in self.stats["sentence_length"]:
                        self.stats["sentence_length"][length] += 1
                    else:
                        self.stats["sentence_length"][length] = 1
            self.inside_paragraph = False
            self.paragraph = ""
            
        self.wordAnalyser.analyse_word(line)

    def print_basic_stats(self):
        wordAnalyser = self.wordAnalyser
        characterAnalyser = wordAnalyser.characterAnalyser
        wordCount = sum(wordAnalyser.stats["word_counts"].values())
        sentenceCount = sum(self.stats["sentence_length"].values())
        print("Lines:", self.stats["total_lines"])
        print("Paragraphs:", self.stats["paragraph_count"])
        print("Sentences:", sentenceCount)
        print("Words:", wordCount)
        print("Unique words:", len(wordAnalyser.stats["word_counts"]))
        print("Characters (with spaces):", (characterAnalyser.stats["character_count"] + characterAnalyser.stats["space_count"]))
        print("Characters (without spaces):", characterAnalyser.stats["character_count"])
        print("Average words per line:", f"{(wordCount/self.stats["total_lines"]):.1f}")
        print("Average word length:", f"{wordAnalyser.calculate_average_word_length():.1f} characters")
        print("Average words per sentence:", f"{(wordCount/sentenceCount):.1f}")
        
