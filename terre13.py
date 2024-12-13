import sys

arguments = sys.argv[1:]
condition = sys.argv[1] == sys.argv[2] or sys.argv[1] == sys.argv[3] or sys.argv[2] == sys.argv[3]
if condition or len(arguments) != 3:
    print("Erreur! Merci d'entrer 3 nombres entiers différents")
else:
    try:
        for i in arguments:
            liste = [int(i) for i in arguments]
            arg = int(i)
    except:
        print("Merci d'entrer uniquement des nombres entiers")
    else:
        for argument in liste:
            if i < i+1 < i+2:
        print(liste[1])