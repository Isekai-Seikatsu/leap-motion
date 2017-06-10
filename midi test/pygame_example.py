import pygame.midi
import time

pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(0)
for i in 60,62,64,65,67,69,71:
    player.note_on(i, 127)
    time.sleep(1)
    player.note_off(i, 127)
del player
pygame.midi.quit()
