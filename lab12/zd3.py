ru_en = {}

with open("en-ru.txt", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if " - " in line:
            eng, rus_part = line.split(" - ", 1)
        elif " – " in line:
            eng, rus_part = line.split(" – ", 1)
        else:
            continue

        rus_words = [w.strip() for w in rus_part.split(",")]

        for rus in rus_words:
            if rus in ru_en:
                ru_en[rus] = ru_en[rus] + ", " + eng
            else:
                ru_en[rus] = eng

with open("ru-en.txt", "w", encoding="utf-8") as f:
    for rus in sorted(ru_en):
        f.write(rus + " – " + ru_en[rus] + "\n")
print("Готово! Файл ru-en.txt создан.")