# Explore Python syntax
# Functions: A group of related statements to perform a task and return a value
from fileinput import close


def to_celsius(x):
    """ Convert Fahrenheit to Celsius"""
    return (x-32) * 5/9
to_celsius(75)
to_celsius(105)
to_celsius(35)
print(to_celsius(15))
print(to_celsius(95))
print(to_celsius(125))
############################
# Conditional statements: Sections of code that direct program execution based on specified conditions
number = -4
if number > 0:
    print("number is positive ")
elif number == 0 :
    print("Number is Zero ")
else:
    print(" Number is negative ")