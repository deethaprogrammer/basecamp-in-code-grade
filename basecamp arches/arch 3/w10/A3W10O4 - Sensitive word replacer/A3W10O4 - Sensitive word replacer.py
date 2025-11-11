import os

if __name__ == "__main__":
    text_file_name = input("what is the name of the text file?\n>")
    sensative_file_name = input("what is the name of the text file where you are gonna store the sensative parts?\n>")
    redacted_file_name = input("what is the name of the text file where the text is redacted?\n>")
    path = os.path.dirname(__file__)
    text_file = os.path.join(path, text_file_name)
    sensative_file = os.path.join(path, sensative_file_name)
    redacted_file = os.path.join(path, redacted_file_name)
    try:
        with open(text_file, "r") as r:
            text = r.read()
    except Exception as e:
        print(f"couldn't load the file: {e}")
        exit()

    try:
        with open(sensative_file, "r") as r:
            sens_text = r.read()
    except Exception as e:
        print(f"couldn't load the file: {e}")
        exit()
    sensative_words = [word.strip() for word in sens_text.splitlines() if word.strip()]
    
    for word in sensative_words:
        text = text.replace(word, "*" * len(word))
        
    with open(redacted_file, "w") as w:
        w.write(text)