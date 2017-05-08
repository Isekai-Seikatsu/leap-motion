from random import random,shuffle
from rasengan_sampling import rgb_data

def rasengan_color():
    while True:
        shuffle(rgb_data.rasencolor)
        for R,G,B in rgb_data.rasencolor:
            yield (R/255.0,G/255.0,B/255.0)

def randcolor():
    while True:
        yield (random(), random(), random())
