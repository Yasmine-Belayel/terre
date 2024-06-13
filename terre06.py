chaine = ""
while True:
    chaine = input("Entrez votre texte: ")
    chaine_alphab = chaine.isalpha()
    if chaine_alphab:
        inverse_chaine = chaine[::-1]
        print(inverse_chaine) 
        break
    else:
        print("Erreur! Veuillez entrer des lettres")


"""import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
lettre_donnee = sys.argv[1:]
for lettre_donnee in alphabet:
    indice = alphabet.index(lettre_donnee)
print(indice)"""