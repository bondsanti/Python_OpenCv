import cv2
import matplotlib.pyplot as plt
import numpy as np


'''
ตรวจจับขอบภาพ (Edge Detection)
'''
'''
ตรวจจับขอบภาพด้วย Sobel Method
'''

# img = cv2.imread("img/currency.jpg",0)
# sovbelx = cv2.Sobel(img,-1,1,0) #หาขอบแนวนอน
# sovbely = cv2.Sobel(img,-1,0,1) #หาขอบแนวตั้ง
# sovbelxy = cv2.bitwise_or(sovbelx,sovbely)

# images = [img,sovbelx,sovbely,sovbelxy]
# titles = ["original","sovbelx","sovbely","sovbelxy"]

# cv2.imshow("output",img)
# cv2.imshow("sovbelx",sovbelx)
# cv2.imshow("sovbely",sovbely)
# cv2.imshow("sovbelxy",sovbelxy)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# for i in range(len(images)):
#     plt.subplot(2,2,i+1) #subplot(row,collum,i+1)
#     plt.imshow(images[i],cmap="gray")
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
# plt.show()

'''
 ตรวจจับขอบภาพด้วย Laplacian Method
'''
# img = cv2.imread("img/currency.jpg",0)

# lap = cv2.Laplacian(img,-1)

# cv2.imshow("output",img)
# cv2.imshow("laplacian",lap)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


'''
ตรวจจับขอบภาพด้วย Canny Method
'''
img = cv2.imread("img/currency.jpg",0)

canny = cv2.Canny(img,50,100)

cv2.imshow("output",img)
cv2.imshow("canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()