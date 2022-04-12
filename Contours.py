import cv2

'''
หาเส้นเค้าโครงภาพ (Contours)
'''
# img = cv2.imread("img/ant.jpg")
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# thresh,result = cv2.threshold(img_gray,215,255,cv2.THRESH_BINARY)

# contours,hierarchy = cv2.findContours(result,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# # print(len(contours))
# cv2.drawContours(img,contours,-1,(0,0,255),2)

# cv2.imshow("output",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
ตรวจจับการเคลื่อนไหว (Motion Detection)
'''
# capture = cv2.VideoCapture("img/Walking.mp4")
# check , frame1 = capture.read() #รับภาพจากกล้อง frame ต่อ frame
# check , frame2 = capture.read() #รับภาพจากกล้อง frame ต่อ frame

# while (capture.isOpened()):
   
#     if check == True:
#         motiondiff=cv2.absdiff(frame1,frame2)
#         img_gray = cv2.cvtColor(motiondiff,cv2.COLOR_BGR2GRAY)
#         blur = cv2.GaussianBlur(img_gray,(5,5),0)
#         thresh,result = cv2.threshold(blur,15,255,cv2.THRESH_BINARY)
#         dilation = cv2.dilate(result,None,iterations=3)
#         contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#         cv2.drawContours(frame1,contours,-1,(0,0,255),2)
#         cv2.imshow("output",frame1)
#         frame1 = frame2
#         check , frame2 = capture.read()
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#            break
#     else :
#      break

# capture.release()

# cv2.destroyAllWindows(0)


'''
ติดตามการเคลื่อนไหว (Motion Tracker)
'''

capture = cv2.VideoCapture("img/Walking.mp4")
check , frame1 = capture.read() #รับภาพจากกล้อง frame ต่อ frame
check , frame2 = capture.read() #รับภาพจากกล้อง frame ต่อ frame

while (capture.isOpened()):
   
    if check == True:
        motiondiff=cv2.absdiff(frame1,frame2)
        img_gray = cv2.cvtColor(motiondiff,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(img_gray,(5,5),0)
        thresh,result = cv2.threshold(blur,15,255,cv2.THRESH_BINARY)
        dilation = cv2.dilate(result,None,iterations=3)
        contours,hierarchy = cv2.findContours(dilation,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

        for contour in contours:
         (x,y,w,h) =  cv2.boundingRect(contour)
        if cv2.contourArea(contour)<2500:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
        
        cv2.imshow("output",frame1)
        frame1 = frame2
        check , frame2 = capture.read()
        if cv2.waitKey(1) & 0xFF == ord("e"):
           break
    else :
     break

capture.release()

cv2.destroyAllWindows(0)


