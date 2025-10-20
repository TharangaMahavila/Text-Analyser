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
            case 9:
                self.exit()
        
    def display_basic_stat(self):
        if not self.loader.selected_file:
            return print("First you need to select and analyse the document")
        self.loader.lineAnalyser.get_basic_stats(self.loader.selected_file)

    def exit(self):
        print("Thank you for using Text Analyser!")
