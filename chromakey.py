import sys
import numpy as np
import cv2

#동영상 불러오기
cap1 = cv2.VideoCapture('1.mp4')
cap2 = cv2.VideoCapture('universe.mp4')


#동영상이 존재하지 않으면 창을 닫음
if not cap1.isOpened():
    sys.exit()

if not cap2.isOpened():
    sys.exit()

cv2.namedWindow('frame', cv2.WINDOW_NORMAL)
cv2.resizeWindow('frame', 854, 480)


chromakey = False

while True:
    ret1, frame1 = cap1.read()

    if not ret1:
        break

    if chromakey:
        ret2, frame2 = cap2.read()

        if not ret2:
            break

        frame1_hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)

        #frame1의 해당 bgr 영역 안에있는 픽셀 값을 추출함 
        mask = cv2.inRange(frame1_hsv, (20, 90, 0), (80, 255, 255))
        #frame1에서 추출한 픽셀들의 bgr에 frame2의 값을 입력 
        cv2.copyTo(frame2, mask, frame1)

    cv2.imshow('frame', frame1)
    key = cv2.waitKey(50)

    #space bar를 누를 때마다 크로마키 온오프
    if key == ord(' '):
        chromakey = not chromakey
    elif key == 27:
        break
