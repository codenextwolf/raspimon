from sense_hat import SenseHat
from time import sleep
import os, io
from google.cloud import vision
import cv2

#initialize SenseHat instance and clear the LED matrix
sense = SenseHat()
sense.clear()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'your_file_here.json' #replace your_file_here with your Google cloud project credential JSON file name (follow setup)
client = vision.ImageAnnotatorClient()


def detect_object(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.label_detection(image=image) #full response from Google cloud vision
    label_annotations = response.label_annotations #array of objects labeled
    print(label_annotations[0])
    description = label_annotations[0].description #get description of one object
    return description

#Raspimon RGB colors
r = [139, 0, 0]
mon_w = [255, 255, 255]
mon_y = [250, 214, 29]
mon_oj = [225, 151, 32]
mon_br = [129, 30, 9]
mon_r = [246, 45, 20]
mon_b = [0, 0, 0]
mon_p = [255,105,180]
sky_b = [135,206,235]
grass_g = [0,154,23]

#Raspimon Idle
pimon_idle = [
    sky_b, mon_b, mon_b, sky_b, sky_b, sky_b, sky_b, mon_b,
    sky_b, sky_b, mon_y, mon_oj, sky_b, sky_b, sky_b, mon_oj,
    sky_b, sky_b, sky_b, mon_y, mon_y, mon_y, mon_y, mon_oj,
    mon_oj, mon_oj, sky_b, mon_y, mon_b, mon_y, mon_y, mon_b,
    mon_oj, mon_oj, sky_b, mon_r, mon_y, mon_y, mon_y, mon_oj,
    sky_b, mon_br, sky_b, mon_y, mon_oj, mon_oj, mon_oj, sky_b,
    grass_g, mon_br, mon_y, mon_oj, mon_y, mon_oj, mon_y, grass_g,
    grass_g, grass_g, mon_y, mon_oj, mon_br, mon_br, mon_oj, grass_g
]

sense.set_pixels(pimon_idle) #show raspimon
sleep(3)
sense.show_message('Grab an object', text_colour=mon_y, scroll_speed=0.05)
sleep(1)

#5 sec countdown 
sense.show_letter('5', text_colour=[255, 0, 0])
sleep(1)
sense.show_letter('4', text_colour=[255, 0, 0])
sleep(1)
sense.show_letter('3', text_colour=[255, 0, 0])
sleep(1)
sense.show_letter('2', text_colour=[255, 0, 0])
sleep(1)
sense.show_letter('1', text_colour=[255, 0, 0])
sleep(1)
sense.clear()


sense.set_pixels(pimon_idle)
#capture video
cap = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    file = 'obj.png'
    cv2.imwrite(file,frame)
    
    # Display the resulting frame
    cv2.imshow('frame',frame) #show camera output
    key = cv2.waitKey(0) #press 0 to move through frames
    if key == ord('y'): #press y to detect object in current frame
        obj = detect_object(file)
        sense.show_message('This is a...', text_colour=mon_y, scroll_speed=0.05)
        sense.show_message(obj, text_colour=mon_r, scroll_speed=0.1)
        sleep(1)
        sense.set_pixels(pimon_idle)
    elif key == ord('q'): #press q to quit
        break
cap.release()
cv2.destroyAllWindows()
sense.clear()