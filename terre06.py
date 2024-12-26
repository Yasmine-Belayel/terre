import sys

# Vérification du nombre d'arguments
if len(sys.argv) != 2:
    print("Veuillez fournir un unique argument non numérique.")
    sys.exit(1)

argument = sys.argv[1]

# Vérification si l'argument est un nombre
if argument.isdigit() or (argument[0] == '-' and argument[1:].isdigit()):
    print("ERREUR : l'argument ne doit pas être un nombre.")
    sys.exit(1)

# Initialisation d'une chaîne pour stocker le résultat
reversed_argument = ""

# Boucle pour inverser l'argument
for char in argument:
    reversed_argument = char + reversed_argument

# Affichage du résultat
print(reversed_argument)
