"""
---criteria---
program should raed a input from a user.
after that it should translate each character in the message to its mapping code
function name: message_to_morse
put a space between each character and 4 space's between each word
the program needs to print the error can't convert char [x] if there is no mapping for it where x is the char that is not found

extend the program with functionality of decoding a morse code
function name: morse_to_message

extend the program with a finction translate_text
so that if you give it a string it will detect if it needs to use message_to_morse or morse_to_message

"""

MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-',
    'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--',
    'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-',
    '?': '..--..'}

def message_to_morse(message):
    message_no_space = message.split(" ")
    morse_sentence = []
    
    for word in message_no_space:
        morse_words = []
        for char in word:
            morse_Code = MORSE_CODE_DICT.get(char.upper())
            if morse_Code:
                morse_words.append(morse_Code)
            else:
                return f"can't convert char [{char}] "
        morse_word = ' '.join(morse_words)
        morse_sentence.append(morse_word)
    morse_sentence = '    '.join(morse_sentence)
    return morse_sentence
        
    

def morse_to_message(morse):
    morse_word = morse.split('    ')
    words = []
    for word in morse_word:
        letter = []
        morse_char = word.split(' ')
        for CODE in morse_char:
            found = False
            for key, value in MORSE_CODE_DICT.items():
                if value == CODE:
                    letter.append(key)
                    found = True
                    break
            if not found:
                return f"can't convert this [{CODE}]"
        words.append(''.join(letter))
    sentence = ' '.join(words)
    return sentence
    

def translate_text(text):
    if all(c in ['.', '-', ' '] for c in text.strip()):
        return morse_to_message(text)
    elif not all(c in ['.', '-'] for c in text):
        return message_to_morse(text)
    pass

if __name__ == "__main__":
    print(translate_text(input("input: ")))