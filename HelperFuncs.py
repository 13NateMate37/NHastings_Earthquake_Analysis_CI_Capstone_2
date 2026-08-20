# An in-progress repository of helper functions
# to condense repetitive coded processes 



# Librairies needed

import pandas


def InitialInspect(data_frame):
    """
    Takes a pandas dataframe as an input and prints
    a structured summary of it.

    Shape,
    Column data types,
    Null value counts(per column),
    Duplicate counts(per column),
    Display a .describe() output,
    Display the the first 10 rows.   
    """
    print("Initial shape: (Row x Col)", data_frame.shape)
    print('=' * 50)

    print("Columns data types:\n", data_frame.dtypes)
    print('=' * 50)

    print("Missing value counts: ")
    for column in data_frame: 
        NullCount = data_frame[column].isnull().sum()
        print(f"{column}: {NullCount}.")
    print('=' * 50)

    print("Duplicate counts: ")
    for column in data_frame:
        DuplicateCount = data_frame[column].duplicated().sum()
        print(f"{column}: {DuplicateCount} duplicates.")
    print('=' * 50)

    print(".describe summary:")
    display(data_frame.describe())
    print("=" * 50)

    print("First 10 rows")
    display(data_frame.head(10))
    print("=" * 50)

