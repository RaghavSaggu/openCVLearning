import cv2
import os

os.chdir("C:/Users/Raghav/PycharmProjects/OpenCvPythonProject")

img = cv2.imread("Resources/raghav.jpg")
print(img.shape)
imgResize = cv2.resize(img,(300,300))
print(imgResize.shape)
imgGray = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
print(imgGray.shape)

# cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Gray Image", imgGray)
cv2.waitKey(0)