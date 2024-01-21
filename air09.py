# Decaler tous les arguments un cran vers la gauche (le premier devient le dernier)

import sys

def rotate():
    list_args = sys.argv[1:]
    final_array = []
    if len(sys.argv) < 3:
        sys.exit()
    else:
        x = 1
        while x != len(list_args):
            final_array.append(list_args[x])
            x += 1
        else:
            final_array.append(list_args[0])
    return final_array

try:
    print(", ".join(rotate()))
except:
    print("error")
    sys.exit()