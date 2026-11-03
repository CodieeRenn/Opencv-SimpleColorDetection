
import numpy as np
import cv2


def convert_(Green):
    color =  np.uint8([[Green]])
    cnvrt_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)

    L_limit = cnvrt_color[0][0][0] - 10, 100, 100
    H_limit = cnvrt_color[0][0][0] + 10, 255, 255

    L_limit = np.array(L_limit, dtype = np.uint8)
    H_limit = np.array(H_limit, dtype = np.uint8)



    return L_limit,H_limit











