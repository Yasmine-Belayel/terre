import string


alphabet = ""
for lettres in string.ascii_letters:
    if lettres.islower():
     alphabet += lettres

exemple = input("Entrez une lettre alphabétique ")
exemple_min = exemple.lower()
indice = alphabet.index(exemple_min)
reste = alphabet[indice:]
print(reste)
print()