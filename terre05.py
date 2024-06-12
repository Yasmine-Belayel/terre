dividende = input("Entrez le dividende ")
dividende_int = int(dividende)
diviseur = input("Entrez le diviseur ")
diviseur_int = int(diviseur)
if dividende_int >= diviseur_int > 0:
    resultat = dividende_int / diviseur_int
    resultat_int = int(resultat)
    rest = dividende_int % diviseur_int
    print(f"{dividende_int} / {diviseur_int} = {resultat_int}")
    print(f"Reste: {rest}")
else:
    print("ERREUR")