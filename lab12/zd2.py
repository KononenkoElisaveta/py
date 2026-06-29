import json

with open("products.json", encoding="utf-8") as f:
    data = json.load(f)

name = input("Название: ")
price = int(input("Цена: "))
weight = int(input("Вес: "))
available = input("В наличии? (да/нет): ") == "да"

data["products"].append({
    "name": name,
    "price": price,
    "available": available,
    "weight": weight
})

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

for product in data["products"]:
    print("Название:", product["name"])
    print("Цена:", product["price"])
    print("Вес:", product["weight"])
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()