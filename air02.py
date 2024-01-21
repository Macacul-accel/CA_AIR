# Transformer un tableau de chaîne de caractère en chaîne de caractère et les séparer avec un séparateur donné en dernier argument

import sys

def gather(array_of_str, separator):
    string_format = ""
    for x in range(len(array_of_str)):
        if x < len(array_of_str) - 1:
            string_format += f"{array_of_str[x]}{separator}"
        else:
            string_format += f"{array_of_str[x]}" 
    return string_format

try:
    input_array = sys.argv[1:-1]
    input_separator = sys.argv[-1]
    
    if len(sys.argv) < 3:
        sys.exit()
    else:
        print(gather(input_array, input_separator))

except:
    print("error")
    sys.exit()
