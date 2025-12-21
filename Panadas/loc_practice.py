# loc_practice
import pandas as pd
def run_loc_practice():
    # 1.  create a DataFrame with custom Indices (Labels)
    # We use explicit string labels for rows : 'row_a' , etc.
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York ', 'Los Angeles', 'Chicago', 'Houston']
    }
# Setting the index explicitly to strings to demonstrate label-based selection.
    df = pd.DataFrame(data, index=['id_101', 'id_102', 'id_103', 'id_104'])
    print("___ Original DataFrame (with custom ID index) ___")
    print(df)
    print("\n")

    # . select a single row by Label
    print("__ 1. Select Row 'id_102' ___")
    row_selection = df.loc['id_102']
    print(row_selection)
    print("\n")

    # 3. Select multiple rows (Slicing)
    # Note : unlike the normal python lists , loc slicing includes the LAST items!
    print("___ 2. Select Rows from 'id_101' to 'id_103' ___")
    slice_selection = df.loc['id_101': 'id_103']
    print(slice_selection)
    print("\n")

    # 4. Select specific Row AND specific Columns.
    print("___ 3. Select 'Name' and 'City' for 'id_104' ___")
    subset_selection = df.loc ['id_104', ['Name', 'City']]
    print(subset_selection)

if __name__ == "__main__":
    run_loc_practice()