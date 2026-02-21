n=int(input("введите количество слов "))
k=0
s=""
while n!=0:
    k+=1
    print("введите слово ")
    slovo=str(input())
    s+=slovo+" "
    n-=1
print(s)