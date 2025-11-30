# column_selection.py
import pandas as pd 
# create a sample DataFrame 

data = {
    "Name": ["Hammad", "Ali", "Sara", "Mona"],
    "Age": [30, 25, 22, 28], 
    "Country": ["Egypt", "UAE", "KSA", "QATAR"], 
    "Salary":[1000, 1200, 1100, 1050]
}

df = pd.DataFrame(data)

# select a single colum 

age_column = df["Age"]
print("Single Column -Age:")
print(age_column)

# select multiple columns 
subset = df [["Name", "Country", "Salary"]]
print("\nMultiple columns - Name , country , salary: ")
print(subset)

# check the type 
print("\nTtype of single column:", type(age_column)) # series 
print("Type of multiple columns selection :", type(subset)) # DataFrame