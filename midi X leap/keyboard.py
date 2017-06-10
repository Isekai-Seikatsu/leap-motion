
from visual import *
scene = display(title='keyboard',width=800,height=600,background=(0.5,0.6,0.5))

def octave(L=1.,pitch=3):
    gap=L*0.0618
    length=(L+gap)*7
    x0=length*(pitch-3)
    unit=frame()
    H, W= 6.472*L, L/1.618
    h, l, w= H/1.618, L/1.618, W*1.618
    for i in range(7):box(frame=unit, height= H, length=L, width= W, x=i*(L+gap)+x0)
    for i in 0,1,3,4,5:box(frame=unit, height= h, length=l, width= w, x=i*(L+gap)+x0+L/2, y=(H-h)/2, z=(w-W)/2, color=(0,0,0))
    return unit

def keyboard():
    keyboard = frame()
    for pitch in range(1,6):
        for i in octave(25, pitch).objects:
            i.frame = keyboard
    keyboard.up = (0, 0, -1)
    keyboard.notes = sorted(keyboard.objects, key = lambda ob:ob.x)

    for i in range(len(keyboard.objects)):
        keyboard.objects[i].note = i+36
    return keyboard

if __name__=='__main__':
    keyboard=keyboard()

    import pygame.midi
    pygame.midi.init()
    player = pygame.midi.Output(0)
    for k in range(128):
        player.set_instrument(k)

        for i in keyboard.notes:
            rate(100)
            backup = i.color
            i.color = (0.8, 0.988, 0.992)
            player.note_on(i.note, 127)
            sleep(0.05)
            player.note_off(i.note, 127)
            i.color = backup
    del player
    pygame.midi.quit()
