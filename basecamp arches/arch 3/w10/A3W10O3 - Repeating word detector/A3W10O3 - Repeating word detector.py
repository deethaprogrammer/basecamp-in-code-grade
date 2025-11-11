import os


if __name__ == "__main__":
    name_file = input("filename: ")
    file_path = os.path.dirname(__file__)
    file_name = os.path.join(file_path, name_file)
    try:
        with open(file_name, "r") as r:
            text = r.read().split("\n")
    except Exception as e:
        print(f"Error opening file: {e}")
        quit()
    seen_words = []
    for i, line in enumerate(text):
        words = [w.strip(".,!?;:\"'()[]{}").lower() for w in line.split()]
        for j in range(1, len(words)):
            if words[j] == words[j - 1]:
                print(f"Found duplicate word [{words[j]}] on line: {i + 1}")
