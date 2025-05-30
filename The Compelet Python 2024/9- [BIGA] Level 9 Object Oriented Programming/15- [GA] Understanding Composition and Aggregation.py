#15. [GA] Understanding Composition and Aggregation
class Engine:
    def start(self):
        print("Engine started ")

class Car:
    def __init__(self):
        self.engine = Engine() # composition

car = Car()

car.engine.start()

# it called composition between 2 classes
