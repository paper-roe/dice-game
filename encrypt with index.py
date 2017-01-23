ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = input('Enter your message: ').upper()
encrypted = ''

for letter in message:
    if letter == ' ':
        encrypted += letter
    elif ALPHABET.index(letter) + 5 > len(ALPHABET):
        encrypted += ALPHABET[ALPHABET.index(letter) + 5 - 26]
    else:
        encrypted += ALPHABET[ALPHABET.index(letter) + 5]

print(encrypted)
