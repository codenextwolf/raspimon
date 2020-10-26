#Raspimon Academy Lab 3
from pathlib import Path
import sys
p = Path().absolute() #get path to parent dir
sys.path.append(str(p.parent)) #append to module path
print(sys.path)
from sense_hat import SenseHat
from time import sleep
from raspimon_images import Raspimons

sense = SenseHat()

#makeover time! Here is a Python list. It holds  collection of string values.

names = ["Codey" , "Galbert" , "Freedy", "Voltria" , "Kat-Kat"]

names.append("Lizardia")

sense.show_message(names[1])

#Colors:

r = (255, 0, 0 ) # RED color, stored in an another data structure called a tuple.
b = (0, 0, 0) # black means zero amounts of red, green and blue

#define another color. Use one letter variable names to make it easy later

raspimon = [
b, b, b, b, b, b, b, b,
b, r, r, r, r, r, r, b,
b, r, b, b, b, b, r, b,
b, r, r, b, r, b, r, b,
b, r, b, b, b, b, r, b,
b, r, r, r, r, r, r, b,
b, b, r, b, r, b, b, b,
b, b, r, b, r, b, b, b
]
 
sense.set_pixels(raspimon)

sense.set_pixel(3,4, [255,0,0])

 


