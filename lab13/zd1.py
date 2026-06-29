class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 0  # для 13.3

    def describe_restaurant(self):
        print("Название:", self.restaurant_name)
        print("Тип кухни:", self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name, "открыт!")

    def update_rating(self, new_rating):  # для 13.3
        self.rating = new_rating
        print("Новый рейтинг:", self.rating)


if __name__ == "__main__":
    newRestaurant = Restaurant("Пицца Хат", "Итальянская")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()