import pandas as pd

df = pd.read_csv('tips.csv')
print(df.loc[range(0,10)])
print(df.head()) # head prints the first 5 rows in the data frame
print(df.tail()) # for printing the last 5 rows in the data frame
df2 = pd.read_csv('original 2.csv')
print(df2.head())
print(df2.to_string()) # all of the data is not shown in normal print statements, use to_string for printing the whole data
print(df2.info()) # gives valuable information about the number of records, the type and null values in the data
newdf = df2.dropna() # it drops the null values from the dataframe
print(newdf.info())
df2.fillna(130 , inplace = True) # this will fill the null values with the value that is given in the function
print(df2.info())