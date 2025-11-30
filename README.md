# Text Analyser – Console Program

A simple and interactive **Python console application** that analyses text files along the various kind of parameters and generate the visualizations for them. It supports for identifying **spelling mistakes** and supports for multiple file types (like `.txt` and `.py`) and automatically handles dependency installation when needed.

---

## Features

- Reads `.txt` and `.docx` files (customizable via `config.json`)
- Automatically installs missing dependencies (with user consent)
- Fully configurable and runs smoothly in both **terminal** and **Jupyter Notebook**
- Support displaying basic statistics
- Support word frequency analysis
- Support sentence analysis
- Support character analysis
- Support Exporting results as a document
- Support identifying spelling mistakes

---

## Project Structure

```
Text-Analyser/
├── main.py # Main console program
├── main_menu.py # Program menu
├── file_loader.py # Loading the file and read line by line
├── line_analyser.py # Analyse the line
├── word_analyser.py # Analyse the word
├── character_analyser.py # Analyse the character
├── export_content.py # Template for export document
├── spell_checker.py # Check spelling mistakes
├── data_visualisation.py # Handle all data visualisation matters
├── util.py # Handle common and support functions
├── config.json # Configuration file (file types)
├── sample.txt # Example file for testing
└── README.md # Project documentation
```

---

## Configuration (`config.json`)

Example configuration:
```json
{
    "document_path": ".",
    "file_types": ["txt"]
}
```
You can modify file_types to include more extensions such as .py (binary files are not allowed)

---

## Installation

1. Clone the repository
    - git clone https://github.com/TharangaMahavila/Text-Analyser.git<br>
    - cd Text-Analyser
2. Install dependencies
    - You should have python running in your environment<br>
    - if not see the official installing page of python (https://www.python.org/downloads/)
3. Usage
    - python3 main.py

---

## License
This project is licensed under the MIT License — you’re free to use, modify, and distribute it.

---

## Future Improvements
Add support for grammar checking<br>
Add a GUI version for the better experience

---

## Author
Tharanga Mahavila<br>
https://www.linkedin.com/in/tharanga-mahavila-7b9994199<br>
https://github.com/TharangaMahavila<br>
tharangamahavila@gmail.com