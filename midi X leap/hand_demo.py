from visual import *

class hand_demo():
    def __init__(self):
        self.objects=[cylinder(color=(0.5,0.4,0.5)) for _ in range(20)]
    def update(self, hand):
        j=0
        for finger in hand.fingers:
            for i in range(4):
                bone=finger.bone(i)
                cy=self.objects[j]
                cy.pos =bone.prev_joint.to_tuple()
                cy.axis=(bone.next_joint-bone.prev_joint).to_tuple()
                cy.radius=bone.width/2
                j+=1

if __name__=='__main__':
    import Leap
    controller=Leap.Controller()

    scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)

    scene.center.y+=100
    hands=[hand_demo(), hand_demo()]
    while True:
                rate(100)
                frame=controller.frame()
                i=0
                for hand in frame.hands:
                    print i
                    hands[i].update(hand)
                    i+=1
