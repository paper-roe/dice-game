import random

string = 'the quick brown fox jumped over the lazy dog'
string = list(string)
jumbled = ''

for letter in range(0, len(string)):
    jumbled += string.pop(random.randint(0, len(string)-1))

print(string)
print(jumbled)
