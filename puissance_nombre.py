def nombre_entier(a, b):
        int(a)
        int(b)
        return True


base = ""
while not base == " ":
    base = input("Entrez le nombre de base: ")
    exposant = input("Entrez le nombre exposant: ")
    if nombre_entier:
        try:
            base_int = int(base)
            exposant_int = int(exposant)
            if exposant_int > 0:
                resultat = base_int ** exposant_int
                print(f"{base_int} {exposant_int}")
                print(resultat)
                break
            else:
                print("L'exposant doit être un nombre positif")
        except:
            print("Erreur! Entrez des nombres valides")