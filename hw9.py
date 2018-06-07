import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('./tmp/hw9/22811332_1561712930555771_1470497248_n.jpg')
img2 = cv2.imread('./tmp/hw9/22782082_1561712937222437_949835528_n.png')

hsv1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

size =  np.shape(img1)

for i in range(0,size[0]):
  for j in range(0,size[1]):
    hsv2[i][j][2]=hsv1[i][j][2]

res = cv2.cvtColor(hsv2, cv2.COLOR_HSV2BGR)

cv2.imshow("hsv1",hsv1)
cv2.imshow("hsv2",hsv2)
cv2.imshow("res",res)

k = cv2.waitKey(0)

if k == 27:
  cv2.destroyAllWindows

