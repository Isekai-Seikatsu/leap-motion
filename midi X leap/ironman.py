import Leap

controller=Leap.Controller()

while True:
    frame=controller.frame()
    if len(frame.hands)==2:
        order={}
        for hand in frame.hands:
            #print hand.confidenc
            pwm = Leap.Vector.forward.dot(hand.palm_normal)/Leap.Vector.forward.magnitude_squared
            if hand.is_right:   order['R'] = pwm
            else:   order['L'] = pwm

    else:
        #stop
        pass
