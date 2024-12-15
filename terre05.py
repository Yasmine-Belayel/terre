import sys

dividend = int(sys.argv[1])
divisor = int(sys.argv[2])
if dividend >= divisor > 0:
    result = int(dividend / divisor)
    rest = dividend % divisor
    print(f"{dividend} / {divisor} = {result}")
    print(f"Reste: {rest}")
else:
    print("ERREUR")