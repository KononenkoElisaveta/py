import csv

total = 0

with open("products.csv", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    print("Нужно купить:")
    for row in reader:
        print(row["продукт"], "-", row["количество"], "шт. за", row["цена"], "руб.")
        total = total + int(row["количество"]) * int(row["цена"])

print("Итоговая сумма:", total, "руб.")