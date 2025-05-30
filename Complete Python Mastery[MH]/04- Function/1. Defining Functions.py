# 1. Defining Functions

# create your own custom function
def greet (name , it):
    print(" Hello", name + " form ", it)

greet("Hammad", "DevOps")

# another function
def even_number(y):
    for y in range (0,10):
     if y % 2 == 0:
      print(y)
even_number("")

# if we can create a function that is responsible for finding all the even numbers in range of a given value for the user

def even(z):
    z= int(input("please insert our value form 0 to 1000 "))
    for z in range (0, z):
        if z %2== 0:
            print(z)
even(z=0)

