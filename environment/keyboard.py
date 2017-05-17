
from visual import *
scene = display(title='keyboard',width=800,height=600,background=(0.5,0.6,0.5))

def octave(L=1., gap=0.05):
    unit=frame()
    H, W= 6.472*L, L/1.618
    h, l, w= H/1.618, L/1.618, W*1.618
    for i in range(7):box(frame=unit, height= H, length=L, width= W, x=i*(L+gap))
    for i in range(2):box(frame=unit, height= h, length=l, width= w, x=i*(L+gap)+L/2, y=(H-h)/2, z=(w-W)/2, color=(0,0,0))
    for i in range(3,6):box(frame=unit, height= h, length=l, width= w, x=i*(L+gap)+L/2, y=(H-h)/2, z=(w-W)/2, color=(0,0,0))
    return unit

if __name__=='__main__':octave()
