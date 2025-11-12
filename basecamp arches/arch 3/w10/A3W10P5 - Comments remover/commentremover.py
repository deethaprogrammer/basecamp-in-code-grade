import os

if __name__ == "__main__":
    file_name_input = input("What is the name of your file:\n>")
    file_name_save = input("what is the name of the new file:\n>")
    file_path = os.path.dirname(__file__)
    file = os.path.join(file_path, file_name_input)
    file_save = os.path.join(file_path, file_name_save)
    text = []
    try:
        with open(file, "r") as r:
            for line in r:
                if "#" in line:
                    line = line.replace("#", '').strip()
                    text.append(line)
                else:
                    text.append(line)
    except Exception as e:
        print(f"can't import file {e}")
        quit()
    text_full = ("\n".join(text))
    try:
        with open(file_save, "w") as w:
            w.write(text_full)
    except Exception as e:
        print(f"can't import file {e}")
        quit()