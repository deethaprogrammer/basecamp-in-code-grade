import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        print("please provide a name as an argument.")
        quit()
    try:
        with open(name, "r") as r:
            text = r.read().strip()
            line = text.split("\n")
    except Exception as e:
        print(f"can't load the file {e}")
        quit()
    for i in range(10):
        print(line[len(line) - 10 + i])