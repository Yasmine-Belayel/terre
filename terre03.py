import sys
code_lettre = ord(sys.argv[1])
for i in range(code_lettre, 123):
    print(chr(i), end='')
print()