import cv2


'''
อ่านภาพ
'''
#อ่านค่า & อ่านภาพ
# img = cv2.imread("img/python.png")
# img = cv2.imread("img/python.png",0) #Gray
# img = cv2.imread("img/python.png",-1) #allfar canal

# print(img) #ดูค่า pixel สี
# print(img.ndim) #ดูภาพว่าเป็น array กี่ มิติ
# print(type(img)) #ชนิดของภาพ




# imgResize = cv2.resize(img,(400,400)) #ปรับเปลี่ยนขนาด
# cv2.imshow("output",img) #การแสดงผลภาพ
# cv2.imwrite("output.jpg",img) #export ภาพ
# cv2.waitKey(delay=5000) #แสดงภาพตามเวลาที่กำหนด
# cv2.waitKey(0)
# cv2.destroyAllWindows()

'''
วาดเส้นตรงลงบนภาพ
'''
img = cv2.imread("img/python.png")

#วาดเส้นตรง
#line (ภาพ , จุดเริ่มต้น (x,y) , จุดสุดท้าย (x,y) , สี(BGR) , ความหนา)
cv2.line(img,(0,0),(100,100),(255,0,255),2)

#วาดสีเหลี่ยม
#rectangle (ภาพ , มุมซ้าย (x,y) , ล่างขวา (x,y) , สี(BGR) , ความหนา)
cv2.rectangle(img,(20,20),(100,200),(0,0,255),2)


#วาดวงกลม
#circle (ภาพ , ตำแหน่งจุดศูนย์กลาง (x,y) ,รัศมี , สี(BGR) , ความหนา)
cv2.circle(img,(100,100),(50),(255,0,0),2)

#วาดข้อความบนภาพ
#putText (ภาพ , ข้อความ ,พิกัดแสงข้ออความ (x,y), font , ขนาดข้อความ , สี(BGR) , ความหนา)
cv2.putText(img,"Test",(120,100),cv2.FONT_HERSHEY_SIMPLEX,1.5,(43,0,255),5)

cv2.imshow("output",img) #การแสดงผลภาพ
cv2.waitKey(0)
cv2.destroyAllWindows()

