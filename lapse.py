import time
import picamera
from datetime import datetime

with picamera.PiCamera() as camera:
    
    camera.resolution = (1920,1080)
    camera.hflip=True
    camera.vflip=True
    camera.iso=100
    try:
        for i in enumerate(camera.capture_continuous('image{counter:02d}.jpg')):
            time.sleep(300)
            if i == 576:
                break
            if  int(datetime.now().strftime("%H"))>=19:
                camera.exposure_mode='night'
            elif int(datetime.now().strftime("%H"))<=7: 
                camera.exposure_mode='night'
            else:
                camera.exposure_mode='auto'
    finally:
        pass
