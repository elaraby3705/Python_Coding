# 2. [BIA] Exercise 4.1 built in Functions that Use Math
"""
Isuzu is 1.70 Million market share.
Toyota is 2.3 Million market share.
Suzuki is 0.9 Million market share.

01- Create the Variables of market share for each brand
02- The average height is [Put the average height here ].
03- the maximum market share [put here ] also the minium market share .

"""
Isuzu_Msh = 1.70
Toyota_Msh = 2.3
Suzuki_Msh = 0.9
avg = (Isuzu_Msh + Toyota_Msh+ Suzuki_Msh)/3
print(f"The Maximum market Share is :{max(Isuzu_Msh,Toyota_Msh,Suzuki_Msh)} Md\n"
      f"The Minimum Market share is :{min(Isuzu_Msh,Toyota_Msh,Suzuki_Msh)}Md")
print(f"Isuzu Market share is :{Isuzu_Msh} Million Dollar\n"
      f"Toyota Market share is :{Toyota_Msh} Million Dollar\n"
      f"Suzuki Market Share is :{Suzuki_Msh} Million Dollar\n"
      f"The total average of the 3 Brands are :{avg}")
