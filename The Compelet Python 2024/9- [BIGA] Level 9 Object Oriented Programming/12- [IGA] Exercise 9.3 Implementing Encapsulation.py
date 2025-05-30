# 12. [IGA] Exercise 9.3 Implementing Encapsulation
"""
Define a class named computer, with attribute using double underscore , meaning __
Use brand and model constructor (arguments). Make brand and model private.
Define a function (meaning a method ) called ge info that only has the self atrribute
Get info should show (meaning return the brand and model
"""
class Computer:
    def __init__(self, brand ,model ):
       self.__brand = brand
       self.__model = model

    def get_info(self):
        return self.__brand + " " +self.__model

computer = Computer("Apple", "Mac book ")
computer01 = Computer("Dell ", "Dell XPS ")
print(computer.get_info())
print(computer01.get_info())