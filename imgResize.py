import cv2
import imutils
img = cv2.imread("bellicon.jpeg")
resizeImg = imutils.resize(img, width = 20)
cv2.imwrite("resizedImg.jpeg", resizeImg)
