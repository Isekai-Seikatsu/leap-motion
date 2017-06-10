
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
    j = 0
    unit.sorted_ob = sorted(unit.objects, key = lambda key:key.x)
    for i in unit.sorted_ob:
        i.note = (pitch-3) + 60 + j
        i.backup = (False, i.color)
        #i.play
        j += 1
    return unit

def keyboard(finger_width = 25., pitch_range = (1, 6)):
    keyboard = frame()
    keyboard.keys = []
    for pitch in range(*pitch_range):
        unit = octave(finger_width, pitch)
        unit.frame = keyboard
        keyboard.keys = keyboard.keys + unit.sorted_ob

    keyboard.up = (0, 0, -1)
    return keyboard, (1.0618*finger_width*7, 6.472*finger_width, finger_width)

if __name__=='__main__':
    keyboard()
