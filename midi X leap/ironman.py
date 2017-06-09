import Leap

controller=Leap.Controller()

while True:
    frame=controller.frame()
    if len(frame.hands)==2:
        order={}
        for hand in frame.hands:
            pwm = 0 if hand.grab_strength == 1 else Leap.Vector.backward.dot(hand.palm_normal)/Leap.Vector.backward.magnitude_squared

            if hand.is_right:
                order['R'] = pwm
            else:
                order['L'] = pwm
        print order
        #requests order

    else:
        #requests stop
        pass
