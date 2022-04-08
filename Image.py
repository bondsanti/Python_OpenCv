import cv2

#อ่านค่า & อ่านภาพ
# img = cv2.imread("img/python.png")
img = cv2.imread("img/python.png",0) #Gray
# img = cv2.imread("img/python.png",-1) #allfar canal

# print(img) #ดูค่า pixel สี
# print(img.ndim) #ดูภาพว่าเป็น array กี่ มิติ
# print(type(img)) #ชนิดของภาพ




# imgResize = cv2.resize(img,(400,400)) #ปรับเปลี่ยนขนาด
cv2.imshow("output",img) #การแสดงผลภาพ
# cv2.imwrite("output.jpg",img) #export ภาพ
#cv2.waitKey(delay=5000) #แสดงภาพตามเวลาที่กำหนด
cv2.waitKey(0)
cv2.destroyAllWindows()

