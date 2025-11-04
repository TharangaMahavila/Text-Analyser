from pathlib import Path
import importlib
import util
import line_analyser

importlib.reload(line_analyser)

class FileLoader:
    def __init__(self):
        self.selected_file = None
        self.lineAnalyser = None
        
    def get_all_files(self):
        try:
            directory = Path(util.get_config("document_path"))
            if not directory.exists() and directory.is_dir():
                print("Directory not found")
                return []
            files = []
            for ext in util.get_config("file_types"):
                files.extend([f.name for f in directory.glob(f"*.{ext}")])
            return files
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
        files = self.get_all_files()
        for index, file in enumerate(files, start=1):
            print(f"  {index}. {file}")
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
                        self.lineAnalyser = line_analyser.LineAnalyser()
                        self.analyse_txt(filename)
                        self.selected_file = filename
                        break
                    else:
                        raise ValueError("Invalid number or filename. Please enter again")
                except Exception as e:
                    attempts += 1
                    print(e)
                
        else:
            print("No files found. There should be at least one file to begin")
    
    def analyse_txt(self, filename):
        try:
            print(f'Analysing "{filename}"...')
            file_path = Path(util.get_config("document_path")) / filename
            with open(file_path, 'r') as f:
                for line in f:
                    self.lineAnalyser.analyse_line(line)
            print(f"Analysis complete! Processed {self.lineAnalyser.stats["total_lines"]} lines.")
            print(f'Successfully loaded and analysed "{filename}"')
        except Exception as e:
            print(e)
            raise Exception("Error in analysing the document")