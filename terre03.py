import sys
code_letter = ord(sys.argv[1])
for i in range(code_letter, 123):
    print(chr(i), end='')
print()
print()