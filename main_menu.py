import sys
import file_loader
import export_content
import importlib
import os
from datetime import datetime
import util
import data_visualisation

importlib.reload(util)
importlib.reload(file_loader)
importlib.reload(export_content)
importlib.reload(data_visualisation)

class MainMenu:
    def __init__(self):
        self.loader = file_loader.FileLoader()
    
    def display_menu(self):
        menu_options = {1:"Load text file",
                        2:"Display basic statistics",
                        3:"Word frequency analysis",
                        4:"Sentence analysis",
                        5:"Character analysis",
                        6:"Export results",
                        7:"Spelling checker",
                        8:"Exit"
                       }
        print()
        print("="*50)
        print(f"{"TEXT ANALYSER":^50}")
        print("="*50)
        
        for key, value in menu_options.items():
            print(f"{key}. {value}")
    
        print("="*50)
        print(f"Current File: {self.loader.selected_file}" if self.loader.selected_file else "No file loaded")
        print()
    
    def select_menu(self, menu_id):
        match menu_id:
            case 1:
                self.loader.list_files()
            case 2:
                self.display_basic_stat()
            case 3:
                self.word_frequency_analysis()
            case 4:
                self.sentence_analysis()
            case 5:
                self.character_analysis()
            case 6:
                self.export_result()
            case 7:
                self.spelling_mistakes()
            case 8:
                self.exit()
        
    def display_basic_stat(self):
        if not self.loader.selected_file:
            return print("First you need to select and analyse the document")
        print(f'--- Basic Statistics for "{self.loader.selected_file}" ---')
        for key, value in self.loader.lineAnalyser.get_basic_stats().items():
            print(f"{key}: {value}")
        print()
        print("Generating basic statistics visualisation...")
        print()
        input("Press Enter to continue...")
        data_visualisation.generate_text_composition(self.loader.lineAnalyser.get_basic_stats())

    def word_frequency_analysis(self):
        if not self.loader.selected_file:
            return print("First you need to select and analyse the document")
        print(f'--- Word Analysis for "{self.loader.selected_file}" ---')
        lineAnalyser = self.loader.lineAnalyser
        wordAnalyser = lineAnalyser.wordAnalyser
        print("Top 10 most common words:")
        most_common = wordAnalyser.get_most_common_words(10)
        for i ,(key,value) in enumerate(most_common.items(), start=1):
            print(f" {i:>2}. {key:<20} {value["count"]:>6} times ({value["percentage"]:>3}%)")
        print()
        print("Word length statistics:")
        for key, value in wordAnalyser.get_word_length_stats().items():
            print(f"  {key}: {value}")
        print(f"Words appearing only once: {wordAnalyser.get_word_count_for_frequency(1)}")
        print()
        print("Generating word analysis visualisation...")
        print()
        input("Press Enter to continue...")
        data_visualisation.generate_word_length_distribution(wordAnalyser.stats["word_counts"])
        data_visualisation.generate_most_common_words(most_common)

    def sentence_analysis(self):
        if not self.loader.selected_file:
            return print("First you need to select and analyse the document")
        print(f'--- Sentence Analysis for "{self.loader.selected_file}" ---')
        lineAnalyser = self.loader.lineAnalyser
        for key, value in lineAnalyser.get_sentence_analysis_stats().items():
            print(f"{key}: {value}")
        print()
        print(f"Shortest sentence text: {lineAnalyser.shortestSentence}")
        print()
        print(f"Longest sentence text: {util.wrap_text(lineAnalyser.longestSentence, 2)}")
        print()
        print("Sentence length distribution (top 5):")
        most_common = lineAnalyser.get_sentence_length_distribution(5)
        for key, value in most_common:
            print(f"  {key:>2} words: {value:>6} sentences")
        print()
        print("Generating sentence analysis visualisation...")
        print()
        input("Press Enter to continue...")
        data_visualisation.generate_sentence_length_distribution(lineAnalyser.stats["sentence_length"])
        data_visualisation.generate_most_common_sentence_lengths(most_common)

    def character_analysis(self):
        if not self.loader.selected_file:
            return print("First you need to select and analyse the document")
        print(f'--- Character Analysis for "{self.loader.selected_file}" ---')
        lineAnalyser = self.loader.lineAnalyser
        wordAnalyser = lineAnalyser.wordAnalyser
        characterAnalyser = wordAnalyser.characterAnalyser
        print("Character type distribution:")
        for key, value in characterAnalyser.get_character_type_distribution().items():
            print(f'  {key+":":<20} {value["count"]:>6} ({value["percentage"]:>3}%)')
        print()
        print("Most common letters (10):")
        most_common = characterAnalyser.get_most_common_letters(10).items()
        for i ,(key,value) in enumerate(most_common, start=1):
            print(f' {i:>2}. "{key}" - {value["count"]:>6} times ({value["percentage"]}%)')
        print()
        print("Generating character analysis visualisation...")
        print()
        input("Press Enter to continue...")
        data_visualisation.generate_character_type_distribution(characterAnalyser.get_character_type_distribution())
        data_visualisation.generate_most_common_letters(most_common)

    def export_result(self):
        if not self.loader.selected_file:
            return print("First you need to select and analyse the document")
        fileName = self.loader.selected_file.split(".")[0] + "_result.txt"
        os.makedirs("results", exist_ok=True)
        output_file = os.path.join("results", fileName)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(export_content.get_export_content(self.loader))
        print(f'Results exported to "results/{fileName}"')
        print("Results saved in simple text format - easy to read and understand!")

    def spelling_mistakes(self):
        if not self.loader.selected_file:
            return print("First you need to select and analyse the document")
        print(f'--- Spelling Mistakes for "{self.loader.selected_file}" ---')
        lineAnalyser = self.loader.lineAnalyser
        wordAnalyser = lineAnalyser.wordAnalyser
        spellingChecker = wordAnalyser.spellingChecker
        print()
        print(f"Found {len(spellingChecker.get_mispelled_stats())} spelling mistakes during the analysis")
        print()
        if len(spellingChecker.get_mispelled_stats()) > 0: 
            print("Generating the detailed report...")
            print()
            input("Press Enter to continue...")
            content = ""
            for key, value in spellingChecker.get_mispelled_stats().items():
                content += f"Line {key} - {value}\n"
            fileName = "spelling_mistakes_" + self.loader.selected_file.split(".")[0] + ".txt"
            os.makedirs("results", exist_ok=True)
            output_file = os.path.join("results", fileName)
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f'Results exported to "results/{fileName}"')

    def exit(self):
        print("Thank you for using Text Analyser!")
        sys.exit(0)
            
