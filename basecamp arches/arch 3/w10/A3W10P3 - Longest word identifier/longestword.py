import os

if __name__ == "__main__":
    file_name = input("What is the name of your file:\n>")
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path, file_name)
    words = []
    try:
        with open(file, "r") as r:
            for line in r:
                for word in line.split():
                    words.append(word)
    except Exception as e:
        print(f"can't load file {e}")
        quit()
    max_len = max(len(word) for word in words)
    longest_words = list(filter(lambda length: len(length) == max_len, words))
    print(longest_words)