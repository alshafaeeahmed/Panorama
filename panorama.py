import cv2
import numpy as np
import sys
from reportlab import xrange

left_image = cv2.imread(sys.argv[1])
left_image_gray = cv2.cvtColor(left_image, cv2.COLOR_BGR2GRAY)
right_image = cv2.imread(sys.argv[2])
img2_gray = cv2.cvtColor(right_image, cv2.COLOR_BGR2GRAY)

# Step number 1
# Calculation of Keypoints and their descriptors of the images.
# Create our ORB detector and detect keypoints and descriptors
orb = cv2.ORB_create(nfeatures=500)
# Find the key points and descriptors with ORB
left_keypoints, left_descriptors = orb.detectAndCompute(left_image_gray, None)
right_keypoints, right_descriptors = orb.detectAndCompute(img2_gray, None)

# Step number 2
# Calculate distances between each contour in one image and each contour in the other image.
matcher = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = matcher.match(left_descriptors, right_descriptors)
matches = sorted(matches, key=lambda x: x.distance)
matches = matches[:int(len(matches) * 0.2)]

matches = [left_match for left_match, right_math in
           cv2.BFMatcher(cv2.NORM_HAMMING).knnMatch(right_descriptors, left_descriptors, k=2) if
           left_match.distance < right_math.distance]

#  Step number 3
# Calculation of a homography matrix.
right_image_kp = np.float32([right_keypoints[m.queryIdx].pt for m in matches])
left_image_kp = np.float32([left_keypoints[m.trainIdx].pt for m in matches])
# Establish a homography
H, status = cv2.findHomography(right_image_kp, left_image_kp, cv2.RANSAC)

height_left_image = right_image.shape[0]
width_left_image = left_image.shape[1]
width_right_image = right_image.shape[1]
height_panorama = height_left_image
width_panorama = width_left_image + width_right_image
# Step number  4
# Perform transformation using a homography matrix.
# Sewing the two images into one large panoramic image.
panorama2 = cv2.warpPerspective(right_image, H, (width_panorama, height_panorama))
panorama2[0:left_image.shape[0], 0:left_image.shape[1]] = left_image

# Delete black frame
h, w, d = panorama2.shape
# left limit
for i in range(w):
    if np.sum(panorama2[:, i, :]) > 0:
        break
# right limit
for j in xrange(w - 1, 0, -1):
    if np.sum(panorama2[:, j, :]) > 0:
        break

cropped = panorama2[:, i:j + 1, :].copy()
output = cv2.imwrite(sys.argv[3], cropped)
output = 'output.jpg'
