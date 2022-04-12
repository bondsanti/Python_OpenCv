import cv2
import numpy as np
import matplotlib.pyplot as plt

'''
Convolution *ลบ Noise
'''

# img = cv2.imread("img/noise.png")
# # kernel = np.ones((3,3),np.float32)/9

# convo1 = cv2.filter2D(img,-1,np.ones((3,3),np.float32)/9)
# convo2 = cv2.filter2D(img,-1,np.ones((3,3),np.float32)/25)


# titles=["Original","Convolution 3x3","Convolution 5x5"]
# images=[img,convo1,convo2]

# for i in range(len(images)):
#     plt.subplot(1,3,i+1)   
#     plt.imshow(img)
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()

'''
คอนโวลูชั่นภาพ ด้วย Filter2D& ตัวกรองค่าเฉลี่ย (Mean Filter) *ลบ Noise
'''

# img = cv2.imread("img/noise.png")
# # kernel = np.ones((3,3),np.float32)/9

# filter2d = cv2.filter2D(img,-1,np.ones((3,3),np.float32)/25)
# mean= cv2.blur(img,(5,5))



# titles=["Original","filter2d 5x5","mean"]
# images=[img,filter2d,mean]

# for i in range(len(images)):
#     plt.subplot(1,3,i+1)   
#     plt.imshow(img)
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()

'''
 ตัวกรองค่ามัธยฐาน (Median Filter)&ตัวกรองเกาส์เซียน (Gaussian Filter) *ลบ Noise
'''

img = cv2.imread("img/noise.png")
# kernel = np.ones((3,3),np.float32)/9

filter2d = cv2.filter2D(img,-1,np.ones((3,3),np.float32)/25)
mean= cv2.blur(img,(5,5))
mblur = cv2.medianBlur(img,5)
gblur = cv2.GaussianBlur(img,(5,5),0)



titles=["Original","filter2d 5x5","Mean","Median","Gaussian"]
images=[img,filter2d,mean,mblur,gblur]

for i in range(len(images)):
    plt.subplot(2,3,i+1)   
    plt.imshow(img)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()