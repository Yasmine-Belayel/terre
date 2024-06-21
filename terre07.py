import sys


if len(sys.argv) != 2:   
    print("Erreur! Merci de saisir UN SEUL argument pour exécuter le programme")
else:
    if sys.argv[1].isdigit():
        print("Erreur! Le programme accepte uniquement une chaîne de caractères")
    else:   
        print(f"Votre chaîne de caractères contient {len(sys.argv[1])} caractères")