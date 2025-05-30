# 6. Chaining Comparison Operators
# age should be between 18 and 65
age = 35
if age >= 18 and age < 65 :
    print("Eligible")
else:
    print(" not eligible")

# another way to do so using chaining Comparison

message  = "Eligible" if age >= 18 and age <65 else " not eligible "
print(message)

# a cleaner way
message01 = "In range " if 18<= age <65 else print("not even close ")
print(message01)