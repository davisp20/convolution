
"""
Created on Mon Mar  9 11:37:06 2020

@author: Phil Davis
"""

import matplotlib.image as img
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

sharpen = np.asarray([[0,-1,0],[-1,5,-1],[0,-1,0]])
boxblur = (1/9)*np.asarray([[1,1,1],[1,1,1],[1,1,1]])
edge = np.asarray([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

def showconvo(image, convKern, title1):
    image = image.copy()
    dst = cv.filter2D(image, -1, convKern)
    fig , axs = plt.subplots(nrows =2 )
    axs[0].imshow(image)
    axs[0].set_title('Original')
    axs[1].imshow(dst)
    axs[1].set_title(title1)
    fig.tight_layout()
    plt.show()
    

image = img.imread('babyyoda1.jpg')

print(image.shape)

showconvo(image, sharpen, 'Sharpen' )
#showconvo(image, boxblur, 'Blur')
#showconvo(image, edge, 'Edge Dection')