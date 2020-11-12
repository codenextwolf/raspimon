import sys
sys.path.append("..")

from sense_hat import SenseHat
from raspimon_images import Raspimons
from time import sleep

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
shake_left = [
        b, b, b, b, b, b, b, b,
        w, w, w, w, w, w, b, b,
        w, b, b, b, b, w, w, b,
        w, w, b, w, b, w, b, w,
        w, b, m, b, b, w, b, b,
        w, w, w, w, w, w, b, b,
        b, w, b, b, w, b, b, b,
        b, b, w, b, b, w, b, b
        ]

shake_right = [
        b, b, b, b, b, b, b, b,
        b, b, w, w, w, w, w, w,
        b, w, w, b, b, b, b, w,
        w, b, w, b, w, b, w, w,
        b, b, w, b, b, m, b, w,
        b, b, w, w, w, w, w, w,
        b, b, b, b, w, b, w, b,
        b, b, b, w, b, w, b, b
        ]

sense.set_pixels(rest) #set your own Raspimons here as default rest pose

#define your shake() function here:


    
while True:
        
      
        accel= sense.get_accelerometer_raw()
        print(accel)
        

        



