import cv2
import datetime

'''
เปิดกล้อง
'''

# capture = cv2.VideoCapture(0)

# while (True):
#     check , frame = capture.read() #รับภาพจากกล้อง frame ต่อ frame
#     cv2.imshow("output",frame)

#     if cv2.waitKey(1) & 0xFF == ord("e"):
#         break

# capture.release()
# cv2.destroyAllWindows(0)

'''
อัดวีดีโอ
'''

# capture = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')

# #("ชื่อไฟล.นามสกุล",ไฟล์,เฟรมเรท,(ุ640,480))
# result = cv2.VideoWriter("output.mp4",fourcc,20,(640,480))

# while (capture.isOpened()):
#     check , frame = capture.read() #รับภาพจากกล้อง frame ต่อ frame
#     cv2.imshow("output",frame)
#     result.write(frame)
#     if cv2.waitKey(1) & 0xFF == ord("e"):
#         break

# result.release()
# capture.release()
# cv2.destroyAllWindows(0)


'''
เปิดไฟล์ วีดีโอ
'''
capture = cv2.VideoCapture("img/video.mp4") #เปิดไฟล์ Video.mp4
while (capture.isOpened()):
    check , frame = capture.read() #รับภาพจากกล้อง frame ต่อ frame

    if check == True:
     currentDate = str(datetime.datetime.now())
     cv2.putText(frame,currentDate,(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),2)
    #  vdoGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#ปรับสี Video เป็นสีเทา
     cv2.imshow("output",frame)
     if cv2.waitKey(1) & 0xFF == ord("e"):
      break
    else :
     break
capture.release()
cv2.destroyAllWindows(0)