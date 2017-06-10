import Leap
from keyboard import *
controller=Leap.Controller()

import pygame.midi
pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(0)

keyboard = keyboard()
while True:
    rate(100)
    frame=controller.frame()
    for hand in frame.hands:
        pos=hand.palm_position.to_tuple()
        note=int((pos[0]+500)/(1000./36))+48
        #note=int((pos[1]-50)/(650./12))+60
        key = keyboard.notes[note-36]
        backup = key.color
        key.color = (0.8, 0.988, 0.992)
        player.note_on(note, 127)
        sleep(0.05)
        player.note_off(note, 127)
        key.color = backup
        print note
