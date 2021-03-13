# BitBirds generation script
# Intro
This is published under MIT license, which means you can do whatever you want with it - entirely at your own risk.

Please don't be an asshole... this is, like, grassroots and stuff. 

Specifically I'm asking you in good faith not to directly knock off the BitBirds project, or otherwise try to screw me over for sharing this. Do not use this for anything hateful or discriminatory.

# Setting the expectations
As I've found to be the case with many templatized assets, folks new to this may struggle with setting up the dependencies. Often in technology, setting up something like PIP (a python asset installation tool) isn't something the developer thinks about in a given project because it has been on their computer for months or years. 

Even having set up a number of dependencies just a few weeks ago for this project, I don't remember exactly how I worked through the various error messages. When you try to run the code if it fails there will often be some useful nugget of an error code buried in the cryptic response blob. As a rule for life - Google is your friend, and others have probably encountered your exact error message if you look long enough. When asking questions on discord, stackoverflow, or wherever try to tell very specifically what you've tried, what you expect as the result, and what issue you're encountering. That'll get a lot more useful feedback than just shouting HALP.

# Dependencies
From memory the things I needed to setup were:

Python 3 (default on my mac was python 2.7)

PIP - an installation mechanism for python assets. 

IIRC I needed to use some special command with python 3 to use pip as an installation mechanism for the items below- perhaps 'pip3 install ...' rather than 'pip install ...'?

Pillow - asset to generate images - installed with pip

NumPy - asset to work with arrays - installed with pip

I don't *Think* I had to install 'random' to use the number randomization but might have.

As you're setting this up please reach out to me on discord or twitter if you encounter specifics not mentioned in here and I'll add them for posterity.

# How this script works
The video I've put on youtube will go into more depth, but to summarize:
We are iterating through a 'loop' for each bird. The loop starts with a 'seed number' that is used to deterministically generate pseudo-random numbers. I say deterministically and pseudo random because from the same seed number the 'random' output will always be the same. 

There is then a 'chain' of additional random numbers generated from each other that are used to define all of the variables about the birds. Many of the attributes generate a random number between 1-1000 and use that for a logical statement.

- Head color and throat color are a random 1-255 number generated into each of the 3 RGB values in a color.
- Eye color looks at a random number between 1-1000 and if it's 47 or less, will give the bird crazy eyes. Crazy eyes always have the same pupil color (154, 0, 0) and then generate a random color for the 'white of the eye,' in the same way the head and throat color are generated.
- Beak color is determined by an evaluation of another 1-1000 'random' number. Grey is most common, gold is also common, red is rare, and black is very rare.

The bird images are 24x24 arrays of variables, representing every pixel in the final image. There are four different arrays in the script for each type of bird. I've used variables with two letters for each different color, so as to keep the 'matrix' of pixel variables easy to see and work with. 

The script uses another 1-1000 'random' number to decide which of the bird type templates to use. Basic bird is most common, at about 75% probability. Jay has a 15% probability, woodpecker has 6%, eagle has 3.5%, and cockatoo has half a percent probability.

From there, you're just about home free. The script sizes the generated bird from 24 pixels x 24 pixels up to 480 pixels x 480 pixels. It generates the image file path, and saves the image into the folder 'bird_images.'

Then it goes right back to the top of the loop, and does it again for the next bird, until the number of defined loops is completed. 

# Wrap up
I really hope this inspires someone to take up coding and expand their horizons! I certainly wouldn't profess to be a professional coder, but I am a technologist in my day job and have found it a fulfilling and rewarding life path.  Looking more specifically - I would go so far as to say this BitBirds project has been a life changing one for me. The community that has popped up around it already has been inspiring and I'm excited to see it grow in the years to come.

If would like to show your thanks for this shared asset I'd encourage you to plant some trees! https://onetreeplanted.org/collections/all
If you feel absolutly compelled to send ETH or NFTs to me directly, please know that it is not necessary, but the BitBirds hardware wallet address is: 0x1fd146a5e6152c5ACd3A013fBC42A243e4DfCe63

