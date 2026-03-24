weekd = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")

weekend = int(input("Сколько выходных на неделе вы хотите? (1-7): "))
if weekend < 1 or weekend > 7:
    print("Ошибка: Количество выходных должно быть от 1 до 7")
weekends = list(weekd[-weekend:])
workd = list(weekd[:-weekend])

print(f"Ваши выходные дни: {', '.join(weekends)}")
print(f"Ваши рабочие дни: {', '.join(workd)}")
