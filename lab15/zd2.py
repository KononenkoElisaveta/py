import tkinter as tk
import requests
def translate(text):
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|ru"
    response = requests.get(url, timeout=5).json()
    return response["responseData"]["translatedText"]

def get_fact():
    try:
        url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
        response = requests.get(url, timeout=5)
        data = response.json()
        fact = data["text"]

        translated = translate(fact)

        msg.config(text=translated, fg="#1565C0")
    except:
        msg.config(text="Ошибка соединения!", fg="#C62828")

root = tk.Tk()
root.title("Интересный факт")
root.geometry("450x300")
root.configure(bg="#E3F2FD")
tk.Label(root, text="🧠 Интересный факт", font=("Arial", 18, "bold"),
         bg="#E3F2FD", fg="#1565C0").pack(pady=20)
tk.Button(root, text="Получить факт!", font=("Arial", 13, "bold"),
          bg="#1976D2", fg="white", relief="flat", padx=15, pady=8,
          cursor="hand2", command=get_fact).pack()
msg = tk.Label(root, text="", font=("Arial", 12), bg="#E3F2FD",
               fg="#1565C0", wraplength=400, justify="center")
msg.pack(pady=20, padx=20)

root.mainloop()