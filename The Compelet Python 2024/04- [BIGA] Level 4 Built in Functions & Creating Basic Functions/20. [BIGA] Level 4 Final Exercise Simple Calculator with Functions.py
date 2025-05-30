# 20. [BIGA] Level 4 Final Exercise Simple Calculator with Functions
"""
# Expected out put be like : -
- Enter your value
- your operator
- your second value
- your result is
"""
print("Hello to the calculator app from python ")
value1= int(input("your first value is : "))
operator=input(" which operator do you need \n +, / , * , - : ")
value2= int(input("your second value is : "))

def cal(value1, operator, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return  value1 - value2
    elif operator == "*":
        return value1 *value2
    elif operator== "/":
        return  value1 / value2
    else:
        return  "Invalid operator , please rerun  the program again "

    return f" result  = {value1} {operator} {value2}"


print(cal(value1, operator, value2))


## this is the final lesson in level 4 congrats ,, happy coding to , practice makes perfect


