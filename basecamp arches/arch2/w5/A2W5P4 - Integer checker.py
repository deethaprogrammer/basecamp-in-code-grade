def is_integer(unchecked: str) -> bool:
    unchecked = unchecked.strip()
    if len(unchecked) == 0:
        return False
    if (unchecked.isdigit()):
        return True
    if unchecked[0] in "-+" and unchecked[1:].isdigit():
        return True
    else:
        return False
    
def remove_non_integer(unchecked: str) -> int:
    unchecked = unchecked.strip()
    chek = ""
    for letter in unchecked:
        if letter.isdigit() or letter == ("-" or "+"):
            chek += letter
    return int(chek)
    
        

if __name__ == "__main__":
    unchek = input("test: ")
    chek = ""
    if is_integer(unchek) == True:
        print('valid')
    else:
        print('invalid')
    print(remove_non_integer(unchek))