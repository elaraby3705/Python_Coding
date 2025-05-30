# 9. Debugging

# how to create a bug and debug it in python
def multiply(*numbers):
    total = 1
    for number in numbers:
        total*=number
    return total
print("Start")
print(multiply(1,2,3))
