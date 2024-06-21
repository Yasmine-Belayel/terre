import sys

if len(sys.argv) != 2:
    print("Erreur! Merci d'entrer uniquement UN SEUL argument")
else:
    try:
        nombre = int(sys.argv[1])
    except:
        print("Merci d'entrer uniquement des chiffres")
    else:
        if nombre >= 0:
            resultat = nombre ** 0.5
            print(f"La racine carrée de {nombre} est: {resultat}")
        else:
            print("erreur ! Veuillez entrer un nombre valide")