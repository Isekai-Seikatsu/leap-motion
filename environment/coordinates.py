import Leap
from maze import *

controller=Leap.Controller()

scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5))
ball=sphere(color=(0.5,0.4,0.5))
w,h=5,5#
maze=create(make_maze( w, h))
D3=( length*(w*4.0+1), height*(h*4.0+1), width )

maze.pos=( (-D3[0]+length)/2.0, (D3[1]-height)/2.0)
print maze.pos
while True:
    #try:
        rate(1000)
        if controller.is_connected:
            frame=controller.frame()
            interaction_box = frame.interaction_box
            for hand in frame.hands:
                #is_right=hand.is_right
                #ball.color=color.red if is_right else color.blue
                pos = interaction_box.normalize_point(hand.palm_position)#,False)
                x=pos.x*D3[0]-D3[0]/2.0
                y=pos.y*D3[1]-D3[1]/2.0
                z=pos.z*D3[2]-D3[2]/2.0
                ball.pos=(x,y,z)
                #if pos.x>=1 and y<-D3[1]/2.0+4*height and y>-D3[1]/2.0+height:
                #        delete(maze)
                #        maze=create(make_maze( w, h))
                #        maze.pos=( (-D3[0]+length)/2.0, (D3[1]-height)/2.0)

                
                
    #except:
    #    print'break out'
    #    break
