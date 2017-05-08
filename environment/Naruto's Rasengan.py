import Leap
from visual import *
from my_color import rasengan_color

controller=Leap.Controller()

scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)
hand_Demo=frame()
for _ in range(20):cylinder(frame=hand_Demo, color=(0.5,0.4,0.5))    #20 bones ,thumb has a non-length bone

rasengans = frame()
charging=False

scene.center.y+=180
while True:

            rate(100)
            frame=controller.frame()

            for hand in frame.hands:
                #product rasengan
                if hand.grab_strength==1 and not(charging) :
                    rasengan= sphere(frame=rasengans, v=Leap.Vector.zero, rc=rasengan_color())
                    charging = True
                if charging:
                    rasengan.pos=hand.sphere_center.to_tuple()
                    rasengan.radius=hand.sphere_radius
                    if hand.palm_velocity.magnitude >500:#500 mm/s
                        rasengan.v=hand.palm_velocity
                        charging=False
                #hands figure
                iter_cy=iter(hand_Demo.objects) #
                for finger in hand.fingers:
                    for i in range(4):
                        bone=finger.bone(i)
                        cy=next(iter_cy)
                        cy.pos =bone.prev_joint.to_tuple()
                        cy.axis=(bone.next_joint-bone.prev_joint).to_tuple()
                        cy.radius=bone.width/2
            #rasengans moving and color changing
            for i in rasengans.objects:
                i.color=next(i.rc)
                i.pos+=vector((i.v*0.01).to_tuple())
                if i.pos.mag>1500:#1500 mm around
                    i.visible=False
                    del i
