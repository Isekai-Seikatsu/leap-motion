import Leap
from keyboard_EMT import *
from hand_demo import *
controller = Leap.Controller()

scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)

hands = [hand_demo(), hand_demo()]

keyboard, octave_LHW = keyboard()
sthop = 100#set the height of piano
keyboard.y += sthop
scene.center.y += sthop

import pygame.midi
pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(0)

while True:
            rate(100)
            frame = controller.frame()
            i=0
            keys_is_pressed = [False] * 60
            for hand in frame.hands:
                for finger in hand.pointables:
                    if  all([ 1  if l < p < u else 0 for l, p, u in zip((-2*octave_LHW[0], -octave_LHW[2]*0.927+sthop, -octave_LHW[1]/2.), finger.tip_position, (3*octave_LHW[0], octave_LHW[2]*0.691+sthop, octave_LHW[1]/2.))]):
                        x = finger.tip_position.x#hand.palm_position.x
                        _, key = min(((abs(key.pos.x - x), key) for key in keyboard.objects[int((x+octave_LHW[0]*2)/octave_LHW[0])].objects))
                        keys_is_pressed[key.note-36] = True


                hands[i].update(hand)
                i+=1

            #print sum(keys_is_pressed)

            for k in range(60):
                keyboard.keys[k].color = (0.8, 0.988, 0.992) if keys_is_pressed[k] else keyboard.keys[k].backup[1]
                if keyboard.keys[k].backup[0] == True and keys_is_pressed[k] == False:
                    player.note_off(keyboard.keys[k].note, 127)#
                    keyboard.keys[k].backup[0] == False
                elif  keyboard.keys[k].backup[0] == False and keys_is_pressed[k] == True:
                    player.note_on(keyboard.keys[k].note, 127)#
                    keyboard.keys[k].backup[0] == True
