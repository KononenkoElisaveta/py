import tkinter as tk
import requests

API_KEY = "50beafa8fea9ed6725f6783b2eb90b4e"


def get_weather():
    city = entry.get().strip()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            msg.config(text="Город не найден!", fg="#C62828")
            return

        name = data["name"]
        temp = data["main"]["temp"]
        feels = data["main"]["feels_like"]
        desc = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]

        result = (f"🌍 {name}\n"
                  f"🌡 Температура: {temp}°C\n"
                  f"🤔 Ощущается как: {feels}°C\n"
                  f"☁️ {desc}\n"
                  f"💧 Влажность: {humidity}%\n"
                  f"💨 Ветер: {wind} м/с")

        msg.config(text=result, fg="#1565C0")
    except:
        msg.config(text="Ошибка соединения!", fg="#C62828")


root = tk.Tk()
root.title("Погода")
root.geometry("350x400")
root.configure(bg="#E3F2FD")

tk.Label(root, text="🌤 Погода", font=("Arial", 20, "bold"),
         bg="#E3F2FD", fg="#1565C0").pack(pady=15)

tk.Label(root, text="Введите город:", font=("Arial", 12),
         bg="#E3F2FD", fg="#1976D2").pack()

entry = tk.Entry(root, font=("Arial", 13), bg="white",
                 fg="#0D47A1", relief="flat", bd=5)
entry.pack(padx=30, fill="x", pady=5)

tk.Button(root, text="Узнать погоду", font=("Arial", 12, "bold"),
          bg="#1976D2", fg="white", relief="flat", padx=15, pady=6,
          cursor="hand2", command=get_weather).pack(pady=10)

msg = tk.Label(root, text="", font=("Arial", 12), bg="#E3F2FD",
               fg="#1565C0", justify="left")
msg.pack(padx=20)

root.mainloop()