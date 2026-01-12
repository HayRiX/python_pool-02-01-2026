#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    def __init__(self, name, height, age, color: str):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")
        print(f"{self.name} is blooming beautifully!\n")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: int):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade = self.trunk_diameter * 1.56
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {int(shade)} square meters of shade\n")


class Vegetable(Plant):
    def __init__(self, name, height, age,
                 harvest_season: str, nutritional_value: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def nutritional(self):
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in {self.nutritional_value}\n")


print("=== Garden Plant Types ===\n")

flower1 = Flower("Rose", 25, 30, "red")
flower2 = Flower("Hydrangeas", 115, 90, "purple")

tree1 = Tree("Oak", 500, 1825, 50)
tree2 = Tree("Spruce", 883, 2687, 70)

vegetable1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
vegetable2 = Vegetable("Potato", 75, 78, "summer", "potassium")

flower1.bloom()
flower2.bloom()
tree1.produce_shade()
tree2.produce_shade()
vegetable1.nutritional()
vegetable2.nutritional()
