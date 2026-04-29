import cv2
for i in range(1, 6):
    filename = f'{i}.jpg'
    img = cv2.imread(filename)
    print(f'Обработка: {filename}')
    filtered_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    output_filename = f'filtered_{i}.jpg'
    cv2.imwrite(output_filename, filtered_img)

print('\nГотово')