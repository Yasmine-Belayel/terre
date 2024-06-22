from datetime import datetime
import sys

def h_format(t):
    h_24 = datetime.strptime(t, '%H:%M')
    h_12 = datetime.strftime(h_24, '%I:%M%p')

    print(h_12)

conversion = sys.argv[1]

h_format(conversion)