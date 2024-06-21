import sys

if len(sys.argv) != 3:   
    print("Erreur! Merci de saisir deux arguments pour exécuter le programme")
else:
    try:
        base = int(sys.argv[1])
        exposant = int(sys.argv[2])
    except:
        print("Erreur! Veuillez entrer uniquement des chiffres")
    else:
        if exposant >= 0:
            resultat = base ** exposant
            print(f"{base} ** {exposant}: {resultat}")
        else:
            print("Erreur! Merci d'entrer des nombres valides")