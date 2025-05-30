# 13. [IGA] Answer 9.3 Implementing Encapsulation
class Adam:
    def __init__(self, karate, motorcycle):
        self.__karate = karate
        self.__motorcycle = motorcycle

    def get_info(self):
        print(" Hi , Ya Adam: Hena ")
        print("Braka 3amel eh ")
        return  self.__karate +" \n " + self.__motorcycle

Adam01 = Adam("Cap Hesham ","Toumcycle ")
Brouqa = Adam("Automoclye ", "Cars ")

print(Adam01.get_info())

print("\n")
print(Brouqa.get_info())