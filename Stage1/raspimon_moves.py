import sys
sys.path.append("..")

from raspimon_images import Raspimons
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
raspis = Raspimons() #create the instance so we can use the Raspimons as a raspis variable.

closed_mouth = raspis.get_closed_mouth()
open_mouth = raspis.get_open_mouth()
closed_eyes = raspis.get_closed_eyes()

sleep(0.4)
sense.set_pixels(closed_mouth)
sleep(0.3)
sense.set_pixels(open_mouth)
sleep(0.4)
sense.set_pixels(closed_eyes)
sleep(0.3)
sense.set_pixels(open_mouth)
sleep(0.4)
sense.set_pixels(closed_mouth)
sleep(0.3)
sense.set_pixels(closed_eyes)
sleep(0.4)
sense.flip_v()
sleep(0.2)
sense.flip_v()
sleep(0.4)
sense.set_pixels(closed_mouth)
sleep(0.3)
sense.set_pixels(open_mouth)
sleep(0.5)
sense.set_pixels(closed_mouth)
sleep(0.5)
sense.set_pixels(closed_eyes)
sleep(0.5)
sense.set_pixels(open_mouth)
sleep(0.5)
sense.set_pixels(closed_eyes)
sleep(0.5)
sense.set_pixels(closed_mouth)
sleep(0.5)

print('Done')

