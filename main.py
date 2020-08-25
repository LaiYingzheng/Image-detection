import cv2 as cv
import numpy as np
import pyautogui
from time import time
from vision import Vision
from hsvfilter import HsvFilter
from windowCapture import WindowsCapture

wincap = WindowsCapture('League of Legends')
vision_friend = Vision('image/FREND.jpg')
vision_friend.init_color_gui()

# HSV filter to needle img
#hsv_filter = HsvFilter(0,0,0,0,0,0,0,0,0,0)
loop_time = time()
while (True):

    screenshot = wincap.get_screenshot()
    # cv.imshow('computer vision', screenshot)

    # pre-process image

    # processed_image = vision_friend.apply_hsv_filter(screenshot,hsv_filter)
    #object detection

    # Processed needle image finding
   # rectangles = vision_friend.find(processed_image, threshhold=0.8)

    rectangles = vision_friend.find(screenshot, threshhold= 0.8)

    # draw detection result on original image
    output_image = vision_friend.draw_rectangles(screenshot, rectangles)

    cv.imshow("matches", output_image)
    print('FPS {}'.format(1/ (time() - loop_time)))
    loop_time = time()
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break


print('Done')

