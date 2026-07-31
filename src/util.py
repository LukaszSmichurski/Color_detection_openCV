import numpy as np
import cv2 as cv

def get_limits(color):

    c = np.uint8([[color]])
    hsvC = cv.cvtColor(c, cv.COLOR_BGR2HSV)

    hue = hsvC[0][0][0]

    lower_h = max(0, hue - 10) ##zabezpieczenie przed ujemnymi wartościami
    upper_h = min(179, hue + 10)

    lowerLimit = np.array([lower_h, 100, 100], dtype=np.uint8)
    upperLimit = np.array([upper_h, 255, 255], dtype=np.uint8)

    return lowerLimit, upperLimit
