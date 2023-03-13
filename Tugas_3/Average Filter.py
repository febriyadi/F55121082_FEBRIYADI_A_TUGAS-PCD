import cv2
import numpy as np


img = cv2.imread('image/Average_Filter.jpg')

#definisikan kernel size untuk filter
kernel_size= (5, 5)

kernel = np.ones(kernel_size, np.float32) / (kernel_size[0]*kernel_size[1])

filtered_img= cv2.filter2D(img, -1, kernel)
cv2.imshow('Original car', img)
cv2.imshow('Filtered car', filtered_img)

cv2.waitKey(0)
cv2.destroyAllWindows()