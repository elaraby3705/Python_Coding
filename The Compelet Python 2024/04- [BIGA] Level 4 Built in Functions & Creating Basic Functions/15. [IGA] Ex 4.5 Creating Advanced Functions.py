# 15. [IGA] Exercise 4.5 Creating Advanced Functions  Keyword and Default Values)
"""
- Create a function called my_age with 1 variable in bracket called age .
- in the custom function print my age (your_age)
- call the function using the age of 39
- change the default age in the function to 19
- call the function with nothing in brackets
"""
def my_age(age=19):
    print(f" My age is {age}")

my_age(39)
my_age()