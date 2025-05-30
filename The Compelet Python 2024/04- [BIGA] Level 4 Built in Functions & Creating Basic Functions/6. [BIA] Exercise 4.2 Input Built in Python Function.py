# 6. [BIA] Exercise 4.2 Input Built in Python Function
"""
- Create a code that ask for 3 brand car and there launch date also market share assets
- Print the brand car with established date and there market share in 2024


Brand	First Launch	2025 Projected Market Value	Key Notes
Ford	1903 (Model A)	~$110 billion	Known for EV growth, especially with the Mustang Mach-E; strong U.S. market share​
MOVE ELECTRIC
.
Toyota	1936 (Model AA)	~$250–300 billion	Leading hybrid vehicle producer (e.g., Prius) and a major global automaker​
MOVE ELECTRIC
​
DRIVING ENTHUSIAST
.
Isuzu	1961 (Bellel, first car)	~$7–10 billion (commercial focus)	Dominates regional markets in trucks and utility vehicles, especially in Thailand and Australia​
CAREXPERT
​
ISUZU
.
Tesla	2008 (Roadster)	~$900+ billion	Pioneer in EVs with a strong global presence and cutting-edge technology​
MOVE ELECTRIC
​
DRIVING ENTHUS
"""
Car_brand = input("please pass your brand here:  \n")

establish_date = int(input("establish date is  :"))
Project_Market_Value = float (input("2025 Project Market Value2025 Project Market Value is  : "))
Key_Notes =str(input("Any key Notes  :"))
print(f"Brand name is  :{Car_brand}\n "
      f"Establish Date : {establish_date}\n"
      f"Project Market value : {Project_Market_Value} .B\n"
      f"Key Notes : {Key_Notes}\n "
      f"Happy coding ")