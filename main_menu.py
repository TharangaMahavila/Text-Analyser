import file_loader
import importlib

importlib.reload(file_loader)

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
                        8:"Grammer checker",
                        9:"Exit"
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
            case 9:
                self.exit()
        
    def display_basic_stat(self):
        if not self.loader.selected_file:
            return print("First you need to select and analyse the document")
        print(f'--- Basic Statistics for "{self.loader.selected_file}" ---')
        self.loader.lineAnalyser.print_basic_stats()
        print()
        print("Generating basic statistics visualisation...")
        print()
        input("Press Enter to continue...")

    def word_frequency_analysis(self):
        if not self.loader.selected_file:
            return print("First you need to select and analyse the document")
        print(f'--- Word Analysis for "{self.loader.selected_file}" ---')
        lineAnalyser = self.loader.lineAnalyser
        wordAnalyser = lineAnalyser.wordAnalyser
        wordAnalyser.print_most_common_words(10)
        print()
        wordAnalyser.print_word_length_stats()
        print(f"Words appearing only once: {wordAnalyser.get_word_count_for_frequency(1)}")
        print()
        print("Generating word analysis visualisation...")
        print()
        input("Press Enter to continue...")

    def exit(self):
        print("Thank you for using Text Analyser!")
