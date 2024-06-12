import string

alphabet = ""
for lettres in string.ascii_letters:
    if lettres.islower():
     alphabet += lettres
print(alphabet)
print("")