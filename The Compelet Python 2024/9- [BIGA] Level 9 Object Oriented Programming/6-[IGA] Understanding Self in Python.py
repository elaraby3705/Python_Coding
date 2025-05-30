# 6. [IGA] Understanding Self in Python
class carbrand():
    def __init__(self, name ):
        print("Hey! Welcome to the car Brand Manufacture  : ")
        print(f"Car brand name is : {name}")
        self.car_name = name
        #self.type = type


    def catg(self):
        self.type = type
        print(f"{self.car_name}  Super Faster ")
        print(f"{self.car_name} Super faster.\n"
              f" Is using  {self.type} as fuel  ")

    def fuel(self, type):
        self.type= type
car1 = carbrand("Isuzu")
car1.catg()
car1.fuel("Gas")