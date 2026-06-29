import sys
sys.path.append("../lab13")
from zd1 import Restaurant

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Шоколадное", "Ванильное", "Клубничное"]

    def show_flavors(self):
        print("Сорта мороженого:")
        for flavor in self.flavors:
            print("-", flavor)

stand = IceCreamStand("Морозко", "Мороженое")
stand.describe_restaurant()
stand.show_flavors()
