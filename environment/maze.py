from random import randrange,shuffle
from visual import *
#import gc
#from time import clock

length,height,width=5,5,8.09 # (1+5**0.5)/2 ~~1.618

#scene = display(title='maze',width=800,height=600,background=(0.5,0.6,0.5))

def make_maze(w=5, h=5):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [['1000'] * w + ['1'] for _ in range(h)] + [[]]
    hor = [['1111'] * w + ['1'] for _ in range(h+1)]
    def walk(x, y):
        vis[y][x] = 1
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x: hor[max(y, yy)][x] = '1000'
            if yy == y: ver[y][max(x, xx)] = '0000'
            walk(xx, yy)
    walk(randrange(w), randrange(h))
    result=[]
    for (a, b) in zip(hor, ver):
        result.append(''.join(a))
        for _ in range(3): # 3 is the width at ver
            result.append(''.join(b))

    for i in range(3): # dig the start and goal
        result[i+1]='0'+result[i+1][1:]
        result[-(i+5)]=result[-(i+5)][:-1]+'0'
    return result

def create(graph,X=0,Y=0,Z=0):
    maze, X0=frame(), X
    for line in graph:
        for i in line:
            if i=='1' : box(frame=maze,pos=(X,Y,Z),length=length,height=height,width=width,material=materials.wood)
            X+=length
        X=X0
        Y-=height
    return maze

def delete(frame):
    for i in frame.objects:
        i.visible=False
        del i
'''
while __name__=='__main__':
    rate(100)

    maze=create(make_maze())
    for i in maze.objects:
           i.visible=False
           del i
    print'Done'
        #t=clock()
        #gc.collect()
        #print clock()-t'''
