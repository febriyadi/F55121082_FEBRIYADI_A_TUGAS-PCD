import cv2
import numpy as np
import matplotlib.pyplot as plt

# Memuat gambar
img = cv2.imread('image/Hestogram.jpg', 0)

# Samakan histogramnya
equalized_img = cv2.equalizeHist(img)

# Tampilkan hasilnya
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(10,5))
ax1.imshow(img, cmap='gray')
ax1.set_title('Original Image')
ax2.imshow(equalized_img, cmap='gray')
ax2.set_title('Equalized Image')
plt.show()
