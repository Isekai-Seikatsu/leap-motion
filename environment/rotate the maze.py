import Leap
from maze import *

controller=Leap.Controller()

scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5))

w,h=5,5#
D3=( length*(w*4.0+1), height*(h*4.0+1), width )
maze=create(make_maze( w, h), (-D3[0]+length)/2.0, (D3[1]-height)/2.0 )

while True:

            rate(100)
            frame=controller.frame()
            for hand in frame.hands:
                maze.up= hand.direction.to_tuple()
                maze.axis=hand.palm_normal.cross(hand.direction).to_tuple()
