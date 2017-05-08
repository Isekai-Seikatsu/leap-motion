import Leap
from visual import *
from time import clock

controller=Leap.Controller()

scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)
hand_Demo=frame()
for _ in range(20):cylinder(frame=hand_Demo,color=(0.5,0.4,0.5))    #20 bones ,thumb has equal two bones
#arm=cylinder(color=(0.5,0.4,0.5))
scene.center.y+=100
t=clock()
ct=controller.now()
while True:

            #rate(100)
            sleep(0.01)
            frame=controller.frame()
            fps=frame.current_frames_per_second
            #t1,t2=frame.timestamp,controller.now()
            #print frame.timestamp/1000000.0, controller.now()/1000000.0,  t1 == t2

            print int((clock()-t)*1000000), (controller.now()-ct)
            t=clock()
            ct=controller.now()


            for hand in frame.hands:

                iter_cy=iter(hand_Demo.objects)
                for finger in hand.fingers:
                    for i in range(4):
                        bone=finger.bone(i)
                        cy=next(iter_cy)
                        cy.pos =bone.prev_joint.to_tuple()
                        cy.axis=(bone.next_joint-bone.prev_joint).to_tuple()
                        cy.radius=bone.width/2
                '''
                arm.pos=hand.arm.elbow_position.to_tuple()
                arm.axis=(hand.arm.wrist_position-hand.arm.elbow_position).to_tuple()
                arm.radius=hand.arm.width/2'''
