import cv2

img = cv2.imread("C:/Users/aliaksei.fezhanka/Downloads/aliaksei.fezhanka.png", 1)

print(type(img))
print(img)
print(img.shape)

resized_img=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("C:/Users/aliaksei.fezhanka/Downloads/aliaksei.fezhanka_resized.jpg", resized_img)
cv2.waitKey(5000)
cv2.destroyAllWindows()