# <Python for data analysis>
# 5.1 Introduction to pandas Data Structures
# page 129
import pandas as pd
import numpy as np
print('there are many ways to construct a DataFrame,')
print('one of the most common is from a dict of equal-lenth lists or Numpy arrays')
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'nevada', 'nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)

print('the resulting DataFrame will have its index assigned automatically as with Series')
print('and the columns are placed in sorted order')
print(frame)

print('the head method selects only the first five rows')
print(frame.head())

print("specify a sequence of columns, the DataFrame's columns will be arraged in the order")
print(pd.DataFrame(data, columns=['year', 'state', 'pop']))

print('if pass a column that isn\'t contained in the dict,')
print('it will appear with missing values in the result')
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
							index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)


