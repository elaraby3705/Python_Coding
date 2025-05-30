# 6. xargs
def multiply (x, y, z, l):
    return  x* y

print(multiply(2,3, 4, 5 ))

#
def multiply01(*numbers):
    global result
    for numbers in numbers:
        result = numbers *numbers
    return result

print(multiply01(2, 3, 4, 5))

# this code up there we need to explanation by Thony

def multiply02(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total

print(multiply02(2 , 2, 3, 4))

# Happy Coding