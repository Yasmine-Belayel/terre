import sys

# vérification des arguments
if len(sys.argv) < 3:
    print("Veuillez fournir deux nombres en arguments : un dividende et un diviseur.")
    sys.exit(1)

# Vérification si les arguments sont des entiers
dividend_str = sys.argv[1]
divisor_str = sys.argv[2]

if not (dividend_str.lstrip('-').isdigit() and divisor_str.lstrip('-').isdigit()):
    print("Veuillez entrer des nombres valides.")
    sys.exit(1)

# Conversion des arguments en entiers
dividend = int(dividend_str)
divisor = int(divisor_str)

# Vérification des conditions pour la division
if dividend >= divisor > 0:
    result = dividend // divisor  # Utilisation de // pour la division entière
    rest = dividend % divisor
    print(f"{dividend} / {divisor} = {result}")
    print(f"Reste: {rest}")
else:
    print("ERREUR : Assurez-vous que le dividende est supérieur ou égal au diviseur et que le diviseur est positif.")
