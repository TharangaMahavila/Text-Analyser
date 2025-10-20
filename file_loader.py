from pathlib import Path
import importlib
import line_analyser

importlib.reload(line_analyser)

class FileLoader:
    def __init__(self):
        self.selected_file = None
        self.lineAnalyser = None
        
    def get_all_files(self, path):
        try:
            directory = Path(path)
            if not directory.exists() and directory.is_dir():
                print("Directory not found")
                return []
            return [f.name for f in directory.glob("*.txt")]
        except Exception as e:
            print(e)
    
    def get_file_name(self, choice, file_list):
        for index, file in enumerate(file_list, start=1):
            if choice == str(index) or choice == file:
                return file
        return None
        
    def list_files(self):
        print("--- File Selection ---")
        print("Available text files:")
        current_path = "."
        files = self.get_all_files(current_path)
        for index, file in enumerate(files, start=1):
            print(f"  {index}. {file}\n")
        if len(files) > 0:
            attempts = 0
            while True:
                try:
                    if attempts > 5:
                        print("It seems you have entered five consecutive invalid attempts. Come back again later!")
                        break
                    choice = input("Enter filename or number from list above:")
                    print()
                    filename = self.get_file_name(choice, files)
                    if filename is not None:
                        self.selected_file = filename
                        self.lineAnalyser = line_analyser.LineAnalyser()
                        self.analyse_txt(current_path, filename)
                        break
                    else:
                        raise ValueError()
                except ValueError:
                    attempts += 1
                    print("Invalid number or filename. Please enter again")
                
        else:
            print("No files found. There should be at least one file to begin")
    
    def analyse_txt(self, path, filename):
        print(f'Analysing "{filename}"...')
        file_path = Path(path) / filename
        with open(file_path, 'r') as f:
            for line in f:
                self.lineAnalyser.analyse_line(line)
        print(f"Analysis complete! Processed {self.lineAnalyser.stats["total_lines"]} lines.")
        print(f'Successfully loaded and analysed "{filename}"')
