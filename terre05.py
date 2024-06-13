import sys

dividende = int(sys.argv[1])
diviseur = int(sys.argv[2])
if dividende >= diviseur > 0:
    resultat = int(dividende / diviseur)
    reste = dividende % diviseur
    print(f"{dividende} / {diviseur} = {resultat}")
    print(f"Reste: {reste}")
else:
    print("ERREUR")