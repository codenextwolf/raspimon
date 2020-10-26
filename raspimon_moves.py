from raspimon_images import Raspimons
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
raspis = Raspimons() #create the instance so we can use the Raspimons as a raspis variable.

sense.set_pixels(raspis.get_open_mouth())
sleep(0.4)
sense.set_pixels(raspis.get_closed_mouth())
sleep(0.3)
sense.set_pixels(raspis.get_open_mouth())
sleep(0.4)
sense.set_pixels(raspis.get_closed_mouth())
sleep(0.3)
sense.set_pixels(raspis.get_open_mouth())
sleep(0.4)
sense.set_pixels(raspis.get_closed_mouth())
sleep(0.3)
sense.set_pixels(raspis.get_open_mouth())
sleep(0.4)
sense.set_pixels(raspis.get_closed_mouth())
sleep(0.3)

 

 

