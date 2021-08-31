#This script is used to generate a dataset of bitbirds images.
#you need to tell how many bitbirds images data should be in these csv files.each image will be in form of 24,24,3.
#example - if we want 1 image in dataset so:
     #'bitbirds_dataset' file will have 24 rows and 24 columns for this image and wach cell will have 3 values for RGB.
     #'bitbirds_target' file will have one row which is the name of bird
#another example - if we want 10 image in dataset so:
     #'bitbirds_dataset' file will have 240 rows and 24 columns. and first 24 rows will belongs to first image and next 24 rows (i.e. 25 to 48) will belongs to second image and so on till 10th image.
     #'bitbirds_target' file will have ten rows which are the names of respective birds of these 10 images




# Built with python 3, dependencies installed with pip 
# library to generate images - Pillow 
# https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image

# library to work with arrays 
# https://numpy.org/
import numpy as np
import pandas as pd

# library to interact with the operating system
import os,csv

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

#Define csv files of dataset one file name 'bitbirds_dataset' contains birds images. each image is of size 24,24,3 stores in 24 rows and 24 columns in CSV file.
#another 'bitbirds_target' file contains respective bird name of each image.

fil_name = 'bitbirds_dataset'
array = []
with open(fil_name+'.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows(array)
bird_name=[]
fi_name = 'bitbirds_target'
with open(fi_name+'.csv', 'w', newline='\n') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerows('')

images = int(input(' Enter no. of images you want to be in dataset e.g. 1,2 etc. '))
for x in range(0, images):

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

    # store 3D pixels array in csv file
    fil_name = 'bitbirds_dataset'
    with open(fil_name+'.csv', 'a', newline='\n') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerows(array)
    bird_name.append([p])
    
    
# store bitbirds names in csv file
fi_name = 'bitbirds_target'
with open(fi_name+'.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(bird_name)
    
# To read the data set uncomment below

##with open(fil_name+'.csv', 'r') as f:
##  reader = csv.reader(f)
##  array = list(reader)
##
##
##nwexamples = []
##for row in array:
##    nwrow = []
##    for r in row:
##        nwrow.append(r[1:-1].split(' '))
##    nwexamples.append(nwrow)
##print(nwexamples)
