k=0
s=""
slovo=""
while slovo!="stop":
    k+=1
    print("введите слово ")
    slovo=str(input())
    if slovo!="stop": s+=slovo+" "
print(s)