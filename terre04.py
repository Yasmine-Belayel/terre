nombre_str = input("Veuillez insérer un nombre entier SVP: ")
nombre_int = int(nombre_str)
reste = nombre_int % 2
if reste == 0:
    print(f"le nombre {nombre_int} est pair")
else:
    print(f"le nombre {nombre_int} est impair")
    