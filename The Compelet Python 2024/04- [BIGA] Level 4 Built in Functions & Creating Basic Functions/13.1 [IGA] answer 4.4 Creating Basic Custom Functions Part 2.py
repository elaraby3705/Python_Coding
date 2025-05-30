#13.1 [IGA] answer 4.4 Creating Basic Custom Functions Part
"""
names = input("who was on it (Titanic ) : \n")
Year = int(input("which Year is it : \n"))

def ti(name, year):
    year = Year -1912
    return f"{names} were on titanic when it sunk  {year} Years ago "

ti(names,year=Year)
"""

##################
"""
n_names= input("who was on titanic ? : \n ")
n_year = input("which Year is it : \n")

def ti01(name,year):
    year = int(year)
    year = year -1912
    year = str(year)
    print(f"{name} was on titanic since it sunk at : {year} ")


ti01(n_names,n_year)
# # # # # # # # # # # # # # 
# This part of code worked just fine , I am going to try it again 
names = input("who was on tiTanic ? \n ")
year = input("which year it sunk  :\n ")

def ti01(name, year):
  year = int(year)
  year = year - 1912
  year = str(year)
  print(f"{names} were on it when it sunk {year} Years ago")

ti01(names, year )
"""

##### TI02 -- another try
names = input("who was on ti ? \n ")
year = input("which year is it ? \n")

def ti02(name, year):
  year = int(year)
  year = year - 1912
  year = str(year)
  print(f" {names} was on it when it sunk {year} Years ago ")

ti02(names, year)

