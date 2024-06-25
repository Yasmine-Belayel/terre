import sys

arguments = sys.argv[1:]
try:
    for i in arguments:
        liste = [int(i) for i in arguments]
except:
    print("Erreur! Merci d'entrer uniquement des nombres entiers")
else:
    n = len(liste)
    triee = True
    for i in range(n-1):
        for j in range(i+1, n):
            if liste[i] > liste[j]:
                triee = False
                break
        if not triee:
            break
    if triee:
        print("triée")   
    else:
        print("pas triée")

    