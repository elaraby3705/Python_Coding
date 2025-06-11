# Arithmetic Rules In Python & stringing together
num01 = 10
num02 = '12'
num03 = 13.230
num04 = "2"
"""Ree = num01 + num02
print(Ree)""" # Unsupported operation int with str
Ree = f"{num01+ int(num02)}"
print(Ree) # value of Num01 and Num 02 as int values
""" print(Ree + 4 )""" # why this will generate error  ?
# Careful what is the output
Ree = num01+ int(num02)
print(Ree) # value of Num01 and Num 02 as int values
print(Ree + 5 )

print(type(Ree))
print(num01 + num03)

print(int(num04) + num03 * int(num04))# output is 28.46
print((int(num04) + num03) * int(num04))# Output 30.46
"Careful with these arithmetic rules in python "

# Happy coding
# Keep Practice ***


