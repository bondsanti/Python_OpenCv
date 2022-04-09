import cv2
import numpy
'''
แสดงพิกัดด้วย Mouse Event
'''

# img = cv2.imread("img/tree.jpg")

# def clickPosition(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         text = str(x)+","+str(y)
        
#         cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
#         cv2.imshow("Result",img)

# cv2.imshow("Result",img)      
# cv2.setMouseCallback("Result",clickPosition) #ทำงานกับ Mouse
# cv2.waitKey(0)
# cv2.destroyAllWindows()


'''
แสดงค่าสีด้วย Mouse Event
'''

# img = cv2.imread("img/tree.jpg")

# def clickPosition(event,x,y,flags,param):
#     if event == cv2.EVENT_LBUTTONDOWN:
#         blue = img[y , x , 0]
#         green = img[y, x, 1]
#         red = img[y, x, 2]

#         text = str(blue)+","+str(green)+","+str(red)
        
#         cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),3)
#         cv2.imshow("Result",img)

# cv2.imshow("Result",img)      
# cv2.setMouseCallback("Result",clickPosition) #ทำงานกับ Mouse
# cv2.waitKey(0)
# cv2.destroyAllWindows()


'''
แสดงภาพ จากสุด pixel ด้วย Mouse Event
'''

img = cv2.imread("img/color.jpg")

def clickPosition(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y , x , 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        imgcolor = numpy.zeros([300,300,3],numpy.uint8)
        imgcolor[:] = [blue,green,red]
        cv2.imshow("Result",imgcolor)

cv2.imshow("Result",img)      
cv2.setMouseCallback("Result",clickPosition) #ทำงานกับ Mouse
cv2.waitKey(0)
cv2.destroyAllWindows()

