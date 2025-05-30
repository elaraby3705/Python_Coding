# 17.1 [IGA] Returning Values from Custom Functions (circle radius )
"""
Circle radius = 2 * Pi *R

- let's code
"""
import math

r= float(input(" Pls insert the R value : "))
"""
R = radius of a circle 
L = Length of a rectangle
W = width of a rectangle 
S = Side of a Square  
"""
# laws used here are
"""
1-Square :- 
    formula >> Area = (side)**2 
    formula >> perimeter = side * 4 
    formula >> Diagonal  = side // 2 
    
2- Rectangle :- 
    formula >> Area = length * width 
    formula >> perimeter = 2(length + width ) 
    formula >> Diagonal = 2//(length**2 + width **2) 
    
3- Circle : - 
    formula >> Circumference  = 2 *  pi *  r
    formula >> area = pi * r **2 
    formula >> Diameter  = 2r 
     
>>>>>Happy coding >>>>>>
"""
def r_cir(r):
    pi = 3.1415926539
    area_of_circle =  pi * r**2
    circ_of_circle = 2 * pi * r
    di_of_circle = 2 *r
    return (f"The area of circle  = {area_of_circle} \n"
            f"The Circumference of the circle  = {circ_of_circle}\n "
            f"Diameter = {di_of_circle} ")
r_cir(r)
print(r_cir(r))

side = int(input("your square ide is : "))
def square(side ):
    area_of_squar = side**2
    perimeter = 4 *side
    diagonal = math.sqrt(side)
    return (f" area of Square : {area_of_squar}\n"
            f"perimeter of Square is : {perimeter}\n"
            f"diagonal of Square is :{diagonal}")
print(square(side))

l = int(input("Rectangle length is  :  "))
w = int(input("Rectangle width is  :  "))

def rectangle(l ,w):
    area = l * w
    perimeter = (l + w )*2
    diagonal =math.sqrt((l**2) + (w**2))
    return (f"Area of rectangle is : {area} \n"
            f"perimeter of rectangle is : {perimeter}\n"
            f"diagonal of rectangle is : { diagonal}")
print(rectangle(l, w ))





