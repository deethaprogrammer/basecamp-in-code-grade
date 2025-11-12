import sys

if __name__ == "__main__":
    answer = []
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        print("please provide a name as an argument.")
        quit()
    try:
        with open(name, "r") as r:
            for line in r:
                answer.append(line)
                if len(answer) > 10:
                    answer.pop(0)
    except Exception as e:
        print(f"can't load the file {e}")
        quit()
    for i in range(len(answer)):
        print(answer[i])