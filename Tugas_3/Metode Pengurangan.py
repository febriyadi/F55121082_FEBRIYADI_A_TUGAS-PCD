import cv2

# load dua buah citra yang akan dikurangi
img1 = cv2.imread('image/pengurangan1.jpg')
img2 = cv2.imread('image/pengurangan.jpg')

# pastikan ukuran kedua citra sama
if img1.shape != img2.shape:
    print('Ukuran kedua citra berbeda')
else:
    # kurangi citra 2 dari citra 1
    result = cv2.subtract(img1, img2)
    # tampilkan citra hasil pengurangan
    cv2.imshow('Result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
