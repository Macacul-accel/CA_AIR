# Retourner la valeur qui n'a pas de paire

import sys

def undercover(args_list):
    intruder = 0
    while intruder != len(args_list):
        try_args_list = args_list[:]
        try_args_list.pop(intruder)
        if args_list[intruder] in try_args_list:
            intruder += 1
            del try_args_list
        else:
            return args_list[intruder]

try:
    input_list = sys.argv[1:]

    if len(sys.argv) < 3:
        sys.exit()
    else:
        print(undercover(input_list))

except:
    print("error")
    sys.exit()