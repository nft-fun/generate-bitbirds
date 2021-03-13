# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np

# library to interact with the operating system
import os

# library to generate random integer values
from random import seed
from random import randint

# gets path to be used in image creation mechanism, using os
dirname = os.path.dirname(__file__)

# sets final image dimensions as 480x480 pixels
# the original 24x24 pixel image will be expanded to these dimensions
dimensions = 480, 480

# tells how many times to iterate through the following mechanism
# which equals the number of birds
# e.g. 
# for x in range(0-200) 
# would generate 201 birds numbered 0-200
for x in range(0, 50):

    # using ETH block number as starting random number seed
    b=11981207
    seed(x+b)

    #head color - randomly generate each number in an RGB color
    hd = (randint(0, 256), randint(0, 256), randint(0, 256))
    c=randint(0,500)
    seed(c)

    #throat color - same as head color
    th = (randint(0, 256), randint(0, 256), randint(0, 256))
    d = randint(0,1000)
    seed(d)

    #eye "white" color
    # if random number between 1-1000 is 47 or less - Crazy Eyes!
    if d > 47:
        # normal eyes are always the same color
        ew = (240,248,255)
        ey = (0, 0, 0)
    else:
        # crazy eyes have the same (154, 0, 0) pupil and a random 'eye white' color
        ew = (randint(0, 256), randint(0, 256), randint(0, 256))
        ey = (154, 0, 0)
    e = randint(0,1000)
    seed(e)

    # beak color
    f = randint(0, 1000)
    if f > 500:
        # if random number is 501-1000 >> grey beak
        bk = (152, 152, 152)
    elif 500 >= f > 47:
        # 48-500 >> gold beak
        bk = (204, 172, 0)
    elif 47 >= f > 7:
        # 8 >> 47 >> red beak
        bk = (204, 0, 0) 
    else:
        # random number is 7 or less >> black beak
        bk = (0, 0, 0) 

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
        p = "pecker"
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