# Vérifier si les exo sont présents dans le répertoire et s'ils sont fonctionnels

import subprocess

# Fichier avec input et output attendu "resultat_metexo.txt"
def get_py_files():
    py_files = []
    op = open("resultat_metexo.txt", "r")
    for files in op:
        if ".py" in files:
            py_files.append(files[:8])
    return py_files

def check_if_running(file_name):
    result = subprocess.run(f"python3 {file_name}", capture_output=True, text=True, shell=True)
    if result.stdout.strip():
        return True

def check_good_script(file_name):
    script_input = subprocess.run(f"cat resultat_metexo.txt | grep -A1 {file_name} | grep -v {file_name}", 
                                  capture_output=True, text=True, shell=True)
    script_result = subprocess.run(f"python3 {file_name} {script_input.stdout.strip()}",
                                   capture_output=True, text=True, shell=True)
    if script_result.stdout.strip() != "error":
        return True


total_test = 0
total_success = 0
for x in get_py_files():
    if check_if_running(x):
        print(f"{x} (1/2) :\033[1;32;40m success\033[1;37;40m")
        total_test += 1
        total_success += 1
    else:
        print(f"{x} (1/2) :\033[1;31;40m failure\033[1;37;40m")
        total_test += 1
    if check_good_script(x):
        print(f"{x} (2/2) :\033[1;32;40m success\033[1;37;40m")
        total_test += 1
        total_success += 1
    else:
        print(f"{x} (2/2) :\033[1;31;40m failure\033[1;37;40m")
        total_test += 1
print(f"Total succes : {total_success}/{total_test}")

        # "\033[1;31;40m" # RED
        # "\033[1;32;40m" # Green