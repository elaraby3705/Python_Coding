def formated_name(f_name, l_name):
    formated_f_name= f_name.title()
    formated_l_name = l_name.title()
    return  f"{formated_f_name} {formated_l_name}"
print(formated_name("HaMMad", "IbRAihm"))

########################################################
def mobile(brand, category, model ):
    mob_brand = ["Samsung", "Apple", "Others"]
    mob_cat = ["Smart", "Tablet", "regular"]
    mob_mod = ["numbs","chars", "symbols"]
    return (f"{mob_brand}\n"
            f" {mob_cat}\n"
            f" {mob_mod}")

print(mobile("Samsung", "A cat ", "Numbers "))