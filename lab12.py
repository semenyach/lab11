from tkinter import *
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.name}")
        print(f"Тип кухни: {self.type}")

    def open_restaurant(self):
        print("Ресторан открыт\n")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, works):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors
        self.location = location
        self.works = works

    def showf(self):
        print("Вкусы:")
        for flavor in self.flavors:
            print(flavor)

    def addf(self, flavor):
        self.flavors.append(flavor)

    def removef(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)

    def checkf(self):
        f=input("Проверить на наличие:")
        if f in self.flavors:
            print(f"{f} в наличии")
        else:
            print(f"{f} не в наличии")


class Eskimo(IceCreamStand):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, works):
        super().__init__(restaurant_name, cuisine_type, flavors, location, works)

    def add_stick_ice_cream(self, flavor):
        self.addf("Эскимо " + flavor)

    def remove_stick_ice_cream(self, flavor):
        self.removef("Эскимо " + flavor)


class SoftIceCream(IceCreamStand):
    def __init__(self, restaurant_name, cuisine_type, flavors, location, works):
        super().__init__(restaurant_name, cuisine_type, flavors, location, works)

    def addsoft(self, flavor):
        self.addf("Мягкое " + flavor)

    def removesoft(self, flavor):
        self.removef("Мягкое " + flavor)

IceCreamStand1 = IceCreamStand("Гуща", "Итальянская", ["Пломбир", "Шоколадное", "Крем-брюле"], "Большая Морская 18", "10:00 - 20:00")

Eskimo1 = Eskimo("Кинокухня", "Кавказская", ["Ванильное", "Клубничное", "Вишнёвое"], "Вознесенский 44-46", "9:00 - 18:00")

Soft1 = SoftIceCream("Cool cream", "Индийская", ["Ванильное", "Шоколадное", "Апельсиновое"], "Садовая 54", "12:00 - 22:00")

IceCreamStand1.addf("Клубничное")
IceCreamStand1.removef("Крем-брюле")
IceCreamStand1.showf()
IceCreamStand1.checkf()



root = Tk()
root['bg'] = '#ffffff'
fl=Label(text='Доступные вкусы:')
fl.pack()
for i in IceCreamStand1.flavors:
    text=Entry(width=20)
    text.insert(0, i)
    text.pack()
root.mainloop()
