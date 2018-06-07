import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./tmp/hw10/DSC_4102.jpg')

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

cv2.imshow("ret",ret)
cv2.imshow("thresh",thresh)

k = cv2.waitKey(0)

if k == 27:
  cv2.destroyAllWindows

