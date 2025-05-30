# 10. [BIA] Answer 4.3 Creating Custom Functions Part 1
"""
Now we will solve this solution by our own using a step ahead by asking the user for input
"""
def car_brand01():
    brand_name = str(input("Your car Brand is : \n"))
    brand_release_date  = int(input("Your brand release date is : \n  "))
    brand_market_values = float(input("Your brand Market value is  : \n "))
    print(f"The Brand Name is : {brand_name} General Motors "
          f"\nThe Brand Release date is : {brand_release_date} dc. "
          f"\nThe Brand Market value is : {brand_market_values} Billion $ .")
car_brand01()

# Happy Coding