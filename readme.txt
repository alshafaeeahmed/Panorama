The author's contacts: 
Ahmed Alshafaee , ID: 316474980 .
Wasim Azbarqa , ID:318985512 .

The Subject of the project: Create a panoramic image Using opencv2.

* The program receives two images and stitches them into one panoramic image,
 in the size of the sum of the widths of the images and also and the height of the left image.

Building a panorama image with OpenCV, can be done in only five steps: 
1. Calculation of Keypoints and their descriptors of the images.
2. Calculate distances between each contour in one image and each contour in the other image.
3. Calculation of a homography matrix.
4. Perform transformation using a homography matrix.
5. Sewing the two images into one large panoramic image.

Warning : you may have Warning "Cannot find reference 'imread' in '__init__.py | __init__
   .py'" , its just bug in pycharm , the Program will run normally

What to download directories:

import cv2
import numpy as np
import sys
import os

These libraries should be downloaded for the project running it within PyCharm software,
And then the code will run the output inside the output folder and there will be output images after the correction inside the folder.




