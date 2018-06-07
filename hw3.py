import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./tmp/hw3/22449107_1549613061765758_1319171719_o.jpg',0)
    
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) 
cv2.imwrite('res.png',res)
cv2.imshow('res.png',res)
k = cv2.waitKey(0)

if k == 27:
  cv2.destroyAllWindows