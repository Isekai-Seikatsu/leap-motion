import pygame.midi
from time import sleep, clock
from mido import MidiFile

mid = MidiFile('Reflection.mid')
pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(0)

set_temp=iter(mid.tracks[1])
temp=next(set_temp)
t0=clock()
for i in mid.tracks[3]:
        if i.type=='note_on':
            player.note_on(i.note, i.velocity)

        elif i.type=='note_off':
            player.note_off(i.note, i.velocity)
            #sleep(i.time*0.666666/960.)
        sleep(i.time*temp.tempo*0.000001/96.)
        if clock()-t0 > temp.time*temp.tempo*0.000001/96.:
            temp=next(set_temp)
            t0=clock()













del player
pygame.midi.quit()
