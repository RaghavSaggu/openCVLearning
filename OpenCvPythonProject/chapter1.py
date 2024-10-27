import cv2
import os

os.chdir("C:/Users/Raghav/PycharmProjects/OpenCvPythonProject")

img = cv2.imread("Resources/raghav.jpg")
print(img.shape)
# cv2.imshow("Image", img)

imgResize = cv2.resize(img,(300,300))
print(imgResize.shape)
cv2.imshow("Resized Image", imgResize)

imgCropped = imgResize[0:200, 60:250]
print(imgCropped.shape)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)