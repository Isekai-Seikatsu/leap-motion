import Leap
from visual import *
from visual.graph import *
'''
controller=Leap.Controller()
controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)



while True:
            frame=controller.frame()
            interaction_box = frame.interaction_box
            for ges in frame.gestures():
                print ges.id,
                circle = Leap.CircleGesture(ges)
                
                print circle.radius,circle.progress, "clockwise" if (circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2) else "counterclockwise"
'''

controller=Leap.Controller()
controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)

graph = gdots()

while True:
            rate(1000)
            frame=controller.frame()
            interaction_box = frame.interaction_box
            '''
            for hand in frame.hands:
                pos=interaction_box.normalize_point(hand.palm_position)
                graph.plot(pos=(pos.x,pos.y))
            '''
            for ges in frame.gestures():
                #print ges.id,
                #tap = Leap.KeyTapGesture(ges)
                tap=Leap.ScreenTapGesture(ges)
                pos=tap.position
                graph.plot(pos=(pos.x,pos.y))
                #finger=Leap.Finger(tap.pointable)
                #print finger.type
                
