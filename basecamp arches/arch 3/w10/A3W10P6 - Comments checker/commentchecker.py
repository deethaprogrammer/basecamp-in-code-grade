import os

if __name__ == "__main__":
    file_name_input = input("What is the name of your file:\n>")
    file_names = [names.strip() for names in file_name_input.split(",")]
    file_path = os.path.dirname(__file__)
    for file_name in file_names:
        file = os.path.join(file_path, file_name)
        try:
            with open(file, "r") as r:
                lines = r.readlines()
                for i, line in enumerate(lines):
                    if "def" in line:
                        if i == 0 or not lines[i - 1].strip().startswith("#"):
                            words = line.split(" ")
                            word = line.replace(":", '').split(" ")
                            print(f"File: {file_name} contains a function [{word[1]}] on line [{i + 1}] without a preceding comment.")
        except Exception as e:
            print(f"can't import file {e}")
            quit()