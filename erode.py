import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2  
import numpy as np   
from matplotlib import pyplot as plt
# img = cv2.imread('./tmp/map.png',cv2.IMREAD_GRAYSCALE)  
img = cv2.imread('./tmp/map.png',0)  
kernel = np.ones((5,5),np.uint8)
dilation = cv2.erode(img,kernel,iterations = 1)
erosion = cv2.erode(img,kernel,iterations = 1) 

dilation_erosion = cv2.erode(dilation,kernel,iterations = 1)      
erosion_dilation = cv2.dilate(erosion,kernel,iterations = 1)      
 
# plt.imshow(img, cmap = 'gray')
# plt.imshow(erosion, cmap = 'gray')
plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.subplot(132),plt.imshow(dilation_erosion, cmap = 'gray')
plt.subplot(133),plt.imshow(erosion_dilation, cmap = 'gray')
plt.show()