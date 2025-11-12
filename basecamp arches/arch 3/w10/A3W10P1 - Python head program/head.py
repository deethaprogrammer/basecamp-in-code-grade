import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print(f"hello {name}")
    else:
        print("Please provide a name as an argument.")
    try:
        with open(name, "r") as r:
            for i in range(10):
                line = r.readline()
                if not line:
                    break
                print(line, end='')
    except Exception as e:
        print("can't load this file {e}")
        quit()
    