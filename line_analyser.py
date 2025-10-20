import importlib
import re
import word_analyser

importlib.reload(word_analyser)

class LineAnalyser:
    def __init__(self):
        self.wordAnalyser = word_analyser.WordAnalyser()
        self.inside_paragraph = False
        self.paragraph = ""
        self.stats = {
            "total_lines":0,
            "paragraph_count":0,
            "sentence_count":0,
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
            self.stats["sentence_count"] += len(sentences)
            self.inside_paragraph = False
            self.paragraph = ""
            
        self.wordAnalyser.analyse_word(line)

    def get_basic_stats(self, filename):
        wordAnalyser = self.wordAnalyser
        characterAnalyser = wordAnalyser.characterAnalyser
        print(f'--- Basic Statistics for "{filename}" ---')
        print("Lines:", self.stats["total_lines"])
        print("Paragraphs:", self.stats["paragraph_count"])
        print("Sentences:", self.stats["sentence_count"])
        print("Words:", wordAnalyser.stats["word_count"])
        print("Unique words:", len(wordAnalyser.stats["unique_words"]))
        print("Characters (with spaces):", (characterAnalyser.stats["character_count"] + characterAnalyser.stats["space_count"]))
        print("Characters (without spaces):", characterAnalyser.stats["character_count"])
        print("Average words per line:", f"{(wordAnalyser.stats["word_count"]/self.stats["total_lines"]):.1f}")
        print("Average word length:", f"{(characterAnalyser.stats["character_count"]/wordAnalyser.stats["word_count"]):.1f} characters")
        print("Average words per sentence:", f"{(wordAnalyser.stats["word_count"]/self.stats["sentence_count"]):.1f}")
        print()
        print("Generating basic statistics visualisation...")
        print()
        input("Press Enter to continue...")
        
