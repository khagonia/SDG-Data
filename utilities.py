### UTILITY FUNCTIONS ###

# import pandas as pd

# count_null <function>
# count the null values of columns, given a dataframe
# 
# args:
#   - df <DataFrame>
#   - cols <List><string> : list of valid columns
# 
# returns:
#   - nulls <List><int> : list of null value count per column
def count_null(df, cols= []):
    if not cols: 
        cols = df.columns

    nulls = {}
    total= 0
    for col in cols:
        try:
          null_count = df[col].isnull().sum()
        except:
          print(f'Column {col} does not exist. Skipping')
        else:
          nulls[col] = null_count
          total = total + null_count

    if nulls:
       nulls['sum'] = total

    return nulls

# summarize_null <function>
# count the null values of each columns, given a dataframe
# prints our a verbose summary of null count per column
#
# if you need a function that return the null values, refer to count_null
# 
# args:
#   - df <DataFrame>
#   - cols <List><string> : (optional) list of valid columns,
#                         : default value is all columns in the given df
# 
def summarize_null(df, cols= []):
    if not cols: 
        cols = df.columns


    pad = len(max(cols, key=len))
    print('Column' + ' ' * pad + 'Null' + ' ' * 6 + 'Dtype')

    nulls = {}
    total= 0
    for col in cols:
        try:
          null_count = df[col].isnull().sum()
          print(f'{col}' + ' ' * (pad + 6 - len(col)) + f'{null_count}' + ' ' * (10 - len(str(null_count))) + str(df[col].dtypes))
        except:
          print(f'Column {col} does not exist. Skipping')
        else:
          nulls[col] = null_count
          total = total + null_count
        #print(type())
    if nulls:
       nulls['sum'] = total

# pad_null <function>
# pad null values in a dataframe, with a given value
#
# args:
#   - df <DataFrame>
#   - cols <List><string> : columns where padding will be applied
#                         : default, all valid columns of df
#   - type <List><string> : list of data types to be padded
#                         : there are default values to be padded per data type
#                         : accepted data types are int, float, string
#   - value <List><mixed> : (optional) list of values to be padded for each column
#   
def pad_null(df, cols = [], value = None):
    if not cols: 
        cols = df.columns

    
    for col in cols:
        try:
          df[col] = df[col].fillna(value)
        except:
          print(f'Column {col} does not exist. Skipping')
    
    return df
          