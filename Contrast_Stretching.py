import cv2 
import numpy as np

path = 'trk.jpg'
alpha = 5.2
beta = 50

image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

min_val = np.min(image)
max_val = np.max(image)

height, width = image.shape

stretched_image = np.zeros_like(image, dtype=np.uint8)

for i in range(height):
    for j in range(width):
        stretched_image[i, j] = np.clip(alpha * image[i, j] + beta, 0, 255)

cv2.imshow('Original Image', image)
cv2.imshow('Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
