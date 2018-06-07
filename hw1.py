from __future__ import print_function
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
from skimage.filters import threshold_adaptive
from skimage import measure
import numpy as np

import cv2
image = cv2.imread("./tmp/hw1/22385094_1549611858432545_1235538123_n.jpg")
plate = cv2.medianBlur(image, 5)
V = cv2.split(cv2.cvtColor(plate, cv2.COLOR_BGR2HSV))[2]
thresh = threshold_adaptive(V, 31, offset=5).astype("uint8") * 255
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Original", image)
cv2.imshow("License Plate", plate)
cv2.imshow("Thresh", thresh)
labels = measure.label(thresh, neighbors=8, background=0)
mask = np.zeros(thresh.shape, dtype="uint8")
print("[INFO] found {} blobs".format(len(np.unique(labels))))
for (i, label) in enumerate(np.unique(labels)):
  # if label == 0:
  #   print("[INFO] label: 0 (background)")
  # continue
  print("[INFO] label: {} (foreground)".format(i))
  labelMask = np.zeros(thresh.shape, dtype="uint8")
  labelMask[labels == label] = 255
  numPixels = cv2.countNonZero(labelMask)
  if numPixels > 204 and numPixels < 306:
    mask = cv2.add(mask, labelMask)
    cv2.imshow("Label", labelMask)
    # cv2.waitKey(0)
    cv2.imshow("Large Blobs", mask)
    # cv2.waitKey(0)
    k = cv2.waitKey(0)

if k == 27:
  cv2.destroyAllWindows
  
