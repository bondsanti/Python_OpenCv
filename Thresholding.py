import cv2
import matplotlib.pyplot as plt

'''
ฟังก์ชั่น Threshold ใน OpenCV
'''
# gay_img =cv2.imread("img/gradient.png")
# thres1,result1 = cv2.threshold(gay_img,128,255,cv2.THRESH_BINARY)
# thres2,result2 = cv2.threshold(gay_img,128,255,cv2.THRESH_BINARY_INV)
# thres3,result3 = cv2.threshold(gay_img,128,255,cv2.THRESH_TRUNC)
# thres4,result4 = cv2.threshold(gay_img,128,255,cv2.THRESH_TOZERO)
# thres5,result5 = cv2.threshold(gay_img,128,255,cv2.THRESH_TOZERO_INV)

# cv2.imshow("Original",gay_img)
# cv2.imshow("THRESH_BINARY",result1)
# cv2.imshow("THRESH_BINARY_INV",result2)
# cv2.imshow("TRUNC",result3)
# cv2.imshow("THRESH_TOZERO",result4)
# cv2.imshow("THRESH_TOZERO_INV",result5)
# images = [gay_img,result1,result2,result3,result4,result5]
# titles = ["Original","THRESH_BINARY","THRESH_BINARY_INV","TRUNC","THRESH_TOZERO","THRESH_TOZERO_INV"]
'''
แสดง Threshold ใน Matplotlib
'''
# for i in range(len(images)):
#     plt.subplot(2,3,i+1)
#     plt.imshow(images[i])
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

# plt.show()

'''
เปรียบเทียบค่า Threshold Value
'''

# img = cv2.imread("img/ant.jpg")
# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# thresh_value = [50,100,130,200,230]
# plt.subplot(231,xticks=[],yticks=[])
# plt.title("Original")
# plt.imshow(gray_img,cmap="gray")

# for i in range(len(thresh_value)):
#     thres,result = cv2.threshold(gray_img,thresh_value[i],255,cv2.THRESH_BINARY)
#     plt.subplot(232+i)
#     plt.title("%d"%thresh_value[i])
#     plt.imshow(result,cmap="gray")
#     plt.xticks([]),plt.yticks([])

# plt.show()

'''
ปรับค่า Threshold ด้วย Trackbar
'''
# def display(value):
#     pass

# cv2.namedWindow("Threshold")
# cv2.createTrackbar("value","Threshold",128,255,display)

# while True :
#     gray_img = cv2.imread("img/ant.jpg",0)
#     thresh_value = cv2.getTrackbarPos("value","Threshold")
#     thres,result =cv2.threshold(gray_img,thresh_value,255,cv2.THRESH_BINARY)
#     if cv2.waitKey(1) & 0xFF == ord("e"):
#        break
#     cv2.imshow("Threshold",result)
# cv2.destroyAllWindows()

'''
การใช้งาน Adaptive Threshold
'''
# img = cv2.imread("img/map.jpg",0)

# thres,result = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
# adth_mean = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)
# adth_Gaussian = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,1)

# cv2.imshow("THRESH_BINARY",result)
# cv2.imshow("ADAPTIVE_THRESH_MEAN_C",adth_mean)
# cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN_C",adth_Gaussian)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
เปรียบเทียบค่า BlockSize
'''

img = cv2.imread("img/map.jpg",0)

# thres,result = cv2.threshold(img,128,255,cv2.THRESH_BINARY)
# adth_mean = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,1)
size = [3,5,9,17,33] #ขนาด Block
plt.subplot(231,xticks=[],yticks=[])
plt.imshow(img,cmap="gray")

for i in range(len(size)):
    adth_mean = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,size[i],1)
    plt.subplot(232+i)
    plt.title("%d"%size[i])
    plt.imshow(adth_mean,cmap="gray")
    plt.xticks([]),plt.yticks([])
plt.show()



