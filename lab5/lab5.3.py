slovo=str(input("введите слово: "))
for x in slovo:
    if x=="ф":
        print("ого!это редкое слово")
        break
else:
    print("эх, это не очень редкое слово")