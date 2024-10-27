import cv2
import os

print("package imported")
os.chdir("C:/Users/Raghav/PycharmProjects/OpenCvPythonProject")

img = cv2.imread("Resources/raghav.jpg")
cv2.imshow("Output", img)
cv2.waitKey(0)