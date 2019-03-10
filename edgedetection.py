# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 20:27:53 2019

@author: Mr.Robot
"""

import cv2
import matplotlib.pyplot as plt


def main():
    
    path = "ringworm1.jpg"
    imgpath =  path
    img = cv2.imread(imgpath, 0)
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    
    L1 = cv2.Canny(img, 30, 300, L2gradient=False)
    
    L2 = cv2.Canny(img, 100, 150, L2gradient=True)

    
    titles = ['Original Image', 'L1 Norm', 'L2 Norm']

    outputs = [img, L1, L2]
    
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(outputs[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    cv2.imwrite("edo.jpg",img)
    cv2.imwrite("ed1.jpg",L1)
    cv2.imwrite("ed2.jpg",L2)
if __name__ == "__main__":
    main()