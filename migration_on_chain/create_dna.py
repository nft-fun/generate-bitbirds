import pandas as pd
import os
import csv
# import json
from helper_functions import create_type_trait, create_beak_traits, create_eye_traits, create_head_traits,create_throat_traits, query_opensea,process_csv, write_summary_json, write_metadata_json, append_glitch_collection, bcolors, mode

from dotenv import load_dotenv
load_dotenv()

# Retrieves opensea key from .env and generates http headers
OS_KEY = os.getenv('OS_KEY')
headers = {'X-API-KEY': OS_KEY, 'Accept': 'application/json'}

# Retrieves bird_data csv from local folder
file_path = "./bird_data.csv"
data = pd.read_csv(file_path, sep=',')
if mode == 'log':
    print(data)

# Preps summary.json file to receive data 
with open ('./generated_files/summary.json','w') as jsonfile:
    jsonfile.write('{"bird_summary": []}')

#Preps summary.csv file to receive data
with open(('./generated_files/summary.csv'), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow( ['Number'] + ['OS Name'] + ['OS Token ID'] + ['DNA'] + ['Description'])
 
    # Loops once per bird
    for i in range(0,1500):
    # for i in range(415,430):
        
        if i != 423:

            print(f'{bcolors.HEADER}{bcolors.BOLD}\n-------- i:{i} --------{bcolors.ENDC}')

            # Processes trait variables from csv data value
            number, bird_type, eye_rgb, bk_color, hd_rgb, th_rgb, description, glitch, eyes = process_csv(i,data)

            print(f'{bcolors.OKGREEN}\n--- Bird number: {number} ---{bcolors.ENDC}')

            #Creates binary traits with functions in helper_functions.py
            dna_type = create_type_trait(bird_type)
            dna_beak = create_beak_traits(bk_color)
            dna_eye, eye_red, eye_green, eye_blue, pupil_red, pupil_green, pupil_blue = create_eye_traits(eyes, eye_rgb)
            hd_red, hd_green, hd_blue = create_head_traits(hd_rgb)
            th_red, th_green, th_blue =  create_throat_traits(th_rgb)
            if glitch == 'YES':
                glitch_bin = '00000001'
            else:
                glitch_bin = ''

            # Create full binary dna 
            full_bin_dna = f'{dna_type}{dna_beak}{dna_eye}{eye_red}{eye_green}{eye_blue}{pupil_red}{pupil_green}{pupil_blue}{hd_red}{hd_green}{hd_blue}{th_red}{th_green}{th_blue}{glitch_bin}'
            if mode == 'log':
                print(f'\n{bcolors.OKGREEN}Full binary DNA: {full_bin_dna}{bcolors.ENDC}')

            final_dna = int(full_bin_dna,2)
            
            os_token_id, name = query_opensea(i, headers)

            print(f'\n{bcolors.OKGREEN}{bcolors.BOLD}Summary{bcolors.ENDC}\n {bcolors.OKCYAN}Bird Number: {number}\n OS Name: {name}\n OS Token ID: {os_token_id}\n New DNA: {final_dna}{bcolors.ENDC}\n')

            # adds a row to the summary.csv file
            writer.writerow([number, name, f'_{os_token_id}', f'_{final_dna}', description])

            write_metadata_json(number, description, bird_type, bk_color, eyes)

            if glitch == 'YES':
                append_glitch_collection(i)

            #Adds an array item to the summary.json file
            write_summary_json(number,name,os_token_id,final_dna,description)



        else:
            print(f'{bcolors.WARNING}\n\n--- i=423 ... skipping ---\n\n{bcolors.ENDC}')










