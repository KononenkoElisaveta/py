import json

with open("products.json", encoding="utf-8") as f:
    data = json.load(f)  # читает как словарь

for product in data["products"]:
    print("Название:", product["name"])
    print("Цена:", product["price"])
    print("Вес:", product["weight"])
    if product["available"]:
        print("В наличии")
    else:
        print("Нет в наличии!")
    print()