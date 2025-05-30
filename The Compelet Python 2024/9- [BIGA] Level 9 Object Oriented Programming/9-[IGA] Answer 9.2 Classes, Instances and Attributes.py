# 9. [IGA] Answer 9.2 Classes, Instances and Attributes
class car:
    car_wheel = 4
    def __init__(self, maker, model):
        self.maker = maker
        self.model = model

car1 = car("Audi ", "1930")
print(f"{car1.car_wheel }  wheel vehicle " )
print(car1.maker)
print(car1.model)

