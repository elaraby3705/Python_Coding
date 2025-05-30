# 5. [BIGA] Level 5 Final Exercise Grocery Shopping List

"""
# Your code start here .
- step 01 : create the initial shopping list .
- step 02 : add apple to the list
-Step 03 :remove bread form the list
-step 04 :create the show list function
"""
shopping_list = ["Banana ", "Suger", "Rice", "Bread", "Soda "]
def show_list(shopping_list):
    print("\n \nThe original shopping list:-")
    for element in shopping_list:
        print(f"{element}")

show_list(shopping_list)

shopping_list.append("apple")
shopping_list.remove(shopping_list[3])

def show_list(shopping_list):
    print("\nShopping list after adding the apple and removing the bread: ")
    for element in shopping_list:
        print(f"{element}")


show_list(shopping_list)
print(len((shopping_list)))



