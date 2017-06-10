import Leap
from keyboard_EMT import *
from hand_demo import *
controller = Leap.Controller()

scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)

hands = [hand_demo(), hand_demo()]

keyboard, octave_length = keyboard()
keyboard.y += 100
scene.center.y += 100
while True:
            rate(100)
            frame = controller.frame()
            i=0
            for hand in frame.hands:

                for key in keyboard.objects[int((hand.palm_position.x+octave_length*2)/octave_length)]:
                    print type(key.pos)







                hands[i].update(hand)
                i+=1
