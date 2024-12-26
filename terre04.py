import sys

if len(sys.argv) < 2:
    print("Veuillez fournir un nombre en argument")
    sys.exit(1)


argument = sys.argv[1]


if argument.isdigit() or (argument[0] == '-' and argument[1:].isdigit()):
    number = int(argument)  
else:
    print("Veuillez entrer un nombre valide")
    sys.exit(1)


rest = number % 2
if rest == 0:
    print(f"le nombre {number} est pair")
else:
    print(f"le nombre {number} est impair")