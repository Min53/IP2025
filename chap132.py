import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,255,0]

img1 = cv2.imread('opencv_logo.png')

replicate = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()

''' 
img1 = cv2.imread('opencv_logo.jpg')
img2 = cv2.imread('Cartoony-Day-Sky-01.png')
dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.namedWindow('image')
cv2.createTrackbar('weight','image',0,100,nothing)
while(1):
    w=cv2.getTrackbarPos('weight','image')/100
    print(w)
    dst = cv2.addWeighted(img1,w,img2,1,-w,0)
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k== ord('m'):
        mode=not mode
    elif k==27:
        break
cv2.destroyAllWindows()
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''