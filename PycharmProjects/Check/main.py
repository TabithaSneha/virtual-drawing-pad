import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

centre = []  #Array for updating coordinates of the centroid
img = np.zeros((480, 640, 3), np.uint8)  #Creating the window of VDP
while (1):
    ret, frame = cap.read()
    frame = cv.flip(frame, 1)  #Capturing each frame

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  #Converting from BGR to HSV

    lower_red = np.array([160, 70, 50])
    upper_red = np.array([180, 255, 255])  #Specifing HSV range for red color

    mask = cv.inRange(hsv, lower_red, upper_red)

    kernel = np.ones((11,11), np.uint8)
    closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernel)
    opening = cv.morphologyEx(closing, cv.MORPH_OPEN, kernel)
    blur = cv.GaussianBlur(opening, (5, 5), 0)  #Reducing noise

    ret1, thresh = cv.threshold(blur, 127,255,0)  #Color Thresholding

    contours, hierarchy = cv.findContours(thresh, 1, 2)  #Finding contours

    if len(contours) > 0:
        cnt = contours[0]
        M = cv.moments(cnt)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])  #Computing coordinates of centroid

        cv.circle(img, (cx, cy), 5, (255, 0, 0), -1) #Drawing a circle

        centre.append((cx, cy))  #Updating centroid coordinates

        for i in range(1, len(centre)):
            if centre[i - 1] is None or centre[i] is None:
                continue

            cv.line(img, centre[i - 1], centre[i], (255, 0, 0), 5)  #Drawing connecting lines between two centroids

    cv.imshow('Camera Frame', frame)
    cv.imshow('VDP Window', img)  #Display

    k = cv.waitKey(20) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
