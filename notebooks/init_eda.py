# %%
# Imports
import pandas as pd
from pandas.api import types as ptypes

# %%
# Show all columns
pd.set_option('display.max_columns', None)

# Increase number of rows
pd.set_option('display.max_rows', 100)

# Don’t truncate wide columns
pd.set_option('display.max_colwidth', None)

# Let pandas/jupyter auto-detect the console width
pd.set_option('display.width', None)

# %%
# Kedro catalog load dataframe
df = catalog.load("data")
display(df.head(5))

# %%
# Count Duplicates
print(len(df) - df.drop_duplicates())

# %%
# Count Null Rows
print(df.isna().all(axis=1).sum())

# %%
# List data types of columns in dataframe
df.dtypes

# %%
# Identifies columns that are completely null
null_cols = df.columns[df.isna().all(axis=0)].tolist()
print(null_cols)

# %%
# Count number of nulls in each column
null_dict = df.isna().sum().to_dict()
print(null_dict)

# %%
# Find string columns that should potentially be numeric
for column in df.columns:
    if not ptypes.is_string_dtype(df[column]):
        continue
    s = df[column].str.strip()
    int_pattern = r"^-?[0-9]+$"
    float_pattern = r"^-?(?:[0-9]+\.[0-9]*|\.[0-9]+)(?:[eE][+-]?[0-9]+)?$"
    is_int = s.str.match(int_pattern).all()
    is_float = s.str.match(float_pattern).all()
    if is_int or is_float:
        print(f"{column} | Int: {is_int}, Float: {is_float}")
