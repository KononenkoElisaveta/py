import sys
sys.path.append("../lab13")
from zd1 import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, location, working_hours):
        super().__init__(restaurant_name, cuisine_type)
        self.location = location
        self.working_hours = working_hours
        self.flavors = ["Шоколадное", "Ванильное", "Клубничное"]
        self.stick_types = []
        self.soft_types = []

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print("-", flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(flavor, "добавлено!")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(flavor, "удалено!")
        else:
            print("Такого сорта нет")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(flavor, "— есть в наличии!")
        else:
            print(flavor, "— нет в наличии")

    def add_stick(self, name):
        self.stick_types.append(name)
        print("На палочке добавлено:", name)

    def add_soft(self, name):
        self.soft_types.append(name)
        print("Мягкое мороженое добавлено:", name)

    def show_stick(self):
        print("На палочке:", self.stick_types)

    def show_soft(self):
        print("Мягкое:", self.soft_types)


stand = IceCreamStand("Морозко", "Мороженое", "ул. Ленина 5", "10:00-22:00")
stand.describe_restaurant()
stand.show_flavors()
stand.add_flavor("Фисташковое")
stand.remove_flavor("Ванильное")
stand.check_flavor("Шоколадное")
stand.add_stick("эскимо")
stand.add_soft("Мистер Твистер")
stand.show_stick()
stand.show_soft()