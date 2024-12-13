import sys

number = int(sys.argv[1])
rest = number % 2
if rest == 0:
    print(f"le nombre {number} est pair")
else:
    print(f"le nombre {number} est impair")
    