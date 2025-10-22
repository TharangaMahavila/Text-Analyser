import matplotlib.pyplot as plt

def get_bar_chart(x,y,title="",x_label="",y_label=""):
    plt.bar(x, y)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.show()

def get_pie_chart(values, labels, title=""):
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title(title)
    plt.show()

def generate_text_composition(data):
    x = ["Lines","Paragraphs","Sentences","Unique words"]
    y = [data["Lines"],data["Paragraphs"],data["Sentences"],data["Unique words"]]
    get_bar_chart(x, y, "Text Composition", "", "count")

def generate_word_length_distribution(data):
    x = [len(key) for key in data.keys()]
    y = list(data.values())
    get_bar_chart(x, y, "Word Length Distribution", "Word length (characters)", "Frequency")
    
def generate_most_common_words(data):
    x = list(data.keys())
    y = [value["count"] for value in data.values()]
    get_bar_chart(x, y, "Top 10 most common words", "Words", "Frequency")

def generate_sentence_length_distribution(data):
    x = list(data.keys())
    y = list(data.values())
    get_bar_chart(x, y, "Sentence Length Distribution", "Sentence length (words)", "Frequency")
    
def generate_most_common_sentence_lengths(data):
    x = [str(key)+" words" for key,value in data]
    y = [value for key,value in data]
    get_bar_chart(x, y, "Top 5 most common sentence length", "Sentence length (words)", "Number of sentences")

def generate_character_type_distribution(data):
    values = [value["count"] for value in data.values()]
    lables = list(data.keys())
    get_pie_chart(values, lables, "Character Type Distribution")

def generate_most_common_letters(data):
    x = [key for key,value in data]
    y = [value["count"] for key,value in data]
    get_bar_chart(x, y, "Top 10 most common letters", "Letter", "Frequency")