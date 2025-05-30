# 12. Exercise

# def fizz_buzz(value):
#     value=int(input("your value is : "))
#     if value % 3 == 0 and value % 5 == 0:
#         print("fizz Buzz")
#     elif value %5 ==0:
#         print("buzz")
#     elif value %3 ==0:
#         print("fizz")
#     else:
#         print("Wrong Entry ")
# while fizz_buzz(value="")is True:
#     continue
# fizz_buzz(15)


#
def Fizz_Buzz(x_value):
    # int(input("Value is "))
    if (x_value % 3 == 0) and (x_value % 5):
        return "Fizz Buzz "
    if x_value % 3 == 0:
        return "Fizz"
    if x_value %5 ==0:
        return "Buzz"
print(Fizz_Buzz(15))


# redef this function
def fezzo_buzzo(val):
    if val % 3 == 0 and val % 5 == 0:
        # division By %3 and %5 and
        print("FIZZyBuzz")
    elif val % 5 == 0:
        # Division By %5
        print("BUZZ")
    elif val % 3 == 0:
        # Divison By 3
        print("FIZZ")
    else:
        print(val)

fezzo_buzzo(15)


# These 2 example