import string


alphabet_min = ""
for lettres in string.ascii_letters:
    if lettres.islower():
     alphabet_min += lettres
print(alphabet_min)
print("")
