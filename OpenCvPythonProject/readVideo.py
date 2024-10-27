import cv2
import os

print("package imported")
os.chdir("C:/Users/Raghav/")

cap  = cv2.VideoCapture("Videos/Clips/jubanKesari.mp4")
while True:
    success, img = cap.read()
    cv2.imshow('Video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break