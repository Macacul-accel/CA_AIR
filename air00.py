# Découper une chaîne de caratère en tableau

import sys

def str_to_array(str_to_split):
    separator = [chr(32), chr(9), chr(10)]
    new_array = []
    i = 0
    for x in range(len(str_to_split)):
        if str_to_split[x] in separator:
            separator_index = x
            word = str_to_split[i:separator_index]
            new_array.append(word)
            i += len(word) + 1
        elif x == len(str_to_split) - 1:
            word = str_to_split[i:]
            new_array.append(word)
    for j in range(len(new_array)):
        print(new_array[j])

try:
    input_args = sys.argv[1]
    if not input_args:
        sys.exit()
    elif len(sys.argv) != 2:
        sys.exit()
    else:
        str_to_array(input_args)

except:
    print("error")
    sys.exit()