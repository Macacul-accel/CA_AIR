# Fusionner et trier deux listes d'entiers triés

import sys

def array_fusion(array_1, array_2):
    final_array = []
    x = 0
    i = 0
    while len(final_array) != len(array_1) + len(array_2):
        if x >= len(array_1):
            final_array.append(array_2[i])
            i += 1
        elif i >= len(array_2):
            final_array.append(array_1[x])
            x += 1
        else:
            if array_1[x] < array_2[i]:
                final_array.append(int(array_1[x]))
                x += 1
            else:
                final_array.append(int(array_2[i]))
                i += 1
    return final_array

def array_cut():
    if len(sys.argv) < 5:
        sys.exit()
    else:
        input_args = sys.argv[1:]
        x = input_args.index("fusion")
        first_array = input_args[:x]
        scnd_array = input_args[x + 1:]
    return array_fusion(first_array, scnd_array)


try:
    print(" ".join(map(str, array_cut())))
except:
    print("error")
    sys.exit()