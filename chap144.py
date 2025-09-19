import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('opencv_logo.png')
k=9
blur = cv2.GaussianBlur(img,(k,k),0)
kernel = np.ones((k,k),np.float32)/(k*k)
dst2 = cv2.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(dst2),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('GaussianBlur')
plt.xticks([]), plt.yticks([])
plt.show()