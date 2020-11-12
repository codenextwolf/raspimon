import sys
sys.path.append("..")
from sense_hat import SenseHat
from time import sleep
from raspimon_images import Raspimons

sense = SenseHat()

#replace with your own colors and Raspimons
w = (255,255,255)
m = (128,0,128)
b = (0, 0, 0)


rest = [
        b, b, b, b, b, b, b, b,
        b, w, w, w, w, w, w, b,
        b, w, b, b, b, b, w, b,
        b, w, w, b, w, b, w, b,
        b, w, b, w, b, b, w, b,
        b, w, w, w, w, w, w, b,
        b, b, w, b, w, b, b, b,
        b, b, w, b, w, b, b, b
        ]
tapped = [
        b, b, b, b, b, b, b, b,
        b, m, m, m, m, m, m, b,
        b, m, b, b, b, b, m, b,
        b, m, m, b, m, b, m, b,
        b, m, b, m, b, b, m, b,
        b, m, m, m, m, m, m, b,
        b, b, m, b, m, b, b, b,
        b, b, m, b, m, b, b, b
        ]

sense.set_pixels(rest) #set your own Raspimons here as default rest pose

while True:
        
        sense.set_pixels(rest)
        
        accel= sense.get_accelerometer_raw()
        print(accel)
        


        

 