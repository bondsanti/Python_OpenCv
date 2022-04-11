import cv2
import numpy as np

'''
การสร้าง Color Trackbar
'''

img = np.zeros((200,250,3),np.uint8)#zeros((w,h,แชลแนลสี),np.uint8)
cv2.namedWindow("ColorTrackbar")

def display(value):
    pass

#เริ่มสร้าง Tracker
cv2.createTrackbar("Blue","ColorTrackbar",0,255,display)#createTrackbar("","แสดงในชื่อ",ค่าต่ำสุด,ค่าสูงสุด)
cv2.createTrackbar("Green","ColorTrackbar",0,255,display)#createTrackbar("","แสดงในชื่อ",ค่าต่ำสุด,ค่าสูงสุด)
cv2.createTrackbar("Red","ColorTrackbar",0,255,display)#createTrackbar("","แสดงในชื่อ",ค่าต่ำสุด,ค่าสูงสุด)

while True:
 cv2.imshow("ColorTrackbar",img)
 if cv2.waitKey(1) & 0xFF == ord("e"):
     break
 
 b = cv2.getTrackbarPos("Blue","ColorTrackbar")
 g = cv2.getTrackbarPos("Green","ColorTrackbar")
 r = cv2.getTrackbarPos("Red","ColorTrackbar")
 img[:] = [b,g,r]

cv2.waitKey(0)
cv2.destroyAllWindows()

