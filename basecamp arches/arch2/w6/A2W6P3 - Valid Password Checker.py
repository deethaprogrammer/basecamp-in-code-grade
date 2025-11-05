"""
valid password needs to be a combination of:
-digits
-uppercase and lowercase (letters)
-and only the symbols * @ ! ?

the program needs to ask the person for a input the input needs to be a password
after that the program needs to validate if its an valid password

---criteria---
the length of the password needs to be between 8 and 20 characters so not less than 8 and not more than 20

if the password is not valid the person gets 3 chances to validate another password

print(valid) if its valid and print(invalid) if it is not

use sets and set operations to solve the problem
"""

#valid = 0,1,2,3,4,5,6,7,8,9 a/z * @ ! ? and A/Z
allowed_char = set(chr(i) for i in range(48, 58))| set(chr(i) for i in range(65, 91))| set([chr(i) for i in range(97, 123)])
allowed_char.update ('*', '@', '!', '?')
chances = 0

def validation(password) -> bool:
    if 8 <= len(password) <=20:
        chars = set(password)
        if chars.issubset(allowed_char):
            return True
        
if __name__ == "__main__":
    while chances <4:
        password = input("input a password: ")
        
        if validation(password):
            print("valid")
            break
        else:
            print('invalid')
            chances +=1