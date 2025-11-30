# dataframe_intro.py
import pandas as pd
# creating a dict for data
data = {
    "Name": ["Hammad", "ALI", "Sara", "Mona "],
    "Age": [30, 25, 22, 29],
    "Country": ["Egypt", "UAE", "KSA", "QATAR"],
}
# convert dictionary to a DataFrame
df = pd.DataFrame(data)

# Print the DataFrame
print("DataFrame created from dictionary")
print(df)

# Accessing a specific column

print("\n Names column")
print(df["Name"])

# Describe the numerical columns

print("\nStatistics:")
print(df.describe())
