import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print(f"hello {name}")
    else:
        print("Please provide a name as an argument.")
    try:
        with open(name, "r") as r:
            text = r.read()
    except Exception as e:
        print("can't load this file {e}")
        quit()
    print(text)