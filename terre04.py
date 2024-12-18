import sys

number = int(sys.argv[1])
if len(number) != 2:   
    print("Erreur! Merci de saisir UN SEUL argument pour exécuter le programme")
elif sys.argv[1].isalpha():
    print("Erreur! Le programme accepte uniquement des chiffres")
rest = number % 2
if rest == 0:
    print(f"le nombre {number} est pair")
else:
    print(f"le nombre {number} est impair")
    