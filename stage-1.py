from sense_hat import SenseHat
from time import sleep

#initialize SenseHat instance
sense = SenseHat()

#google colors
g_blue = [66,133,244]
g_red = [219,68,55]
g_ylw = [244,160,0]
g_green = [15,157,88]

sense.clear() #clear LED matrix

#Show letters to spell Google
sense.show_letter('G', text_colour=g_blue)
sleep(0.8) #pause for 0.8 seconds
sense.show_letter('O', text_colour=g_red)
sleep(0.8)
sense.show_letter('O', text_colour=g_ylw)
sleep(0.8)
sense.show_letter('G', text_colour=g_blue)
sleep(0.8)
sense.show_letter('L', text_colour=g_green)
sleep(0.8)
sense.show_letter('E', text_colour=g_red)
sleep(0.8)

#Scroll "Code Next" and "Raspimon"
sense.show_message('Code Next', text_colour=g_blue, scroll_speed=0.04)
sense.show_message('Raspimon', text_colour=g_red, scroll_speed=0.08)


#Raspimon RGB colors
r = [238,21,21]
w = [255, 255, 255]
mon_y = [250, 214, 29]
mon_oj = [225, 151, 32]
mon_br = [129, 30, 9]
mon_r = [246, 45, 20]
mon_b = [0, 0, 0]
sky_b = [135,206,235]
grass_g = [0,154,23]

#Raspimon Idle (facing right an left)
pimon_i_r = [
    sky_b, mon_b, mon_b, sky_b, sky_b, sky_b, sky_b, mon_b,
    sky_b, sky_b, mon_y, mon_oj, sky_b, sky_b, sky_b, mon_oj,
    sky_b, sky_b, sky_b, mon_y, mon_y, mon_y, mon_y, mon_oj,
    mon_oj, mon_oj, sky_b, mon_y, mon_b, mon_y, mon_y, mon_b,
    mon_oj, mon_oj, sky_b, mon_r, mon_y, mon_y, mon_y, mon_oj,
    sky_b, mon_br, sky_b, mon_y, mon_oj, mon_oj, mon_oj, sky_b,
    grass_g, mon_br, mon_y, mon_oj, mon_y, mon_oj, mon_y, grass_g,
    grass_g, grass_g, mon_y, mon_oj, mon_br, mon_br, mon_oj, grass_g
]

pimon_i_l = [
    mon_b, sky_b, sky_b, sky_b, sky_b, mon_b, mon_b, sky_b,
    mon_oj, sky_b, sky_b, sky_b, mon_oj, mon_y, sky_b, sky_b,
    mon_oj, mon_y, mon_y, mon_y, mon_y, sky_b, sky_b, sky_b,
    mon_b, mon_y, mon_y, mon_b, mon_y, sky_b, mon_oj, mon_oj,
    mon_oj, mon_y, mon_y, mon_y, mon_r, sky_b, mon_oj, mon_oj,
    sky_b, mon_oj, mon_oj, mon_oj, mon_y, sky_b, mon_br, sky_b,
    grass_g, mon_y, mon_oj, mon_y, mon_oj, mon_y, mon_br, grass_g,
    grass_g, mon_oj, mon_br, mon_br, mon_oj, mon_y, grass_g, grass_g
]


sense.clear(r) #flash color on entire LED matrix
sleep(0.5)
sense.clear(w)
sleep(0.5)
sense.set_pixels(pimon_i_r) #show monster image (facing right)
sleep(2)
sense.show_message("Hi I'm PiMon", text_colour=mon_y)

#animation loop
while True:
    sense.set_pixels(pimon_i_r)
    sleep(5)
    sense.show_message("grrr", text_colour=mon_y)
    sense.set_pixels(pimon_i_l) #change to face left image to animate
    sleep(5)
    sense.set_pixels(pimon_i_r)
    sleep(3)
    sense.set_pixels(pimon_i_l)
    sleep(3)