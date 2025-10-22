import importlib
import re
import word_analyser
import util

importlib.reload(util)
importlib.reload(word_analyser)

class LineAnalyser:
    def __init__(self):
        self.wordAnalyser = word_analyser.WordAnalyser()
        self.inside_paragraph = False
        self.paragraph = ""
        self.shortestSentence = ""
        self.longestSentence = ""
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
                    word_length = len(util.get_word_array(sentence))
                    if self.shortestSentence:
                        if len(util.get_word_array(sentence)) < len(util.get_word_array(self.shortestSentence)):
                            self.shortestSentence = sentence
                    else:
                        self.shortestSentence = sentence

                    if self.longestSentence:
                        if len(util.get_word_array(sentence)) > len(util.get_word_array(self.longestSentence)):
                            self.longestSentence = sentence
                    else:
                        self.longestSentence = sentence

                    if word_length in self.stats["sentence_length"]:
                        self.stats["sentence_length"][word_length] += 1
                    else:
                        self.stats["sentence_length"][word_length] = 1
            self.inside_paragraph = False
            self.paragraph = ""
            
        self.wordAnalyser.analyse_word(line)

    def get_basic_stats(self):
        wordAnalyser = self.wordAnalyser
        characterAnalyser = wordAnalyser.characterAnalyser
        wordCount = sum(wordAnalyser.stats["word_counts"].values())
        sentenceCount = sum(self.stats["sentence_length"].values())

        basic_stat = {}
        basic_stat["Lines"] = self.stats["total_lines"]
        basic_stat["Paragraphs"] = self.stats["paragraph_count"]
        basic_stat["Sentences"] = sentenceCount
        basic_stat["Words"] = wordCount
        basic_stat["Unique words"] = len(wordAnalyser.stats["word_counts"])
        basic_stat["Characters (with spaces)"] = characterAnalyser.get_total_characters()
        basic_stat["Characters (without spaces)"] = characterAnalyser.get_total_characters(False)
        basic_stat["Average words per line"] = f"{(wordCount/self.stats["total_lines"]):.1f}"
        basic_stat["Average word length"] = f"{wordAnalyser.calculate_average_word_length():.1f} characters"
        basic_stat["Average words per sentence"] = f"{(wordCount/sentenceCount):.1f}"
        return basic_stat

    def get_sentence_analysis_stats(self):
        wordAnalyser = self.wordAnalyser
        wordCount = sum(wordAnalyser.stats["word_counts"].values())
        sentenceCount = sum(self.stats["sentence_length"].values())
        stats = {}
        stats["Total sentences"] = sentenceCount
        stats["Average words per sentence"] = f"{(wordCount/sentenceCount):.1f}"
        stats["Shortest sentence"] = f"{len(util.get_word_array(self.shortestSentence))} words"
        stats["Longest sentence"] = f"{len(util.get_word_array(self.longestSentence))} words"
        return stats

    def get_sentence_length_distribution(self, length):
        sorted_sentences = sorted(self.stats["sentence_length"].items(), key=lambda item: item[1], reverse=True)
        return sorted_sentences[:length]