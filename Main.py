
#This is code is not a stable version and is only basic

import cv2
from ColorCvt import convert_

cap = cv2.VideoCapture(0)
Green =  [0, 255, 0]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # coverting every frame to HSV
    Cvrtd_Image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # coverting desired color to HSV and getting the upper and lower limits
    L_limit,H_limit  = convert_(Green)

    #creating single channel binary image
    mask = cv2.inRange(Cvrtd_Image, L_limit, H_limit)

    #Getting endpoints of every green object detected
    contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 5)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) & 0XFF == 113:
        break

cap.release()
cv2.destroyAllWindows()
