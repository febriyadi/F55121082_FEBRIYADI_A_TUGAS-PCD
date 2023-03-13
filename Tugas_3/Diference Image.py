from skimage.metrics import structural_similarity
import cv2
import numpy as np

#Memuat gambar
before = cv2.imread('image/leftImage.jpg')
after = cv2.imread('image/rightImage.jpg')

# Konversi gambar ke skala abu-abu
before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

# Hitung SSIM antara dua gambar
(score, diff) = structural_similarity(before_gray, after_gray, full=True)
print("Image Similarity: {:.4f}%".format(score * 100))

# Gambar diff berisi perbedaan gambar sebenarnya antara kedua gambar
# dan direpresentasikan sebagai tipe data floating point dalam rentang [0,1]
# jadi kita harus mengonversi array menjadi 8-bit unsigned integer dalam range
# [0,255] sebelum kita dapat menggunakannya dengan OpenCV
diff = (diff * 255).astype("uint8")
diff_box = cv2.merge([diff, diff, diff])

# Batasi perbedaan gambar, diikuti dengan menemukan kontur
# dapatkan wilayah dari dua gambar masukan yang berbeda
thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

mask = np.zeros(before.shape, dtype='uint8')
filled_after = after.copy()

for c in contours:
    area = cv2.contourArea(c)
    if area > 40:
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(before, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.rectangle(after, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.rectangle(diff_box, (x, y), (x + w, y + h), (36,255,12), 2)
        cv2.drawContours(mask, [c], 0, (255,255,255), -1)
        cv2.drawContours(filled_after, [c], 0, (0,255,0), -1)

cv2.imshow('before', before)
cv2.imshow('after', after)
cv2.imshow('diff', diff)
cv2.imshow('diff_box', diff_box)
cv2.imshow('mask', mask)
cv2.imshow('filled after', filled_after)
cv2.waitKey()