# 8. [IGA] Exercise 9.2 Classes, Instances and Attributes
"""
Define a class called car

define a class attribute called wheels

in the constructor define 1 : maker of the care and 2: model of the car

print the name and how many wheels there are
"""

## we will try somthing different here using same principle

class square:
    def __init__(self, side):
        print("In this one were going to calculate the :"
              " Area of square and the perimeter  of the square  ")
        side = int(input("the square side = : "))
        self.side = side

    def squarearea(self):
        area = self.side * self.side
        print(f" The area of square = {area}")

    def squareperimeter(self):
        perimeter = self.side * 4
        print(f"The perimeter of this square is = {perimeter} ")

square1 = square(side="0")
square1.squarearea()
square1.squareperimeter()
