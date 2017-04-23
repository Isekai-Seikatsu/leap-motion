import Leap
from visual import *

controller=Leap.Controller()

scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)

hand_Demo=frame()
for _ in range(20):cylinder(frame=hand_Demo, color=(0.5,0.4,0.5))    #20 bones ,thumb has equal two bones

V_palm=arrow(color=(1,0,0))

V_tip=frame()
for _ in range(5):arrow(frame=V_tip, shaftwidth=1, color=(0,0,1))

scene.center.y+=200
while True:

            rate(1000)
            frame=controller.frame()
            for hand in frame.hands:

                V_palm.pos =hand.palm_position.to_tuple()
                V_palm.axis=hand.palm_velocity.to_tuple()

                iter_Vtip=iter(V_tip.objects)
                for p in hand.pointables:
                    tiparrow=next(iter_Vtip)
                    tiparrow.pos =p.tip_position.to_tuple()
                    tiparrow.axis=p.tip_velocity.to_tuple()

                iter_cy=iter(hand_Demo.objects)
                for finger in hand.fingers:
                    for i in range(4):
                        bone=finger.bone(i)
                        cy=next(iter_cy)
                        cy.pos =bone.prev_joint.to_tuple()
                        cy.axis=(bone.next_joint-bone.prev_joint).to_tuple()
                        cy.radius=bone.width/2
