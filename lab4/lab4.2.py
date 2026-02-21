nu=int(input("введите номер места, в вагоне 54 места:"))
if nu>=1 and nu<=54:
    if nu%2!=0 : print("нижнее")
    else: print("верхнее")
    if nu<=36 : print("купе")
    else: print("боковое")
else:
    print("такого места в вагоне нет")