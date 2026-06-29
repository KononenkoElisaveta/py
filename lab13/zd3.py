from zd1 import Restaurant

newRestaurant = Restaurant("Сосисочная", "Немецкая")
print("------------")
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)

newRestaurant.update_rating(4)