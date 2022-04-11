import cv2
import matplotlib.pyplot as plt
import numpy as np

'''
Dilation,Erosion,Opening,Closing Morphological 

'''

img = cv2.imread("img/CoinNoise.png",0)
thresh,result = cv2.threshold(img,170,255,cv2.THRESH_BINARY_INV)

kernel = np.ones((2,2),np.uint8) #กรองข้อมูล ขนาด 2x2
dilation = cv2.dilate(result,kernel,iterations=5) #การขยายภาพ
erosion = cv2.erode(result,kernel,iterations=7) #การกร่อยภาพ
opening = cv2.morphologyEx(result,cv2.MORPH_OPEN,kernel,iterations=5) #opening
closing = cv2.morphologyEx(result,cv2.MORPH_CLOSE,kernel,iterations=5) #closing

titles = ["Original","THRESH_INV","Dilation","Erosion","Opening","Closing"]
images = [img,result,dilation,erosion,opening,closing]

for i in range(len(images)):
    plt.subplot(2,3,i+1) #subplot(row,collum,i+1)
    plt.imshow(images[i],cmap="gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()