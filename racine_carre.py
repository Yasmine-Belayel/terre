nombre = ""
while True:
    nombre = input("Entrez un nombre entier positif: ")
    if nombre.isdigit():
        nombre_int = int(nombre)
        resultat = nombre_int ** 0.5
        print(f"La racine carrée de {nombre_int} est: {resultat}")
        break
    else:
        print("erreur ! Veuillez entrer un nombre valide")