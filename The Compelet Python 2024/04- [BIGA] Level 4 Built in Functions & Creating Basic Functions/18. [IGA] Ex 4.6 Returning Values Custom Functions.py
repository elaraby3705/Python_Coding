# 18. [IGA] Exercise 4.6 Returning Values from Custom Functions
# >>>>>>> Happy Coding >>>>>>>>>>>
degree_in_celsius = float(input("your degree is : "))

def celsius_to_fahrenheit(degree_in_celsius):
    converted_degree = (degree_in_celsius -32 )* 1.8
    return f"Your degree form Celsius to fahrenheit is : {converted_degree}"

celsius_to_fahrenheit(degree_in_celsius) # this line of code will not call the function because Env in pycharm
# if you used Google Colab it will call the function because the env
# here to make it happen and the code runs perfectly , we use the line print(calling in function )
print(celsius_to_fahrenheit(35))
print(celsius_to_fahrenheit(degree_in_celsius))
print(celsius_to_fahrenheit(32))
