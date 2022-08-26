alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

use_again = True

def get_input():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        shift = shift % 26
        
    return direction, text, shift

def caesar(phrase, num, code):
    result= ''
    for char in phrase:
        if char in alphabet:
            char_index = alphabet.index(char)
            if code == "encode":
                if char_index + num < len(alphabet)-1:
                    char = alphabet[char_index + num]
                else: 
                    char = alphabet[char_index + num - len(alphabet)]
            else:
                char = alphabet[char_index - num]
        result += str(char)
    return result

while use_again:
    
    direction, text, shift = get_input()
    
    result = caesar(text, shift, direction)
    
    if direction == 'encode':
        print(f'Your encoded phrase is: {result}')

    elif direction == 'decode':
        print(f'Your decoded phrase is: {result}')

    else:
        print('Please enter \'encode\' or \'decode\'')
    
    ask = input("Would you like to keep going? (y/n)\n")
    if ask == 'n':
        use_again = False
    