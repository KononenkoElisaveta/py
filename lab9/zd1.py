import cv2
img=cv2.imread('123.jpg')
h,sh,c=img.shape
print(f"размер:{h}x{sh},цветовые каналы:{c}")
cv2.imshow("image", img)
cv2.waitKey()
