# 4. Logical Operators
"""
and
or
not
"""

# "And operator "

age = 30
height = 170

message = "Eligible" if age == 30 and height== 170 else "Not Eligible "
print(message)

# Or Operator'
message01 = input("enter your age " ) if message == "Eligible" or message == 16 else " not even close "
print(message01)


# Not

value = 20
output = "it is the right value " if value == 30  and not value !=10 or 30 or 40 else " cool"
print(output)