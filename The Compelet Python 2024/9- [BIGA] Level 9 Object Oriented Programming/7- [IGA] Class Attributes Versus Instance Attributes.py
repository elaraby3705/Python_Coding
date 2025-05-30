# 7. [IGA] Class Attributes Versus Instance Attributes
"""
Define a class called car

define a class attribute called wheels

in the constructor define 1 : maker of the care and 2: model of the car

print the name and how many wheels there are
"""
from tkinter.font import names


class car:
    car_wheels = 4

    def __init__(self, name):
        print("Hi , welcome to the car class ")
        self.name = name
        print(f"The Car name is : {name}")

    def carmaker(self, type):
        self.type = type
        print(f"Isuzu  is the {self.name}")

    def carmodel(self, model):
        print(f"This is a {self.name} >> {self.type}"
              f"\n"
              f"Manufactured by  Isuzu,\n"
              f"With the model {model}")


# car1 = car("pickups")
car2 = car("D- Max ")
# car2.carmaker()
car2.carmaker("Pickups ")
car2.carmodel("1970")


