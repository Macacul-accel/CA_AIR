# Créer une pyramide avec un nombre d'étage donné en caractère

import sys

def pyramide(letter, floors):
    pyramide_array = []
    x = int(floors) - 1
    i = 1
    while len(pyramide_array) != int(floors):
        step_by_step = ""
        step_by_step += f"{" " * x}{letter * i}"
        pyramide_array.append(step_by_step)
        x -= 1
        i += 2
    for j in pyramide_array:
        print(j)

try:
    if len(sys.argv) != 3:
        sys.exit()
    else:
        form = sys.argv[1]
        size = sys.argv[2]
        pyramide(form, size)
except:
    print("error")
    sys.exit()