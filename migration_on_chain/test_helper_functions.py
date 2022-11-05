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

mode = 'clean'

def process_summary(i, data):
    number = data.values[i][0]
    os_name = data.values[i][1]
    os_token_id = int(data.values[i][2][1:])
    dna = int(data.values[i][3][1:])
    description = data.values[i][4]

    print(f'{bcolors.OKCYAN}Number: {number}\nOS Name: {os_name}\nOS Token ID: {os_token_id}\nDNA: {dna}\nDescription: {description}{bcolors.ENDC}')

    return number, os_name, os_token_id, dna, description

def process_dna(dna):
    binary_dna = f'{dna:>08b}'
    if mode == 'log':
        print(f'\nBinary DNA (Converted from integer DNA): {binary_dna}')
        print(len(binary_dna))

    # # Pads binary DNA to be 72 characters by adding zeros to the front 
    if len(binary_dna) >= 120:
        if mode == 'log':
            print(f'{bcolors.WARNING}\nGlitch Collection{bcolors.ENDC}')
        padded_binary = binary_dna.zfill(128)
        glitch = 'YES'
    else:
        if mode == 'log':
            print(f'{bcolors.OKGREEN}\nNon glitch...{bcolors.ENDC}')
        padded_binary = binary_dna.zfill(120)
        glitch = 'None'
    if mode == 'log':
        print(f'\nPadded Binary: {padded_binary}')

    # # Makes the binary DNA a bit easier for humans to read 
    friendly_binary = padded_binary
    friendly_binary = " | ".join(friendly_binary[f:f+8] for f in range(0, len(friendly_binary), 8))
    if mode == 'log':
        print(f'\nFriendly binary: {friendly_binary}\n')


    traitlist = []
    trait_count = int(len(padded_binary)/8)
    for t in range(0,trait_count):
        bitshift = t*8
        trait = int(dna) >> bitshift & 255
        # Adds the identified trait to an array
        traitlist = [trait] + traitlist

    if mode == 'log':
        print(f'Trait list: {traitlist}')
    # Makes a friendly bar-separated attribute summary
    attr_list = ' | '.join(map(str,traitlist))
    if mode == 'log':
        print(f'Trait list2: {attr_list}')

    return traitlist, glitch

def process_traitlist(traitlist, glitch):
    if mode == 'log':
        print(traitlist[0])
        print(traitlist[1])
        print(traitlist[2])
        print(traitlist[3])
        print(traitlist[4])
        print(traitlist[5])
        print(traitlist[6])
        print(traitlist[7])
        print(traitlist[8])
        print(traitlist[9])
        print(traitlist[10])
        print(traitlist[11])
        print(traitlist[12])
        print(traitlist[13])
        print(traitlist[14])
        if glitch == 'YES':
            print(f'{bcolors.WARNING} Yes glitch {traitlist[15]}{bcolors.ENDC}')
    bird_type = ''
    beak = ''
    eyes = ''

    # Bird type
    if traitlist[0] == 1:
        bird_type = 'basic' 
    elif traitlist[0] == 2:
        bird_type = 'jay'
    elif traitlist[0] == 3:
        bird_type = 'woodpecker'
    elif traitlist[0] == 4:
        bird_type = 'eagle'
    elif traitlist[0] == 5:
        bird_type = 'cockatoo'

    beak = ''
    # Beaks
    if traitlist[1] == 1:
        beak = 'grey' 
    elif traitlist[1] == 2:
        beak = 'gold'
    elif traitlist[1] == 3:
        beak = 'red'
    elif traitlist[1] == 4:
        beak = 'black'

    # Eyes
    if traitlist[2] == 1:
        eyes = 'normal' 
    elif traitlist[2] == 2:
        eyes = 'crazy'
    elif traitlist[2] == 3:
        eyes = 'satanic'

    # Eye rgb
    eye_rgb = f'({traitlist[3]}, {traitlist[4]}, {traitlist[5]})'
    pupil_rgb = f'({traitlist[6]}, {traitlist[7]}, {traitlist[8]})'

    head_rgb = f'({traitlist[9]}, {traitlist[10]}, {traitlist[11]})'
    throat_rgb = f'({traitlist[12]}, {traitlist[13]}, {traitlist[14]})'

    # eye_rgb = eye_rgb.replace('256','0')
    # pupil_rgb = pupil_rgb.replace('256','0')
    # head_rgb = head_rgb.replace('256','0')
    # throat_rgb = throat_rgb.replace('256','0')




    print(f'\n\n{bcolors.OKGREEN}Result\n Bird Type: {bird_type}\n Beak: {beak}\n Eyes: {eyes}\n Eye RGB: {eye_rgb}\n Pupil RGB: {pupil_rgb}\n Head RGB: {head_rgb}\n Throat RGB: {throat_rgb}\n Glitch: {glitch}{bcolors.ENDC}')

    return bird_type, beak, eyes, eye_rgb, pupil_rgb, head_rgb, throat_rgb, glitch





def check_traits(i, data2, number, bird_type, beak, eyes, eye_rgb, pupil_rgb, head_rgb, throat_rgb, glitch):
    status = 'OK'
    status_msg = f'i={i}:'
    if mode == 'log':
        print(data2.values[i])


    # Check number
    if data2.values[i][0] == number:
        pass
    else:
        status = 'ERROR'
        status_msg = f'{status_msg}\nNUMBER ERROR - {data2.values[i][0]} != {number}'

    if data2.values[i][6] == bird_type:
        pass
    else:
        status = 'ERROR'
        status_msg = f'{status_msg}\nBIRD TYPE ERROR - {data2.values[i][6]} != {bird_type}'

    if data2.values[i][14] == beak:
        pass
    else:
        status = 'ERROR'
        status_msg = f'{status_msg}\nBEAK ERROR - {data2.values[i][14]} != {beak}'

    if data2.values[i][25] == eyes:
        pass
    else:
        status = 'ERROR'
        status_msg = f'{status_msg}\nEYES ERROR - {data2.values[i][25]} != {eyes}'

    if eyes == 'crazy':    
        print('\n\n---EYE RGB TEST---')
        print(data2.values[i][11])
        print(eye_rgb)
        if data2.values[i][11].replace('256','0') == eye_rgb:
            pass
        else:
            status = 'ERROR'
            status_msg = f'{status_msg}\nEYE RGB ERROR - {data2.values[i][11]} != {eye_rgb}'


    # print('\n\n---HEAD RGB TEST---')
    # print(data2.values[i][17])
    # print(head_rgb)
    if data2.values[i][17].replace('256','0') == head_rgb:
        pass
    else:
        status = 'ERROR'
        status_msg = f'{status_msg}\nHEAD RGB ERROR - {data2.values[i][17]} != {head_rgb}'

    # print('\n\n---THROAT RGB TEST---')
    # print(data2.values[i][20])
    # print(throat_rgb)
    if data2.values[i][20].replace('256','0') == throat_rgb:
        pass
    else:
        status = 'ERROR'
        status_msg = f'{status_msg}\nTHROAT RGB ERROR - {data2.values[i][20]} != {throat_rgb}'

    if data2.values[i][24] == glitch:
        pass
    else:
        status = 'ERROR'
        status_msg = f'{status_msg}\nGLITCH ERROR  - {data2.values[i][24]} != {glitch}'

    return status, status_msg



    