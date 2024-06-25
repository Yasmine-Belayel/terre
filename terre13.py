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
        for i in range(len(liste)):
            min_index = i
            for j in range(i + 1, len(liste)):
                if liste[j] < liste[min_index]:
                    min_index = j
            liste[i], liste[min_index] = liste[min_index], liste[i]

        print(liste[1])