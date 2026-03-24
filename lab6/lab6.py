def zd1():
    s=int(input("введите число:"))
    if s%3==0:
        print ("da")
    else:
        print("net")

def zd2():
    try:
        s=int(input("введитее число: "))
        print(100/s)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ValueError:
        print("ValueError")

def zd3():
    s=input("введите дату (дд.мм.гггг)")
    d,m,y= s.split ('.')
    d=int(d)
    m=int(m)
    y=int(y)
    if d * m == y % 100:
        print(True)
    else:
        print(False)
def zd4():
    sum1=sum2=0
    s = input("введите число: ")
    if len(s) % 2 == 0:
        for i in range(len(s)):
            if i < len(s) // 2:
                sum1+=int(s[i])
            else:
                sum2+=int(s[i])
        if sum1 == sum2:
            print (True)
        else:
            print(False)
    else:
        print("оличество цифр должно быть четным")

print("задание 1")
zd1()
print("задание 2")
zd2()
print("задание 3")
zd3()
print("задание 4")
zd4()