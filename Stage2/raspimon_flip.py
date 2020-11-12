import sys
sys.path.append("..")

from sense_hat import SenseHat
from raspimon_images import Raspimons
from time import sleep

sense = SenseHat()

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
 
sense.set_pixels(rest)



while True:
    orientation = sense.get_orientation()
    sleep(.2)
    #print(orientation)
    
    roll = orientation["roll"]
    #print(str(roll))
    
    if roll >120 and roll < 180:
        print("rolled upside down!" + str(roll))
        sense.flip_v()
        sleep(1)
        
   
   
    
    

        
    

