# Afficher le contenu d'un fichier donné en argument

import sys

# file name forair.txt
def read_file(file_name):
    reading = open(file_name, "r")
    return reading.read()

try:
    if len(sys.argv) != 2:
        sys.exit()
    else:
        file = sys.argv[-1]
        print(read_file(file))
except:
    print("error")
    sys.exit()
