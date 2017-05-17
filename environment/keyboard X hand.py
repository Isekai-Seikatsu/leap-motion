import Leap
from keyboard import *

controller=Leap.Controller()

scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)
hand_Demo=frame()
for _ in range(20):cylinder(frame=hand_Demo,color=(0.5,0.4,0.5))    #20 bones ,thumb has a non-length bone
octave()
#scene.center.y+=100
while True:

            rate(100)

            frame=controller.frame()

            for hand in frame.hands:

                iter_cy=iter(hand_Demo.objects)

                for finger in hand.fingers:
                    for i in range(4):
                        bone=finger.bone(i)
                        cy=next(iter_cy)
                        cy.pos =bone.prev_joint.to_tuple()
                        cy.axis=(bone.next_joint-bone.prev_joint).to_tuple()
                        cy.radius=bone.width/2
