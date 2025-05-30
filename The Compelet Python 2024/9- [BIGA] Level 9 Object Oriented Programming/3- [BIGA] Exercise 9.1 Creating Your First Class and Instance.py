# 3- [BIGA] Exercise 9.1 Creating Your First Class and Instance
"""
1- Use the class keyword  and then type the nme of your class that you are going to define . Please use a person's name.

2- Use the init constructor to create the initial behavior of this person . This person needs 2 pieces of information .
1 is the name and 2 is the age

3- print the 2 pieces of information
"""
class person:

    def __init__(self, name, age):
        print(f"fYor name is : {name} \n"
              f"your age is {age}")


person01 = person("Hammad", 99)


# what if we need to create class circle

class circle:

    def __init__(self, r ):
        r = float(input("what is the value of r : "))
        total = float(r * 3.14 *2)
        print(total)


circle(0)
