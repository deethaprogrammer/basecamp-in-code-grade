import random
def generate_random_password() -> str:
    password_sequence = []
    Range = random.randint(7,10)

    for i in range(Range):
        password_sequence.append(chr(random.randint(33, 126)))
    password = "".join(password_sequence)
    return password

if __name__ == "__main__":
    print(generate_random_password())
    