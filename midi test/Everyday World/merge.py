import pygame.midi
from time import sleep, clock
from mido import MidiFile

mid = MidiFile('Everyday World.mid')
tpb = mid.ticks_per_beat
pygame.midi.init()
player = pygame.midi.Output(0)
player.set_instrument(0)

set_temp=(i for i in mid.tracks[0] if i.type=='set_tempo')
temp=next(set_temp)
t0=clock()
for i in mid.tracks[1]:
        try:
                if i.type=='note_on':
                    player.note_on(i.note, i.velocity)

                elif i.type=='note_off':
                    player.note_off(i.note, i.velocity)
                    #sleep(i.time*0.666666/960.)
                sleep(i.time*temp.tempo*0.000001/float(tpb))
                if clock()-t0 > temp.time*temp.tempo*0.000001/float(tpb):
                    temp=next(set_temp)
                    t0=clock()
                #print 'hi'
        except AttributeError:
                #print 'AttributeError'
                pass
        except:
                pass
                #print 'other'













del player
pygame.midi.quit()
