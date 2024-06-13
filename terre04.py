import sys

nombre = int(sys.argv[1])
reste = nombre % 2
if reste == 0:
    print(f"le nombre {nombre} est pair")
else:
    print(f"le nombre {nombre} est impair")
    