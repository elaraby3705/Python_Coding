# Two Dimensional Numpy
import pandas as pd
def run_series_extraction():
    # 1. Create a sample DataFrame
    data = {
        'Product': ['Laptop', 'Mouse', 'Keyboard'],
        'Price': [1200, 5, 75],
        'Stock': [5, 100, 50 ]
    }
    df = pd.DataFrame(data)
    print("__ Original DataFrame __")
    print(df)
    print("\n")
    # 2. Extract the Price column as a Series
    # Using single brackets [] returns a series
    price_series = df ['Price']

    # 3. Check and print the type
    print("__Extract Column : 'Price'  __")
    print(price_series)
    print("\nType of extracted column: ", type(price_series))

    # 3. assertions for validation (optional but good for testing )
    if isinstance(price_series, pd.Series):
        print("\n SUCCESS : The Column was successfully extracted as a pd.series . ")
    else:
        print("\n ERROR: The extracted object is not a Series ")

if __name__ == "__main__":
    run_series_extraction()

