# 10. [IGA] Inheritance Extending Functionality.
class car:
    def carbrand(self,name):
        self.name = name
        name = input("please enter your car name ")
        print(name)



class vehcile (car):
    def brand(self):
        print("This is a brand new car ")


car01 = car()
car01.carbrand("")
car01 = vehcile()
car01.brand()
