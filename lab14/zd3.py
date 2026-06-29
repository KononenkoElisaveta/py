import sys
import tkinter as tk
sys.path.append("../lab13")
from zd1 import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, working_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.location = location
        self.working_hours = working_hours
        self.flavors = ["Шоколадное", "Ванильное", "Клубничное"]

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            return True
        return False

    def check_flavor(self, flavor):
        return flavor in self.flavors

stand = IceCreamStand("Морозко", "Мороженое", "ул. Ленина 5", "10:00-22:00")

root = tk.Tk()
root.title("🍦 " + stand.restaurant_name)
root.geometry("400x550")
root.configure(bg="#E3F2FD")
# Заголовок
tk.Label(root, text="🍦 " + stand.restaurant_name, font=("Arial", 20, "bold"),
         bg="#E3F2FD", fg="#1565C0").pack(pady=10)
tk.Label(root, text="📍 " + stand.location + "  |  ⏰ " + stand.working_hours,
         font=("Arial", 10), bg="#E3F2FD", fg="#1976D2").pack()
# Список
tk.Label(root, text="Сорта мороженого:", font=("Arial", 13, "bold"),
         bg="#E3F2FD", fg="#1565C0").pack(pady=(15, 5))

listbox = tk.Listbox(root, font=("Arial", 12), bg="#BBDEFB",
                     fg="#0D47A1", selectbackground="#1976D2",
                     border=0, height=7)
listbox.pack(padx=30, fill="x")
def refresh():
    listbox.delete(0, tk.END)
    for f in stand.flavors:
        listbox.insert(tk.END, "🍨 " + f)

refresh()
# Поле ввода
tk.Label(root, text="Новый сорт:", font=("Arial", 11),
         bg="#E3F2FD", fg="#1565C0").pack(pady=(15, 3))
entry = tk.Entry(root, font=("Arial", 12), bg="white",
                 fg="#0D47A1", relief="flat", bd=5)
entry.pack(padx=30, fill="x")
# Сообщение
msg = tk.Label(root, text="", font=("Arial", 11), bg="#E3F2FD")
msg.pack(pady=5)
# Кнопки
def add():
    flavor = entry.get().strip()
    if flavor:
        stand.add_flavor(flavor)
        refresh()
        entry.delete(0, tk.END)
        msg.config(text=flavor + " добавлено!", fg="#2E7D32")

def remove():
    selected = listbox.curselection()
    if selected:
        flavor = stand.flavors[selected[0]]
        stand.remove_flavor(flavor)
        refresh()
        msg.config(text=flavor + " удалено!", fg="#C62828")
    else:
        msg.config(text="Выберите сорт из списка!", fg="#E65100")
def check():
    flavor = entry.get().strip()
    if flavor:
        if stand.check_flavor(flavor):
            msg.config(text=flavor + " — есть в наличии! ✅", fg="#2E7D32")
        else:
            msg.config(text=flavor + " — нет в наличии ❌", fg="#C62828")
btn_frame = tk.Frame(root, bg="#E3F2FD")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="➕ Добавить", font=("Arial", 11, "bold"),
          bg="#1976D2", fg="white", relief="flat", padx=12, pady=6,
          cursor="hand2", command=add).pack(side="left", padx=5)

tk.Button(btn_frame, text="➖ Удалить", font=("Arial", 11, "bold"),
          bg="#42A5F5", fg="white", relief="flat", padx=12, pady=6,
          cursor="hand2", command=remove).pack(side="left", padx=5)

tk.Button(btn_frame, text="🔍 Проверить", font=("Arial", 11, "bold"),
          bg="#90CAF9", fg="#0D47A1", relief="flat", padx=12, pady=6,
          cursor="hand2", command=check).pack(side="left", padx=5)


root.mainloop()