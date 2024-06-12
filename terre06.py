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