# Effectuer une opération sur chaque entier d'une liste avec le dernier argument

import sys

def on_all(nb_list, operator):
    result_array = []
    sum_substract = operator[0]
    used_number = int(operator[1:])
    for x in nb_list:
        if sum_substract == "-":
            result_array.append(int(x) - used_number)
        else:
            result_array.append(int(x) + used_number)
    final_result = " ".join(map(str, result_array))
    return final_result

try:
    if len(sys.argv) < 3:
        sys.exit()
    else:
        args_list = sys.argv[1:-1]
        operator = sys.argv[-1]
        print(on_all(args_list, operator))

except:
    print("error")
    sys.exit()