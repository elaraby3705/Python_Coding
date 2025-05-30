# 16. [GA] Level 9 Final Exercise Simple Bank Account Manager (17- answer )
# Instruction : -
"""
- Create a class called Bank Account with attributes for account number and balance
- Add methods to the $ Bank account class for deposit , withdrawal, and balance check.
- Create a dictionary called accounts to store multiple Bank account objects
- Implement a user interface to interact with the Bank Account Objects
"""
class BankAccount:
    def __init__(self, account_number ,balance=0):
        self.account_number = account_number
        self.balance= balance
        print(f"{account_number} {balance}")
        enput = int(input("please chose form the menu: (1,2,3,4 or 5): \n "))
        self.enput = enput
        # implementing the creation of new  account
        # we will do it in two ways first in the __init__ main second separate method

    def create_account(self,f_name, s_name, email , password ):
        self.f_name=f_name
        f_name= input(" your  first name: ")
        self.s_name =s_name
        s_name= input(" your  second name  name: ")
        self.email =email
        email= input(" your  email: ")
        self.password =password
        password = input(" your  password : ")
        print(f"your name is >>{f_name} {s_name}\n"
              f"With email >>{email}\n"
              f"Ofcourse password >>{password}")




    def deposit(self, new_deposit):

        new_deposit = int(input("Pls, how much ? \n "))
        print(f"Here is your deposit value {new_deposit}")
        # check_new_deposit  = boolean(new_deposit)
        check_new_deposit= bool(input(f"are you okay with that value{new_deposit} or you want to do somthing else( 0,1"))
        if check_new_deposit == 0:
            print(f"now I think your account balance has been toped up by {new_deposit}")
        else:
            print("Please try again later ")

    def withdrawal(self):
        print("Withdrawal ")

    def balance_check(self):
       print("")

    def ops(self):
        if self.enput ==1:
            print( "you are asking for creating account ")
        elif self.enput ==2:
            print("your are asking for deposit ")
        elif self.enput ==3:
            print("your are asking for withdrawal ")
        elif self.enput ==4:
            print("you are asking for Check balance ")
        elif self.enput ==5:
            print("you are asking for Exit ")
        else :
            print("Wrong! input try again with a value in range 1 to 5 ")
    accounts = {}


    while True:
        print("1. Create account ")
        print("2. Deposit")
        print("3. Withdrawal")
        print("4. Check balance")
        print("5.Exit")

        break

account1 = BankAccount("")
account1.ops()
account1.create_account("","","","")
