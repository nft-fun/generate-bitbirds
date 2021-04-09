# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to generate a CSV file
import csv

# library to match RGB values to the nearest named color
import webcolors

# library to make HTTP calls (to OpenSea API)
import requests

# library to pause execution (for OpenSea API throttle)
import time
# import json

# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

# lor color matching
from webcolors import CSS3_HEX_TO_NAMES

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 480, 480

# prepares CSV file to be created, defines delimiter, and columns
with open((dirname + '/data/birds.csv'), 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow( ['Number'] + ['Full match'] + ['OpenSea name'] + ['Name match'] + ['Gen-script type'] + ['OpenSea type'] + ['Type match'] + ['Gen-script eyes'] + ['OpenSea eyes'] + ['Eye match'] + ['Eye color(if crazy)'] + ['Crazy eye actual'] + ['Crazy eye closest'] + ['Gen-script beak'] + ['OpenSea beak'] + ['Beak match'] + ['Main head color'] + ['Exact HTML/CSS head color'] + ['Closest head color'] + ['Secondary color'] + ['Exact HTML/CSS secondary color'] + ['Closest secondary color'] + ['Description'])
 
    # tells how many times to iterate through the following mechanism
    # which equals the number of birds
    # e.g. 
    # for x in range(0-200) 
    # would generate 201 birds numbered 0-200
    # for x in range(0, 1500):
    for x in range(0, 100):
        print('x: ' + str(x))

        if x != 423:

            # if x > 422:
            #     x = x-1

            # using ETH block number as starting random number seed
            b=11981207
            seed(x+b)

            # head color - randomly generate each number in an RGB color
            hd1 = randint(0, 256)
            hd2 = randint(0, 256)
            hd3 = randint(0, 256)
            hd = (hd1, hd2, hd3)
            # hd = (0, 0, 0)

            # gets closest named color from head RGB value
            # borrowed from this fucking legend!!! https://www.semicolonworld.com/question/58066/convert-rgb-color-to-english-color-name-like-39-green-39-with-python
            def closest_colour(requested_colour):
                min_colours = {}
                for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
                    r_c, g_c, b_c = webcolors.hex_to_rgb(key)
                    rd = (r_c - requested_colour[0]) ** 2
                    gd = (g_c - requested_colour[1]) ** 2
                    bd = (b_c - requested_colour[2]) ** 2
                    min_colours[(rd + gd + bd)] = name
                return min_colours[min(min_colours.keys())]
            
            def get_colour_name(requested_colour):
                try:
                    closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
                except ValueError:
                    closest_name = closest_colour(requested_colour)
                    actual_name = 'NA'
                return actual_name, closest_name

            requested_colour = hd
            hd_actual_name, hd_closest_name = get_colour_name(requested_colour)
            # print("Actual colour name:", actual_name, ", closest colour name:", closest_name)

            # hd_friendly = webcolors.rgb_to_name(hd)
            # print(hd_friendly)
            c=randint(0,500)
            seed(c)

            #throat color - same as head color
            th1 =randint(0, 256)
            th2 = randint(0, 256)
            th3 = randint(0, 256)
            th = (th1, th2, th3)

            # gets closest named color from throat/secondary RGB value
            def closest_colour(requested_colour):
                min_colours = {}
                for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
                    r_c, g_c, b_c = webcolors.hex_to_rgb(key)
                    rd = (r_c - requested_colour[0]) ** 2
                    gd = (g_c - requested_colour[1]) ** 2
                    bd = (b_c - requested_colour[2]) ** 2
                    min_colours[(rd + gd + bd)] = name
                return min_colours[min(min_colours.keys())]
            
            def get_colour_name(requested_colour):
                try:
                    closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
                except ValueError:
                    closest_name = closest_colour(requested_colour)
                    actual_name = 'NA'
                return actual_name, closest_name

            requested_colour = th
            th_actual_name, th_closest_name = get_colour_name(requested_colour)
            # print("Actual colour name:", actual_name, ", closest colour name:", closest_name)

            d = randint(0,1000)
            seed(d)

            #eye "white" color
            # if random number between 1-1000 is 47 or less - Crazy Eyes!
            if d > 47:
                # normal eyes are always the same color
                ew = (240,248,255)
                eyes = 'normal'
                crazy_color = 'NA'
                ey = (0, 0, 0)
                ew_closest_name = 'NA'
                ew_actual_name = 'NA'
            else:
                # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
                ew = (randint(0, 256), randint(0, 256), randint(0, 256))
                eyes = 'crazy'
                crazy_color = ew
                ey = (154, 0, 0)

                # gets closest named color from crazy eye RGB value
                def closest_colour(requested_colour):
                    min_colours = {}
                    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
                        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
                        rd = (r_c - requested_colour[0]) ** 2
                        gd = (g_c - requested_colour[1]) ** 2
                        bd = (b_c - requested_colour[2]) ** 2
                        min_colours[(rd + gd + bd)] = name
                    return min_colours[min(min_colours.keys())]
                
                def get_colour_name(requested_colour):
                    try:
                        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
                    except ValueError:
                        closest_name = closest_colour(requested_colour)
                        actual_name = 'NA'
                    return actual_name, closest_name

                requested_colour = ew
                ew_actual_name, ew_closest_name = get_colour_name(requested_colour)

            e = randint(0,1000)
            seed(e)

            # beak color
            f = randint(0, 1000)
            if f > 500:
                # if random number is 501-1000 >> grey beak
                bk = (152, 152, 152)
                beak = 'grey'
            elif 500 >= f > 47:
                # 48-500 >> gold beak
                bk = (204, 172, 0)
                beak = 'gold'
            elif 47 >= f > 7:
                # 8 >> 47 >> red beak
                bk = (204, 0, 0) 
                beak = 'red'
            else:
                # random number is 7 or less >> black beak
                bk = (0, 0, 0) 
                beak = 'black'

            # background color
            bg = (238, 238, 238)
            # outline color
            ol = (0, 0, 0)

            basic_bird = [
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ew, ew, hd, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ey, ew, hd, ey, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, th, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, th, th, th, th, th, ol, bg, bg, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
            ]

            woodpecker = [
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ew, ew, hd, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ey, ew, hd, ey, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, bk, bk, bk, ol, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, ol, ol, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, th, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, th, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
            ]

            jay = [
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ew, ew, hd, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ey, ew, hd, ey, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, th, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, th, th, th, th, th, ol, bg, bg, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
            ]

            eagle = [
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ew, ew, hd, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, ey, ew, hd, ey, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, th, th, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
            ]

            cockatoo = [
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, ol, ol, th, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, bg, ol, th, ol, bg, ol, th, th, ol, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, ol, bg, ol, th, ol, ol, ol, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, ol, th, ol, bg, ol, th, th, th, ol, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, ol, th, th, ol, ol, ol, th, th, ol, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, ol, ol, th, th, th, ol, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, ol, th, th, th, hd, hd, hd, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, ol, ol, ol, ol, th, th, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, ol, th, th, th, hd, hd, ew, ew, hd, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, ol, ol, ol, hd, hd, ey, ew, hd, ey, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, th, hd, hd, hd, hd, hd, hd, hd, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, bk, bk, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, bk, bk, bk, bk, ol, ol, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, hd, hd, ol, ol, ol, ol, bg, bg, ol, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, ol, hd, hd, hd, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
                [bg, bg, bg, bg, bg, bg, bg, bg, ol, hd, th, th, th, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
            ]

            # choose which bird image to use
            seed(f)
            g = randint(0,1000)
            if g > 250:
                # if random number is 251 - 1000 >> basic bird
                pixels = basic_bird
                p = "basic"
            elif 250 >= g > 100:
                # 101 - 250 >> jay
                pixels = jay
                p = "jay"
            elif 100 >= g > 40:
                # 41 - 100 >> woodpecker
                pixels = woodpecker
                p = "woodpecker"
            elif 40 >= g > 5:
                # 6 - 40 >> eagle
                pixels = eagle
                p = "eagle"
            else:
                # if random number is 5 or less >> cockatoo!!
                pixels = cockatoo
                p = "cockatoo"

            # convert the pixels into an array using numpy
            array = np.array(pixels, dtype=np.uint8)

            # use PIL to create an image from the new array of pixels
            new_image = Image.fromarray(array)
            new_image = new_image.resize(dimensions, resample=0)
            imgname = dirname + '/bird_images/' + (str(x)) + '.png'
            new_image.save(imgname)

            # pauses to not over-query OpenSea API
            time.sleep(0.6)

            # deals with BitBird 423 being missed from the mintin process
            if x > 422:
                offset = x-1
            else:
                offset = x
            print('offset :' + str(offset))

            # calls the opensea API with the requests library, one bird at a time 
            # with the offset matching (roughly) the iteration number of the bird generation loop
            r = requests.get('https://api.opensea.io/api/v1/assets?collection=bit-birds&order_direction=asc&offset=' + (str(offset)) + '&limit=1')
            jsonResponse = r.json()
            http_response = r.status_code
            # pulls specific data points out of the json response from the OpenSea API
            name = jsonResponse['assets'][0]['name']
            description = jsonResponse['assets'][0]['description']

            print("HTTP status code: " + str(http_response))
            print('Name: ' + name)
            print('Description: ' + str(description))

            # handles the OpenSea trait responses, their order depends on rarity of trait so order is unpredictable
            traits = jsonResponse['assets'][0]['traits']
            length = len(traits)
            # print('Traits:')
            for i in range(length):
                # print(i)
                trait_type = jsonResponse['assets'][0]['traits'][i]['trait_type']
                value = jsonResponse['assets'][0]['traits'][i]['value']
                # print(trait_type + ' : ' + value)
                if trait_type == 'eyes':
                    os_eyes = value
                if trait_type == 'type':
                    os_type = value
                if trait_type == 'beak':
                    os_beak = value
            
            # print('OS Type: ' + os_type)
            # print('OS Eyes: ' + os_eyes)
            # print('OS Beak: ' + os_beak)
            print('hd: ' + str(hd))
            print('th: ' + str(th))

            # checks all of the TRUE/FALSE generated vs. OpenSea match columns
            if name == 'BitBird ' + str(x):
                name_match = True
            else:
                name_match = False

            if p == os_type:
                type_match = True
            else:
                type_match = False
            
            if eyes == os_eyes:
                eye_match = True
            else: 
                eye_match = False

            if beak == os_beak:
                beak_match = True
            else:
                beak_match = False

            # checks whether every evaluated comparison is a match
            if type_match == True and eye_match == True and beak_match == True and name_match == True:
                full_match = True
            else:
                full_match = False

            # adds a row to the CSV file
            row = x
            print('row :' + str(row))
            writer.writerow([row, full_match, name, name_match, p, os_type, type_match, eyes, os_eyes, eye_match, crazy_color, ew_actual_name, ew_closest_name, beak, os_beak, beak_match, hd, hd_actual_name, hd_closest_name, th, th_actual_name, th_closest_name, str(description)])
            print('----------------------')
        else:
            # a leftover from testing
            print('----------------------')


print('*******Done*******')