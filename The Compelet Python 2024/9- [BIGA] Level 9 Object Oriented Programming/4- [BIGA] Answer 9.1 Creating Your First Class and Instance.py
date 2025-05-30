# 4. [BIGA] Answer 9.1 Creating Your First Class and Instance

"""
- in this one we will try to create class that takes a circle radius form user then process the circumference inside the class
"""

class circle():
    def __init__(self):
        self.r = 0 # identifying the value of r

    def get_radius_from_user(self):
        self.r = float(input("The value of r is : "))
        # getting the value of r from the user .

    def calculate_circumference(self):
        return  2 * self.r * 3.14
        # processing the calculation

circle01 = circle()
# creating the class object .
circle01.get_radius_from_user()
# getting the radius value form user

print("Circumference ", circle01.calculate_circumference())
# I think now we have to run the project to see the output