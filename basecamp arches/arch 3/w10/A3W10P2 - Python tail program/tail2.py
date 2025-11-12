import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        print("please provide a name as an argument.")
        quit()
    try:
        with open(name, "r") as r:
            total_line = 0
            for line in r:
                total_line += 1
        with open(name, "r") as f:
            for i, line in enumerate(f):
                if i >= total_line - 10:
                    print(line, end='')
    except Exception as e:
        print(f"can't load the file {e}")
        quit()