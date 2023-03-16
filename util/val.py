import numpy as np
import cv2
support_image_path ='F:/BAM-main/2008_006912.png'
support_image = cv2.imread(support_image_path)
info = support_image.shape
height = info[0]
width = info[1]
dst = np.zeros((height, width, 3), np.uint8)
for h in range(0, height):
    for j in range(0, width):
        (b, g, r) = support_image[h, j]
        if (b,g,r)==(8,8,8):
            support_image[h, j] = (255,255,255)
        if (b,g,r)==(10,10,10):
            support_image[h, j] = (0,0,0)
        dst[h, j] = support_image[h, j]
        # print(dst[h,j])

    cv2.imwrite('img_gray.jpg', dst)