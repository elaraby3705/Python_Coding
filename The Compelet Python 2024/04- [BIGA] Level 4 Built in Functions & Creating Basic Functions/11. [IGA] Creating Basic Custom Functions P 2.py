# 11. [IGA] Creating Basic Custom Functions Part 2
brand_name = "Kia"
brand_release_date = 1960
brand_market_value = 245.233
def car_brand(brand_name, branad_release_date, brand_market_value):
    brand_name = brand_name + " Motors"
    brand_release_date = branad_release_date + 10
    brand_market_value = brand_market_value + 15
    print(brand_name, brand_release_date, brand_market_value)

car_brand(brand_name, brand_release_date, brand_market_value)

# let's give it another try because I need to do so.
"""
phone_brand = "Samsung"
phone_series = "A"
phone_model = 52
phone_sub_series = "s"
phone_release_price = 12500.250
def phone(phone_brand, phone_series, phone_model, phone_sub_series, phone_release_price):
    phone_brand01 = phone_brand
    phone_series01 = phone_series + " Series "
    phone_model01 = phone_model
    phone_sub_series01 = phone_sub_series + " Sub Series "

    print(phone_brand01, phone_series01, phone_model01, phone_sub_series01, phone_release_price)
    print(f"It's a phone called \n {phone_series}{phone_model01}{phone_sub_series} form {phone_brand01}  ")

phone(phone_brand, phone_series, phone_model, phone_sub_series, phone_release_price)
"""
# function 03
# let's do more than declaring variables outside the scope of the function.
# calling inside the function and asking the user for input too
"""
company_name = "Dell"
company_product = ["Pcs", "Laptops", "Workstations"]
product_model0= ["Inspirion ", "Latitude ", "XPS"]
product_number0 = ["13s", "15s", "19s"]
def ins(company_name, product_model0, product_number0):
    company_name01 = company_name + "Corporation "
    company_product01 = company_product[0]+"Electroins "
    which_product_you_have01 = input(f"Please tell us which product you form >>  {company_product} is : ")
    product_model01 = input(f"your product model form >> {product_model0} is :  ")
    product_number01 = input(f"Your Model number form >> {product_number0} is : ")
    product_category01 = input("please input your product category here ")
    print(f"The company name is {company_name01}\n "
          f"Company Product is {company_product01}\n"
          f"The product you have is :  {which_product_you_have01} Model : {product_model01} \n Number {product_number01}  Category : {product_category01}")

ins(company_name ,product_model0, product_number0)
"""

####
##############################
########
# lets do some code here
"""
brand_catg = {"Samsung " : ["Note Series ", "S series ", "A Series "]}
brand_modl = {"A series ": ["A73", "A73s " , "A52", "A52s"]}
brand_numb = {"S sub series ": ["50 Series ", "30 series ", "70 series ", "20series "]}
def phoned(cata , moda, numba):
    cat1 = str(input(f"which cat is your device included form : {brand_catg}"))
    mod1 =str(input(f"which model is your device are from : {brand_modl}"))
    numba1 = str(input(f"Which number of series is your device included form : {brand_numb}"))
    print(f"your device cat  is:  {cat1} \n Your device model is : {mod1}\n Your device number is : {numba1} ")

phoned(cata= brand_numb, moda=brand_modl, numba=brand_numb)
"""
"""
brand_catg = {"Samsung " : ["Note Series ", "S series ", "A Series "]}
brand_modl = {"A series ": ["A73", "A73s " , "A52", "A52s"]}
brand_numb = {"S sub series ": ["50 Series ", "30 series ", "70 series ", "20series "]}
def phoned(cata , moda, numba):
    cata = str(input(f"which cat is your device included form : {brand_catg}"))
    moda =str(input(f"which model is your device are from : {brand_modl}"))
    numba = str(input(f"Which number of series is your device included form : {brand_numb}"))
    print(f"your device cat  is:  {cata}"
          f"\n Your device model is : {moda}"
          f"\n Your device number is : {numba} ")

phoned(cata= brand_numb, moda=brand_modl, numba=brand_numb)
"""
"""
def pep(profession, dep):
    profession01 = "IT"
    dep01 = "DevOps"
    print(f"This is Hammad form  {profession01}\n"
          f"Which is currently working as: {dep01}  ")

pep(profession="IT" ,dep="non")
"""
def membaa(name, dep ):
    print(name, dep)
membaa("ahsraf","DevOps" )
membaa("ahsraf","DevOps" )
membaa("ahsraf","DevOps" )
membaa("ahsraf","DevOps" )
membaa("ahsraf","DevOps" )

data_of_date = [1960,1970,1990]
data_of_Type= ["co", "po", "EO"]
def managa(type01, date01):
    your_date=input(f"please enter your date form : {data_of_date}")
    if your_date == 1970 or your_date== 1960:
        print(f"good news , you've picked the date of {your_date}")
    else:
        print(f"Pleases tick with  with this list {data_of_date}")

    your_type = input(f"Please insert your type base on : {data_of_Type}")
    if your_type == "co" or your_type=="po" or your_type== "Eo":
        print(f"your data of type is {your_type}\n"
              f" Based on your : {your_date}")

managa(type01="",date01="" )