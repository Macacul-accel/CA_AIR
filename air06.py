# Retirer du tableau tous les noms qui comportent la lettre donnée en dernier argument

import sys

def control_sanitary_pass(name_list, letter):
        not_sick = []
        for x in name_list:
            if letter.lower() not in x.lower():
                not_sick.append(x)
        return ",".join(not_sick)

try:
    if len(sys.argv) < 3:
        sys.exit()
    else:
        args_list = sys.argv[1:-1]
        control = sys.argv[-1]
        print(control_sanitary_pass(args_list, control))

except:
    print("error")
    sys.exit()