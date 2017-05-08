from PIL import Image   #pip install Pillow
from operator import itemgetter
from visual import *
import matplotlib.pyplot as plt

rasengan=Image.open('rasengan.png')
rgb=rasengan.getcolors(maxcolors=65536)#at least equal to len(rgb)
rgb.sort(key=itemgetter(0),reverse=True)







rgb=[i[1][:-1] for i in rgb if i[0]>70] # choose the higher same pixels of colors
'''
print len(rgb)
f=open('rgb data.py','w')
for i in rgb:f.write(str(i)+', ')
f.close()'''



'''
x,colors=zip(*rgb)
colors=list(map(lambda (r,g,b,n):(r/255.0,g/255.0,b/255.0),colors))
plt.pie(x, autopct='%1.1f%%', startangle=90, shadow=True, colors=colors)
plt.axis('equal')
plt.show()

scene = display(title='leap motion',width=800,height=600,background=(0.5,0.6,0.5) ,autoscale = False)
ball=sphere()
while True:
    for (n,(R,G,B,M)) in rgb:
        M=float(M)
        ball.color=(R/M, G/M, B/M)
        print n
        sleep(0.05)
    print 'done'
scene.delete()'''
