import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

import cv2
import numpy as np

img = cv2.imread('./tmp/hw7/22809614_1561712947222436_385395702_n.jpg') 

cv2.imshow("img", img)
print img[0][0][0]
print img[0][0][1]
print img[0][0][2]
size =  np.shape(img)
change = np.zeros((size),np.uint8)
print size[0]
#bgr
blue = [180,35,50]
yellow = [65,253,245]
print blue
print yellow
print img[101][201]
colorRange=0.3
for i in range(0,size[0]):
    for j in range(0,size[1]):
        #if int(img[i][j][1])+int(img[i][j][2]) < 100 and int(img[i][j][0]) > 100:
        if (int(img[i][j][1])+int(img[i][j][2])) < int(img[i][j][0]) and int(img[i][j][0]> 100):
            change[i][j] = yellow
        elif img[i][j][0] < 150 and int(img[i][j][1]) > 200: 
        #elif int(img[i][j][1]) > 200: 
            if int(img[i][j][1]) - int(img[i][j][2]) < 35:
                change[i][j]= blue
        else:
            change[i][j]=img[i][j]
cv2.imshow("change", change)
cv2.waitKey(0)
cv2.destroyWindow()

