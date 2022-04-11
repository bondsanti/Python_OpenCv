import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img/girl.jpg")
cv2.imshow("Outout",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()