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

# Initialiser un compteur pour la longueur
count = 0

# Boucle pour compter les caractères dans l'argument
for char in argument:
    count += 1  # Incrémenter le compteur pour chaque caractère

# Affichage de la taille de la chaîne
print(f"La taille de la chaîne est : {count}")