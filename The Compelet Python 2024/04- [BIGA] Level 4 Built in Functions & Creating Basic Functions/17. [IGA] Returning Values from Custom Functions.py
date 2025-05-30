# 17. [IGA] Returning Values from Custom Functions
def convert_ksa_to_egyp(a):
    a= a*13.25
    print(a)
convert_ksa_to_egyp(10)

# function using return
def convert_feht_to_c(c):
    return (c-32)/1.8
convert_feht_to_c(100)

#
def convert_f_to_c(c):
    return (c-32)/1.8

print(convert_f_to_c(100))

#

def my_name(f_name, l_name):
    f_s_name = f_name.title()
    f_l_name = l_name.title()
    return f"{f_s_name} {f_l_name}"

print(my_name("HaMudY ", "IbrHim"))
