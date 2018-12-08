"""
Reference:
PiCamera documentation
https://picamera.readthedocs.org/en/release-1.10/recipes2.html

"""

import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray


camera = PiCamera()
camera.resolution = (1280,720)
camera.framerate = 30
rawCapture = PiRGBArray(camera, size=(1280,720))
rawCapture.truncate(0)

for frame1 in camera.capture_continuous(rawCapture,format="bgr",use_video_port=True):
    
    frame = frame1.array
    frame.setflags(write=1)
    
    cv2.imshow('OD', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
    rawCapture.truncate(0)

camera.close()
