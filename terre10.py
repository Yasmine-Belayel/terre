import sys

arg = sys.argv
if len(arg) != 2:
    print("Erreur! Merci d'entrer uniquement UN SEUL argument")
elif not arg[1].isdigit():
    print("Merci d'entrer uniquement un nombre entier naturel")
else:    
    n = int(arg[1])
    if n == 0 or n == 1:
        print(f"{n} n'est pas un nombre premier")
    else:
        i = 2
        racine_carree_n = n ** 0.5
        while i <= racine_carree_n and n % i != 0:
            i = i+1
        if i > racine_carree_n:
            print(f"{n} est un nombre premier")
        else:
            print(f"{n} n'est pas un nombre premier")
    