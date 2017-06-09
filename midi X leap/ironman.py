import Leap

controller=Leap.Controller()

while True:
    frame=controller.frame()
    if len(frame.hands)==1:
        #order=[]
        for hand in frame.hands:
            #print hand.confidence
            pwm = Leap.Vector.forward.dot(hand.palm_normal)/Leap.Vector.forward.magnitude_squared
            if pwm > 0:
                print 'forward'
            else:
                print 'backward'

    else:
        #stop
        pass
