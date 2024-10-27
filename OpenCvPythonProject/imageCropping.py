import cv2
import os

os.chdir("C:/Users/Raghav/PycharmProjects/OpenCvPythonProject")

img = cv2.imread("Resources/raghav.jpg")
print(img.shape)
cv2.imshow("Image", img)

imgCropped = img[0:500, 120:700]
print(imgCropped.shape)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)