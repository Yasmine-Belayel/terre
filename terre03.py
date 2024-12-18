import sys


code_letter = ord(sys.argv[1])

for letter in range(code_letter, 123):
    print(chr(letter), end='')
print('\n')
