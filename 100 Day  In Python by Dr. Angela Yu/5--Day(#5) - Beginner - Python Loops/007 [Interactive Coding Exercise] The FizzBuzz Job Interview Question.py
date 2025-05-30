# FIZZBUZZ
total = 0
for val in range(1, 101):
    # Range of our program
    if val % 3 == 0 and val % 5 == 0:
        # division By %3 and %5 and
        print("FIZZyBuzz")
    elif val % 5 == 0:
        # Division By %5
        print("BUZZ")
    elif val % 3 == 0:
        # Divison By 3
        print("FIZZ")
    else:
        print(val)
