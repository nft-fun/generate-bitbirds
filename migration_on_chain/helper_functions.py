import time
import requests
import json
from summary_template import summary_template as st
from meta_template import metadata_template 


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# beaks = {
#     'grey' : '(152, 152, 152)', 
#     'gold' : '(204, 172, 0)', 
#     'red' : '(204, 0, 0)', 
#     'black' : '(0, 0, 0)'
#     }


mode = 'clean'


# Processes the csv to useful variables, eyes>final_eyes, beak>gen-script
def process_csv(i,data):
    number = data.values[i][0]
    bird_type = data.values[i][6]
    eye_rgb = data.values[i][11]
    bk_color = data.values[i][14]
    hd_rgb = data.values[i][17]
    th_rgb = data.values[i][20]
    description = data.values[i][23]
    glitch = data.values[i][24]
    eyes = data.values[i][25]

    if mode == 'log':
        print(f'Bird number: {number}\nBird type: {bird_type}\nEyes: {eyes}\nCrazy color: {eye_rgb}\nBeak: {bk_color}\nHead: {hd_rgb}\nThroat: {th_rgb}\nDescription: {description}\nGlitch: {glitch}')
    return number, bird_type, eye_rgb, bk_color, hd_rgb, th_rgb, description, glitch, eyes


# Creates a binary trait from a 0-255 input number
def create_bin_trait(trait_num):
    if mode == 'log':
        print(f'working on binary DNA for trait {trait_num}')
    if int(trait_num) == 256:
        print(f'{bcolors.FAIL} TRAIT IS 256{bcolors.ENDC}')
        trait_num = 0
    bin_dna = bin(int(trait_num))
    # print(bin_dna)
    bin_dna_string = bin_dna.replace("0b","").zfill(8)
    return bin_dna_string


# Creates binary trait for bird type
def create_type_trait(bird_type):
    # Find type trait
    if bird_type == 'basic':
        dna_type = '00000001'
    elif bird_type == 'jay':
        dna_type = '00000010'
    elif bird_type == 'woodpecker':
        dna_type = '00000011'
    elif bird_type == 'eagle':
        dna_type = '00000100'
    elif bird_type == 'cockatoo':
        dna_type = '00000101'
    else:
        print('No types hit')
    if mode == 'log':
        print(f'\nBird type DNA: {dna_type}')
    return dna_type


# Creates binary traits for beak and beak rgb
def create_beak_traits(bk_color):
    # Find beak trait
    if bk_color == 'grey':
        dna_beak = '00000001'
    elif bk_color == 'gold':
        dna_beak = '00000010'
    elif bk_color == 'red':
        dna_beak = '00000011'
    elif bk_color == 'black':
        dna_beak = '00000100'
    else:
        print('No beaks hit')
    if mode == 'log':
        print(f'\nBeak DNA: {dna_beak}')
    return(dna_beak)


# Creates binary traits for eye type eye_rgb and puil rgb traits
def create_eye_traits(eyes, eye_rgb):
    # Find eyes trait
    if eyes == 'normal':
        dna_eye = '00000001'
        eye_red = '11110000'
        eye_green = '11111000'
        eye_blue = '11111111'
        pupil_red = '00000000'
        pupil_green = '00000000'
        pupil_blue = '00000000'
    elif eyes == 'crazy' or eyes == 'satanic':
        if eyes == 'crazy':
            dna_eye = '00000010'
        elif eyes == 'satanic':
            dna_eye = '00000011'
        # eye_red = str(bin(int(eye_rgb[0]))).zfill(8)
        # eye_green = str(bin(int(eye_rgb[1]))).zfill(8)
        # eye_blue = str(bin(int(eye_rgb[2]))).zfill(8)
        if mode == 'log':
            print(f'Crazy eye RGB: {eye_rgb}')
        eye_rgb = eye_rgb.replace("(","")
        eye_rgb = eye_rgb.replace(")","")
        eye_rgb_arr = eye_rgb.split(",")
        eye_red = create_bin_trait(eye_rgb_arr[0])
        eye_green = create_bin_trait(eye_rgb_arr[1])
        eye_blue = create_bin_trait(eye_rgb_arr[2])
        pupil_red = '10011010'
        pupil_green = '00000000'
        pupil_blue = '00000000'
    else:
            print('No eyes hit')
    if mode == 'log':
        print(f'\nEye binary DNA: {dna_eye}\n Eye R: {eye_red} \n Eye G: {eye_green}\n Eye B: {eye_blue}\n Pupil R: {pupil_red}\n Pupil G: {pupil_green}\n Pupil B: {pupil_blue}')

    return dna_eye, eye_red, eye_green, eye_blue, pupil_red, pupil_green, pupil_blue


# Creates binary head rgb traits
def create_head_traits(hd_rgb):
    if mode == 'log':
        print(f'\nHead rgb: {hd_rgb}')
    hd_rgb = hd_rgb.replace("(","")
    hd_rgb = hd_rgb.replace(")","")
    hd_rgb_arr = hd_rgb.split(",")
    hd_red = create_bin_trait(hd_rgb_arr[0])
    hd_green = create_bin_trait(hd_rgb_arr[1])
    hd_blue = create_bin_trait(hd_rgb_arr[2])
    if mode == 'log':
        print(f'Head trait binary - \n Head color R: {hd_red}\n Head color G: {hd_green}\n Head color B: {hd_blue}')
    return hd_red, hd_green, hd_blue


# Created binary secondary color rgb traits
def create_throat_traits(th_rgb):   
    if mode == 'log':
        print(f'\nThroat rgb: {th_rgb}')
    th_rgb = th_rgb.replace("(","")
    th_rgb = th_rgb.replace(")","")
    th_rgb_arr = th_rgb.split(",")
    th_red = create_bin_trait(th_rgb_arr[0])
    th_green = create_bin_trait(th_rgb_arr[1])
    th_blue = create_bin_trait(th_rgb_arr[2])
    if mode == 'log':
        print(f'Throat trait binary - \n Throat color R: {th_red}\n Throat color G: {th_green}\n Throat color B: {th_blue}')
    return th_red, th_green, th_blue


# Queries OpenSea to get original OS tokenID
def query_opensea(i, headers):
    time.sleep(1)
    if i > 422:
        offset = i-1
    else:
        offset=i
    url = f'https://api.opensea.io/api/v1/assets?collection=bit-birds&order_direction=asc&offset={offset}&limit=1'
    if mode == 'log':
        print(url)
    r = requests.get(url , headers=headers)
    if mode == 'log':
        print(r)
    jsonResponse = r.json()
    name = jsonResponse['assets'][0]['name']
    description = jsonResponse['assets'][0]['description']
    os_token_id = jsonResponse['assets'][0]['token_id']
    if mode == 'log':
        print(f'{bcolors.OKCYAN}Name: {name}\nDescription: {description}\nToken ID: {os_token_id}{bcolors.ENDC}\n\n')
    return os_token_id, name


# Writes to summary json file
def write_summary_json(number, name, os_token_id, dna, description):
    st["number"] = number
    st["os_name"] = name
    st["os_token_id"] = os_token_id
    st["dna"] = dna
    st["description"] = description
    if mode == 'log':
        print(st)
    with open('./generated_files/summary.json','r+') as file:
        file_data = json.load(file)
        file_data["bird_summary"].append(st)
        file.seek(0)
        json.dump(file_data, file, indent = 4)


# Writes to new metadata json file
def write_metadata_json(number, description, bird_type, beak, eyes):
    meta =  metadata_template
    meta["name"] = number
    meta["description"] = description
    meta["image"] = 'test'

    meta['attributes'][0]["trait_type"] = 'Bird Type'
    meta['attributes'][0]["value"] = bird_type.capitalize()

    meta['attributes'][1]["trait_type"] = 'Eyes'
    meta['attributes'][1]["value"] = eyes.capitalize()

    meta['attributes'][2]["trait_type"] = 'Beak'
    meta['attributes'][2]["value"] = beak.capitalize()

    if mode == 'log':
        print(meta)

    with open (f'./generated_files/metadata/{number}.json','w') as file:
        json.dump(meta, file, indent = 4)


def append_glitch_collection(number):
    with open(f'./generated_files/metadata/{number}.json','r+') as file:
            file_data = json.load(file)
            gc = '{ "trait_type": "Special", "value": "Glitch Collection" }'
            file_data["attributes"].append(json.loads(gc))
            file.seek(0)
            json.dump(file_data, file, indent = 4)

