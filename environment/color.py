from visual import *

scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)

R,G,B=135,206,250

ball=sphere(color=(R/255.0,G/255.0,B/255.0))


for R in range(0,256,10):
    for G in range(0,256,10):
        for B in range(0,256,10):
                ball.color=(R/255.0,G/255.0,B/255.0)
                sleep(0.001)
