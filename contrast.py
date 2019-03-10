import numpy as np
import cv2 
import math
img=cv2.imread('\Users\Mr.Robot\Desktop\skin\image.jpg', cv2.IMREAD_GRAYSCALE)
print (img)
height = img.size
width = img.size

contrast=1.8
for i in np.arange(height):
    for j in np.arange(width):
        a=img.item(i,j)
        b=math.ceil(a*contrast)
        if b>255:
            b=255
        img.itemset((i,j),b)
cv2.imwrite('\Users\Mr.Robot\Desktop\skin\image_1.jpg', img)
cv2.imshow('picture',img)
cv2.waitkey(0)
cv2.destroyAllWindows()
