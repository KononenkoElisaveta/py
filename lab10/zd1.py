from PIL import Image

# Если файл лежит в корне рабочей папки среды разработки,
# Python увидит его просто по имени
origImage = Image.open("download.jpg")

left = 0
top = 0
right = 270
bottom = 130

corImage = origImage.crop((left, top, right, bottom))

# Сохраняем просто по имени — файл появится там же, в корне проекта
corImage.save('cor_Image1.jpg')


print("Программа выполнена!")