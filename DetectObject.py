import cv2
import numpy


'''
ตรวจจับกลุ่มวัตถุจากสี (Detect Object)
'''

# while True :
#     img= cv2.imread("img/ball2d.jpg")

#     #ช่วงสี BGR
#     lower = numpy.array([5,111,10])
#     upper = numpy.array([124,255,133])

#     mask=cv2.inRange(img,lower,upper)
#     res=cv2.bitwise_and(img,img,mask=mask)

#     if cv2.waitKey(1) & 0xFF == ord("e"):
#      break
#     cv2.imshow("Original",img)
#     cv2.imshow("Mask",mask)
#     cv2.imshow("Result",res)

# cv2.destroyAllWindows()

'''
ตรวจจับใบหน้าจากภาพ (Face Detection)
'''

# img= cv2.imread("img/boy.jpg")

# #อ่านไฟล์ xml classification
# face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")

# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# #จำแนกใบหน้า
# scaleFactor = 1.1
# minNeighber = 3
# face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

# #แสดงตำแหน่งที่เจอใบหน้า
# for (x,y,w,h) in face_detect:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# cv2.imshow("Original",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
ตรวจจับใบหน้าจากวิดีโอ (Face Detection)
'''
# capture = cv2.VideoCapture("img/Mark.mp4") #เปิดไฟล์ Video.mp4

# face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")#อ่านไฟล์ xml classification

# while (capture.isOpened()):
#     check , frame = capture.read() #รับภาพจากกล้อง frame ต่อ frame
#     if check == True:
#         gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         #จำแนกใบหน้า
#         scaleFactor = 1.1
#         minNeighber = 5
#         face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
#          #แสดงตำแหน่งที่เจอใบหน้า
#         for (x,y,w,h) in face_detect:
#            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
#            cv2.imshow("output",frame)
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#            break
#     else :
#      break
# capture.release()

# cv2.destroyAllWindows(0)

'''
ตรวจจับดวงตาจากภาพ (Eye Detection)
'''

# img= cv2.imread("img/girl.jpg")

# #อ่านไฟล์ xml classification
# eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# #จำแนกใบหน้า
# scaleFactor = 1.1
# minNeighber = 3
# eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

# #แสดงตำแหน่งที่เจอใบหน้า
# for (x,y,w,h) in eye_detect:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# cv2.imshow("Original",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
ตรวจจับดวงตาจากวิดีโอ (Eye Detection)
'''

# capture = cv2.VideoCapture("img/Mark.mp4") #เปิดไฟล์ Video.mp4

# eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

# while (capture.isOpened()):
#     check , frame = capture.read() #รับภาพจากกล้อง frame ต่อ frame
#     if check == True:
#         gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         #จำแนกใบหน้า
#         scaleFactor = 1.1
#         minNeighber = 5
#         eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
#          #แสดงตำแหน่งที่เจอใบหน้า
#         for (x,y,w,h) in eye_detect:
#            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
#            cv2.imshow("output",frame)
#         if cv2.waitKey(1) & 0xFF == ord("e"):
#            break
#     else :
#      break
# capture.release()

# cv2.destroyAllWindows(0)

'''
ตรวจจับดวงตาและใบหน้าจากภาพ
'''

# img= cv2.imread("img/girl.jpg")

# #อ่านไฟล์ xml classification
# face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

# gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# #จำแนกใบหน้า
# scaleFactor = 1.1
# minNeighber = 3
# face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
# eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)

# #แสดงตำแหน่งที่เจอใบหน้า
# for (x,y,w,h) in face_detect:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
#     for (ex,ey,ew,eh) in eye_detect:
#        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,0,0),3)

# cv2.imshow("Original",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




'''
ตรวจจับดวงตาและใบหน้าจากวิดีโอ
'''
capture = cv2.VideoCapture("img/Mark.mp4") #เปิดไฟล์ Video.mp4

face_cascade = cv2.CascadeClassifier("Detect/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("Detect/haarcascade_eye_tree_eyeglasses.xml")

while (capture.isOpened()):
    check , frame = capture.read() #รับภาพจากกล้อง frame ต่อ frame
    if check == True:
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #จำแนกใบหน้า
        scaleFactor = 1.1
        minNeighber = 5
        face_detect = face_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
        eye_detect = eye_cascade.detectMultiScale(gray_img,scaleFactor,minNeighber)
         #แสดงตำแหน่งที่เจอใบหน้า
        for (x,y,w,h) in eye_detect:
           cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
           for (ex,ey,ew,eh) in face_detect:
            cv2.rectangle(frame,(ex,ey),(ex+ew,ey+eh),(255,0,0),3)
           cv2.imshow("output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
           break
    else :
     break
capture.release()

cv2.destroyAllWindows(0)