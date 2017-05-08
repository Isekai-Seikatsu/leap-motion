from visual import *
from random import random,choice,shuffle
from rasengan_sampling import rgb_data
scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)
ball=sphere()

R,G,B=135,206,250


while True:

    #ball.color=(random(), random(), random())
    '''
    R,G,B = choice(rgb_data.rasencolor)
    rate(100)
    ball.color=(R/255.0,G/255.0,B/255.0)
    '''
    shuffle(rgb_data.rasencolor)
    for R,G,B in rgb_data.rasencolor:
        rate(100)
        ball.color=(R/255.0,G/255.0,B/255.0)
