# 13. [IGA] answer 4.4 Creating Basic Custom Functions Part 2
"""
- This is to find out how many year the titanic sunk
- ask who was on Titanic
- ask what  year is it currently
- print Jake and rose was on Titanic currently which sunk 112 years ago
"""

names= input("who was on Titanic ? : \n ")
year  = input("what year is it : \n ")
def titanic(name, year):
  year =int(year)
  year = year -1912
  year = str(year)
  print(f"{names} Were on titanic which sunk {year} ago")

titanic(names,year)





