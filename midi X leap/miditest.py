import Leap
controller=Leap.Controller()

import pygame.midi
pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(0)

while True:
    frame=controller.frame()
    for hand in frame.hands:
        pos=hand.palm_position.to_tuple()
        note=int((pos[0]+500)/(1000./36))+48
        #note=int((pos[1]-50)/(650./12))+60
        player.note_on(note, 127)
        print note
