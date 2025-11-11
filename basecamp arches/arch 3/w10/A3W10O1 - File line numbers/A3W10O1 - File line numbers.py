import os


def fix_encoding_issues(s):
    return (
        s.replace("â€“", "-")
         .replace("â€”", "--")
         .replace("â€˜", "'")
         .replace("â€™", "'")
         .replace("â€œ", '"')
         .replace("â€�", '"')
         .replace("€™", "'")
    )
def load_file(file_name):
    with open(file_name, "r") as t:
        text = t.read().split("\n")
    return text

def place_numbers(text):
    num_text = []
    for i, lines in enumerate(text):
        lines = fix_encoding_issues(lines)
        Numbered = str(i + 1)+ ": " + lines
        num_text.append(Numbered)
    return num_text
    
def save_to_new_file(output_name, num_text):
    with open(output_name, "w", encoding="utf-8") as f:
        f.write("\n".join(num_text))
    
if __name__ == "__main__":
    File = input("input the file_name\n>")
    Output_FILE = input("Enter name for output file\n>")
    file_path = os.path.dirname(__file__)
    file_name = os.path.join(file_path, File)
    output_name = os.path.join(file_path, Output_FILE)
    text = load_file(file_name)
    num_text = place_numbers(text)
    save_to_new_file(output_name, num_text)