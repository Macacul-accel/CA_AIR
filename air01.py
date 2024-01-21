# Découper la chaîne de caractère selon le deuxième argument donné

import sys

def split_by(str_to_cut, separator):
    cutted_sentence = []
    i = 0
    for x in range(len(str_to_cut) - len(separator) + 1):
        if str_to_cut[x:x + len(separator)] == separator:
            separator_index = x
            first_part = str_to_cut[i:separator_index]
            cutted_sentence.append(first_part)
            i += len(first_part) + len(separator)
        elif x == len(str_to_cut) - len(separator):
            second_part = str_to_cut[i:]
            cutted_sentence.append(second_part)
    for j in range(len(cutted_sentence)):
        print(cutted_sentence[j])

try:
    input_arg = sys.argv[1]
    input_separator = sys.argv[2]

    if len(sys.argv) != 3:
        sys.exit()
    else:
        split_by(input_arg, input_separator)

except:
    print("error")
    sys.exit()