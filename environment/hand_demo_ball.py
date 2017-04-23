import Leap
from visual import *

controller=Leap.Controller()

scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)
hand_Demo=frame()
for _ in range(25):sphere(frame=hand_Demo,color=(0.5,0.4,0.5))

while True:

            rate(1000)
            frame=controller.frame()
            interaction_box = frame.interaction_box
            for hand in frame.hands:
                joints=[]

                for finger in hand.fingers:  #append joints
                    for i in range(4):joints.append(finger.bone(i).prev_joint)
                    joints.append(finger.bone(i).next_joint)

                iter_j=iter(map(interaction_box.normalize_point, joints))   #raw_to_cooked

                for joint in hand_Demo.objects: #represent joints
                    vector_j=next(iter_j)
                    joint.pos=(vector_j.x*100-50, vector_j.y*100-50, vector_j.z*100-50)


                #index=fingers[1]
                #metacarpal=index.bone(0)
                #print metacarpal.prev_joint,hand.wrist_position
                #distal=index.bone(3)
                #intermediate=index.bone(2)
                #print distal.prev_joint,intermediate.next_joint
                #print hand.arm.width
                #print hand.palm_position.distance_to(hand.wrist_position)
                #basis=hand.basis
                #print basis.z_basis,hand.direction
                #print hand.grab_strength,hand.pinch_strength

                #pos = interaction_box.normalize_point(hand.palm_position)

                #ball.radius=hand.sphere_radius
