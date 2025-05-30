# 2. Arguments
# a  function to print out all the primary numbers from 1 to 100

def primary():
    number = 0
    while number <100:
        number +=1
        if number% 2!= 0 and number % number == 0 :
         print(number)
    print(f"These other values are not a primary number ")


primary()
# now we've managed for coding our function perfectly

# let's do this to that function >> passing arguments

# like if the user needs to do this thing but in range from 1 to a given value by the user

def numprimary(value1):
    value1 =int(input("Form (1 to 1000)\nYour value is : \n "))
    for values in range (1, value1):
        if values %2!= 0 and values % values ==0:
            print(values)

numprimary("")

# defining the same function with while and ignoring the variable inside the function calling

def primary01():
    num = int(input("Form 1 to 1000\nYour value is:  "))
    while num >0:
        num -=1
        if num % 2 !=0:
            print(num)

primary01()
