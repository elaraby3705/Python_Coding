# 10. Nested Loops
# for x in range(3):
  #   for y in range (1):
    #     for z in range(12):
      #       print(x , (x+1)*"*", (z+1)* " >")
           # print(y, (z+1)* "-")
        #     print(x, (y+1)*"- " , (z+1)* ". ")

for x in range (2):
    for y in range (3):
        for z in range (2):
            for w in range (2):
                print(f"({x}, {y}, {z}, {w})")

# happy coding with loops