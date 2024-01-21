# Créer un tableau et ajouter le dernier argument donné dans l'ordre croissant

import sys

def add_new_number(array_number, new_elmt):
    array_with_new_elmt = []
    x = 0
    while len(array_with_new_elmt) != len(array_number) + 1:
        if int(array_number[x]) < int(new_elmt):
            array_with_new_elmt.append(array_number[x])
            x += 1
            if x == len(array_number) - 1:
                if array_number[x] < new_elmt:
                    array_with_new_elmt.append(array_number[x])
                    array_with_new_elmt.append(new_elmt)
        else:
            if new_elmt in array_with_new_elmt:
                array_with_new_elmt.append(array_number[x])
                x += 1
            else:
                array_with_new_elmt.append(new_elmt)
    return array_with_new_elmt

try:
    if len(sys.argv) < 4:
        sys.exit()
    else:
        args_numbers = sys.argv[1:-1]
        to_add_number = sys.argv[-1]
        print(" ".join(map(str, add_new_number(args_numbers, to_add_number))))
    
except:
    print("error")
    sys.exit()