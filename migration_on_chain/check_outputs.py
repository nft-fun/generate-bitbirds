import pandas as pd
import os
import csv
from test_helper_functions import process_summary, process_dna, process_traitlist, check_traits, bcolors

file_path = "./generated_files/summary.csv"
data = pd.read_csv(file_path, sep=';')

file_path2 = "./bird_data.csv"
data2 = pd.read_csv(file_path2, sep=',')

check_result = ''
for i in range (0,1500):
    if i != 423:
        if i > 422:
            o = i - 1
        else:
            o = i

        print(f'{bcolors.HEADER}{bcolors.BOLD}\n-------- i:{i} --------{bcolors.ENDC}')

        number, os_name, os_token_id, dna, description = process_summary(o, data)

        traitlist, glitch = process_dna(dna)

        bird_type, beak, eyes, eye_rgb, pupil_rgb, head_rgb, throat_rgb, glitch = process_traitlist(traitlist, glitch)

        status, status_msg = check_traits(i, data2, number, bird_type, beak, eyes, eye_rgb, pupil_rgb, head_rgb, throat_rgb, glitch)

        if status == 'OK':
            print(f'{bcolors.OKBLUE}\n{status_msg}\nStatus:{status}\n{bcolors.ENDC}')
        else:
            print(f'\n\n{bcolors.FAIL}Status:{status}\nStatus Message: {status_msg}{bcolors.ENDC}')
            check_result = f'{check_result} \n\n~~\n\n{status_msg}'
    else:
        print(f'{bcolors.WARNING}\n\n--- i=423 ... skipping ---\n\n{bcolors.ENDC}')


print(f'\n\n{bcolors.HEADER} ~~~Done~~~ {check_result}{bcolors.ENDC}\n\n')
