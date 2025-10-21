from datetime import datetime
import importlib
import util

importlib.reload(util)

def get_export_content(fileLoader):
    lineAnalyser = fileLoader.lineAnalyser
    wordAnalyser = lineAnalyser.wordAnalyser
    characterAnalyser = wordAnalyser.characterAnalyser

    
    basic_stats = "\n".join([f"{key}: {value}" for key, value in lineAnalyser.get_basic_stats().items()])
    
    most_common_words = "\n".join([f"{i:>2}. {key:<20} {value}" for i, (key, value) in enumerate(wordAnalyser.get_most_common_words(10).items(), start=1)])

    word_stats = "\n".join([f"{key}: {value}" for key, value in wordAnalyser.get_word_length_stats().items()])

    sentence_stats = "\n".join([f"{key}: {value}" for key, value in lineAnalyser.get_sentence_analysis_stats().items()])

    shortest_sentence = f"Shortest sentence text: {lineAnalyser.shortestSentence}"

    longest_sentence = f"Longest sentence text: {util.wrap_text(lineAnalyser.longestSentence, 2)}"

    sentence_length_stats = "\n".join([f"{key}: {value}" for key, value in lineAnalyser.get_sentence_length_distribution(5).items()])

    character_type_stats = "\n".join([f"{key+":":<20} {value}" for key, value in characterAnalyser.get_character_type_distribution().items()])

    most_common_letters = "\n".join([f'{i:>2}. "{key}": {value}' for i, (key, value) in enumerate(characterAnalyser.get_most_common_letters(10).items(), start=1)])
    
    content = f"""============================================================
TEXT ANALYSIS RESULTS
============================================================
File analysed: {fileLoader.selected_file}
Analysis date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                
BASIC STATISTICS
--------------------
{basic_stats}
    
TOP 10 MOST COMMON WORDS
------------------------------
{most_common_words}

WORD STATISTICS
--------------------
{word_stats}

SENTENCE STATISTICS
-------------------------
{sentence_stats}

{shortest_sentence}

{longest_sentence}

Sentence length distribution (top 5):
{sentence_length_stats}

CHARACTER STATISTICS
-------------------------
{character_type_stats}

TOP 10 MOST COMMON LETTERS
------------------------------
{most_common_letters}

============================================================
End of Analysis Report
programmed by: Tharanga & Lashadi
============================================================
"""
    return content