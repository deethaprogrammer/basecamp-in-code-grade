import os

if __name__ == "__main__":
    file_name = input("What is the name of your file:\n>")
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path, file_name)
    words = {}
    try:
        with open(file, "r") as r:
            for line in r:
                for word in line.split():
                    word = word.replace(",.", '')
                    if word in words.keys():
                        words[word] += 1
                    else:
                        words[word] = 1
    except Exception as e:
        print(f"can't load file {e}")
        quit()

    max_values = max(words.values())
    min_values = min(words.values())
    most_common = [Word for Word, count in words.items() if count == max_values]
    most_rare = [Word for Word, count in words.items() if count == min_values]
    for most_word in most_common:
        print(most_word)
    print(' '.join(most_rare))