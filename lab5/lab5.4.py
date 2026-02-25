import random
x=0
y=0
while x!=3:
    sum1=random.randint(1,10)
    sum2=random.randint(1,10)
    k=int(input(f"{sum1}+{sum2}="))
    if k==sum1+sum2:
        print("ответ верный")
        y+=1
    else:
        x+=1
        print("ответ неверный")
print("игра окончена, правильных ответов", y)