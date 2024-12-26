import sys

# Vérification du nombre d'arguments
if len(sys.argv) != 3:
    print("Veuillez fournir un nombre et un exposant.")
    sys.exit(1)

# Récupération des arguments
base_str = sys.argv[1]
exposant_str = sys.argv[2]

# Vérification si les arguments sont des nombres valides
if not (base_str.lstrip('-').isdigit() and exposant_str.lstrip('-').isdigit()):
    print("ERREUR :Veuillez entrer deux nombres valides.")
    sys.exit(1)

# Conversion des arguments
base = int(base_str)
exposant = int(exposant_str)

# Initialisation du résultat à 1
resultat = 1

# Cas pour les exposants négatifs
is_negative_exponent = False
if exposant < 0:
    is_negative_exponent = True
    exposant = -exposant  # Rendre l'exposant positif pour la boucle

# Calcul de la puissance
for i in range(exposant):
    resultat *= base

# Si l'exposant était négatif, inverser le résultat
if is_negative_exponent:
    resultat = 1 / resultat

# Affichage du résultat
print(f"{base} élevé à la puissance {exposant_str} est : {resultat}")
