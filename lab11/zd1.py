import os
import cv2

os.makedirs("result", exist_ok=True)

for file in os.listdir("images"):
    img = cv2.imread("images/" + file)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("result/" + file, gray)
    print(file)