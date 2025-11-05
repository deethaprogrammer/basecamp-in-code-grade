import random

correct = 0

arithmetic_types = {
    "summation": "+",
    "multiplication": "*",
    "subtraction": "-"
}


def arithmetic_operation(arithmetic_type):
    if arithmetic_type == "summation":
        return lambda x, y: x + y
    elif arithmetic_type == "multiplication":
        return lambda x, y: x * y
    elif arithmetic_type == "subtraction":
        return lambda x, y: x - y
    else:
        return False

if __name__ == "__main__" :
    TYPE = input("input what type of formules: ")
    Math = arithmetic_operation(TYPE)
    if not Math:
        print("not right input")
    else:
        form = arithmetic_types[TYPE]
        for i in range(1, 11):
            x = random.randrange(0, 9)
            y = random.randrange(0, 9)
            print(f'{x} {form} {y} = ', end=" ")
            answered = input("")
            try:
                if int(answered) == Math(x, y):
                    correct += 1
            except ValueError:
                print("invalid input")
        print(f'You had {correct} correct and {10 - int(correct)} incorrect answers in {TYPE}')