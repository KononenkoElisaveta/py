def zd1():
    s=int(input("введите число:"))
    if s%3==0:
        print ("da")
    else:
        print("net")

def zd3():
    try:
        s=int(input("введитее число: "))
        print(100/s)
    except ZeroDivisionError:
        print("ZeroDivisionError")
    except ValueError:
        print("ValueError")

def zd3():
    s=input("введите дату (дд.мм.гггг)")
    d,m,y=s.split('.')
    d=int(d)
    m=int(m)
    y=int(y)
    if d*m==y%100:
        print(True)
    else:
        print(False)
def zd4():
