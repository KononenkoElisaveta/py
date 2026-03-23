slovo=str(input("введите слово: "))
for x in slovo:
    if x=="ф" or x=="Ф":
        print("ого!это редкое слово")
        break
else:
    print("эх, это не очень редкое слово")