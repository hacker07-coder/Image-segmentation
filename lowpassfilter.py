# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 13:09:37 2019

@author: Mr.Robot
"""

import cv2
import matplotlib.pyplot as plt


def main():
    
    path = "image.jpg"
    imgpath =  path 
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    
    box = cv2.boxFilter(img, -1, (53, 53))
    
    blur = cv2.blur(img, (13, 13))
    
    gaussian = cv2.GaussianBlur(img, (37, 37), 0)
    
    titles = ['Original Image', 'Box Filter', 
              'Blur', 'Gaussian Blur']

    outputs = [img, box, blur, gaussian]
    
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(outputs[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()