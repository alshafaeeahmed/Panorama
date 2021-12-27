import sys
import cv2
import numpy as np

from google.colab.patches import cv2_imshow

# Load our images
img1 = cv2.imread("first.jpg")
img2 = cv2.imread("second.jpg")

img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2_imshow(img1_gray)
cv2_imshow(img2_gray)