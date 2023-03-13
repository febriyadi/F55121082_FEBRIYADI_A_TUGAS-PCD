import cv2
import numpy as np

# Load the images to be averaged
img1 = cv2.imread('image/img1.jpg')
img2 = cv2.imread('image/img2.jpg')
img3 = cv2.imread('image/img3.jpg')

# Resize the images to have the same dimensions
img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))
img3 = cv2.resize(img3, (640, 480))

# Convert the images to floating point
img1 = np.float32(img1)
img2 = np.float32(img2)
img3 = np.float32(img3)

# Add the images together
sum_img = cv2.add(img1, img2)
sum_img = cv2.add(sum_img, img3)

# Divide the sum by the number of images to get the average
avg_img = np.uint8(sum_img / 3)

# Display the resulting image
cv2.imshow('Average Image', avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
