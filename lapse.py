import time
import picamera
from datetime import datetime

with picamera.PiCamera() as camera:
    
    camera.resolution = (1920,1080)
    camera.hflip=True
    camera.vflip=True
    
    for i in range(3):
        time.sleep(1)
        if  int(datetime.now().strftime("%H"))>=19 or int(datetime.now().strftime("%H"))<=7:
            camera.exposure_mode='night'
            camera.exposure_compensation=25
            camera.iso=200
            camera.capture('image%02d.jpg' % i)
        else:
            camera.capture('image%02d.jpg' % i)
