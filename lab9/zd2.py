import cv2
img=cv2.imread('123.jpg')
if img is None:print("net kartinki")
h,w,c=img.shape
print(f"размер:{h}x{w},цветовые каналы:{c}")
fx=0
fy=0
small=cv2.resize((img,(0,0), fx==1.0/3, fy==1.0/3))
sh,sw,sc=small.shape
print(f"новый размер:{sh}x{sw}")
img2=cv2.flip(img,1)
img3=cv2.flip(img,0)
cv2.imwrite("imgSmall",small)
cv2.imwrite("flip1",img2)
cv2.imwrite("flip2",img3)