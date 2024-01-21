# Afficher une chaîne de caractère en évitant les doublons

import sys

def error_handling():
    if len(sys.argv) != 2:
        return sys.exit()
    else:
        return True

def nodouble():
    if error_handling():
        phrase = sys.argv[1]
        sentence = ""
        x = 0
        while x != len(phrase):
            if len(sentence) == 0:
                sentence += f"{phrase[x]}"
                x += 1
            elif phrase[x] == sentence[-1]:
                x += 1
            else:
                sentence += f"{phrase[x]}"
                x += 1
        return sentence
    
try:
    print(nodouble())

except:
    print("error")
    sys.exit()
                