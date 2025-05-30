# 5. [BIA] Stringing Together Variables
Name = 'DevOps'
age = 12
print(f"This is: {Name}"
      f"\n Age of : {Name} Is : {age} " )

# can we concatenate a string with a float value ??!  -- let's see .
Name = " Software Engineering "
Market_Value = float(12.05)
age = 25
print(f"Field name is : {Name } \n "
      f"With Market Share = {Market_Value} \n "
      f"For about {age} Years  ")
# print("Field name is : "+Name+ " \n With Market Share = " + Market_Value + " \n For about " + age + " Years  ")
"""
 print("Field name is : "+Name+ " \n With Market Share = " + str(Market_Value) + " \n For about " + age + " Years  ")
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
TypeError: can only concatenate str (not "int") to str
"""
print("Field name is : "+Name+ " \n With Market Share = " + str(Market_Value) + " \n For about " + str(age) + " Years  ")

# To avoid error you got two  ways for that first one is with lines 11 12 13
# second ways is to convert your printout lines with the string values for non string ones

### Happy coding ###
