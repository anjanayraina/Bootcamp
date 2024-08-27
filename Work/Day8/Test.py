import pandas as pd

data = [10 , 20, 30 , 40 , 50]
print(data)
my_series = pd.Series(data) # creating a series in pandas
print(my_series)
print(pd.Series([10 , 'a' , 'b' , 10.34 , 100])) # you can also store different datatypes in it
print(my_series[2])
new_series = pd.Series(data , index = ['a' , 'b' , 'c' , 'd' , 'e']) # custom labels can also be created using the index paramater inside the series function
print(new_series)

my_data_frame = {

    'calories': [1,2,3,4] ,
    'days' : [1,2,3,4]
}

