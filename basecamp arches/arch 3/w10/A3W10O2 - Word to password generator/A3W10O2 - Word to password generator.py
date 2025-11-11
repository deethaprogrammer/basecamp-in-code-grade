import os
import random

def load_file(file):
    try:
        with open(file, "r") as f:
            words = f.read().split("\n")
            return words
    except FileNotFoundError:
        print("file not found")
        return None

def remove_wrong_words(words):
    cleared_words = []
    for word in words:
        if 3 <= len(word) <= 7:
            cleared_words.append(word)
    return cleared_words


def password_creator(cwords):
    while True:
        word_1 = random.choice(cwords)
        word_2 = random.choice(cwords)
        password = word_1.capitalize() + word_2.capitalize()
        if 8 <= len(password) <= 10:
            break
    return password

      
if __name__ == "__main__":
    name_file = input("from wich file?\n>")
    file_path = os.path.dirname(__file__)
    file_name = os.path.join(file_path, name_file)
    words = load_file(file_name)
    if words != None:
        cleared_words = remove_wrong_words(words)
        password = password_creator(cleared_words)
        print(password)