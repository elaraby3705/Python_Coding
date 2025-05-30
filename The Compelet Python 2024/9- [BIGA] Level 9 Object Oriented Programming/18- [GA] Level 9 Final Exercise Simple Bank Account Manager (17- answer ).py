# 18 [GA] Level 9 Final Exercise Simple Bank Account Manager (17- answer )
# Instruction : -
"""
- Create a class called Bank Account with attributes for account number and balance
- Add methods to the $ Bank account class for deposit , withdrawal, and balance check.
- Create a dictionary called accounts to store multiple Bank account objects
- Implement a user interface to interact with the Bank Account Objects
"""
class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number =account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance +=amount
        return self.balance

    def withdraw(self, amount):
        if amount<= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance"

    def check_balance(self):
        return self.balance

    accounts = {}
    while True:
        print("1. create account ")
        print("2. Deposit")
        print("3. Withdraw ")
        print("4. Check Balance  ")
        print("5. Exit ")

        choice = int(input(" Choose an option ").strip())

        if  choice == 1:
            acc_numb = input("Enter your account number ").strip()
            initial_balance = float(input("Enter your initial balance "))

            accounts[acc_numb]= BankAccount(acco_numb, initial_balance)

            print("account created. ")

        elif  choice == 2:
            acc_numb = input("Enter your new  account number ").strip()
            if acc_numb in accounts:
                dep_amount = float(input("Enter your deposit amount :  ").strip())
                nb = accounts[acc_numb].deposit(dep_amount)
                print("New Balance is : ", nb)
            else:
                print("couldn't find that account. With number ", acc_numb)

        elif  choice == 3:
            acc_numb = input("Enter your new  account number ").strip()
            if acc_numb in accounts:
                wid_amount = float(input("Enter your withdraw amount :  ").strip())
                nb = accounts[acc_numb].withdraw(wid_amount)
                print("Status : ", nb)
            else:
                print("couldn't find that account. With number ", acc_numb)


        elif  choice == 4:
            acc_numb = input("Enter your account number ").strip()
            if acc_numb in accounts:
                b = accounts[acc_numb].check_balance()
                print("your balance is  : ", b)
            else:
                print("couldn't find that account. With number ", acc_numb)
        elif  choice == 5:
            print("Thanks for Using  our service ")
            break


user1= BankAccount("", 0)
