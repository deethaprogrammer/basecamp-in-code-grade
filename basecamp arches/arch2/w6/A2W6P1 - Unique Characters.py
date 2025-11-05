def unique_chars_dict(inputs):
    unique = {}
    for char in inputs:
        unique[char] = True
    return len(unique)

def unique_chars_set(inputs):
    return len(set(inputs))

if __name__ == "__main__":
    variable = input("")
    print(unique_chars_dict(variable))
    print(unique_chars_set(variable))