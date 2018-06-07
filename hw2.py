# -*- coding:utf-8 -*- 
import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')

__author__ = 'Microcosm'

import cv2
import numpy as np
import glob

criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001)

objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2) 

obj_points = []    
img_points = []    

img = cv2.imread("./tmp/hw2/22386287_1549611905099207_1607378645_n.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
size = gray.shape[::-1]
ret, corners = cv2.findChessboardCorners(gray, (18,18), None)

if ret:
  obj_points.append(objp)

  corners2 = cv2.cornerSubPix(gray, corners, (5,5), (-1,-1), criteria)  
  if corners2:
    img_points.append(corners2)
  else:
    img_points.append(corners)

  cv2.drawChessboardCorners(img, (18,18), corners, ret) 
  cv2.imshow('img', img)
  cv2.waitKey(50)

print len(img_points)
cv2.destroyAllWindows()

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points,size, None, None)

print "ret:",ret
print "mtx:\n",mtx        
print "dist:\n",dist      
print "rvecs:\n",rvecs    
print "tvecs:\n",tvecs

print("-----------------------------------------------------")
img = cv2.imread(images[12])
h, w = img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))
print newcameramtx
print("------------------使用undistort函数-------------------")
dst = cv2.undistort(img,mtx,dist,None,newcameramtx)
x,y,w,h = roi
dst1 = dst[y:y+h,x:x+w]
cv2.imwrite('calibresult11.jpg', dst1)
print "方法一:dst的大小为:", dst1.shape

print("-------------------使用重映射的方式-----------------------")
mapx,mapy = cv2.initUndistortRectifyMap(mtx,dist,None,newcameramtx,(w,h),5)  # 获取映射方程
dst = cv2.remap(img,mapx,mapy,cv2.INTER_CUBIC)
x,y,w,h = roi
dst2 = dst[y:y+h,x:x+w]
cv2.imwrite('calibresult11_2.jpg', dst2)
print "方法二:dst的大小为:", dst2.shape        # 图像比方法一的小

print("-------------------计算反向投影误差-----------------------")
tot_error = 0
for i in xrange(len(obj_points)):
    img_points2, _ = cv2.projectPoints(obj_points[i],rvecs[i],tvecs[i],mtx,dist)
    error = cv2.norm(img_points[i],img_points2, cv2.NORM_L2)/len(img_points2)
    tot_error += error

mean_error = tot_error/len(obj_points)
print "total error: ", tot_error
print "mean error: ", mean_error