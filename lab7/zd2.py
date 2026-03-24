list=[2,4,5,6,4,3,4,8,8,0]
print(f"Исходный список: {list}")
dup = []
s = set()

for i in list :
    if i in s and i not in dup:
        dup.append(i)
    s.add(i)

if dup:
    print(f"Повторяющиеся элементы: {dup}")
else:
    print("В списке нет повторяющихся элементов")