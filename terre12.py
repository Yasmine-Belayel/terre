from datetime import datetime
import sys

def h_format(t):
    h_12 = datetime.strptime(t, '%I:%M%p')
    h_24 = datetime.strftime(h_12, '%H:%M')

    print(h_24)

conversion = sys.argv[1]

h_format(conversion)