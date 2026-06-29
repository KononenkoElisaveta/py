from PIL import Image

origImage = Image.open("download.jpg")

left = 0
top = 0
right = 270
bottom = 130

corImage = origImage.crop((left, top, right, bottom))

corImage.save('cor_Image1.jpg')


print("Программа выполнена!")