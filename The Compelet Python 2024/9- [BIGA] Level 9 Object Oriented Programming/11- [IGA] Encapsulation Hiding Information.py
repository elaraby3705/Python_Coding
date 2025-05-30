# 11. [IGA] Encapsulation Hiding Information
class Bankaccount():
    def __init__(self,balance):
        #To set element private
        self.__balance = balance
    def deposit(self, amount):
            self.__balance +=amount

    def get_balance(self):
            return self.__balance

account = Bankaccount(100)

account.deposit(50)
print(account.get_balance())



