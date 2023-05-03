class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.name = restaurant_name
        self.type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Название ресторана: {self.name}")
        print(f"Тип кухни: {self.type}")

    def open_restaurant(self):
        print("Ресторан открыт\n")

    def changerating(self):
        print(f"Текущий рейтинг: {self.rating} \nПоменять рейтинг на:")
        newrating=int(input(''))
        self.rating = newrating

newRestaurant = Restaurant("Vegan Pyramid", "Египетская", 5)
print(newRestaurant.name)
print(newRestaurant.type, "\n")
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()

def zad2():
    restaurant1 = Restaurant("Тбилисо", "Грузинская", 3)
    restaurant2 = Restaurant("Хочу харчо", "Мегрельская", 3)
    restaurant3 = Restaurant("Garcon", "Французская", 3)

    restaurant1.describe_restaurant()
    restaurant1.changerating()
    restaurant2.describe_restaurant()
    restaurant2.changerating()
    restaurant3.describe_restaurant()
    restaurant3.changerating()

zad2()



