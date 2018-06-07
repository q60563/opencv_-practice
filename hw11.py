import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./tmp/hw11/22773484_1561712953889102_988771220_n.png',0)
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()