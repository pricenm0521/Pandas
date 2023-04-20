# main.py

import numpy as np
import pandas as pd
'''
myData = np.array(['a','b','c','d', 'e', 'Cat', 42])
mySeries = pd.Series(myData)
print (mySeries)
print(type(mySeries))

myData = np.array([134.29, 136.97, 250.31, 312.28])
mySeries = pd.Series(myData,index=['IBM','P&G','Microsoft','Home Depot'])
print (mySeries)
# add KO to the series 
mySeries["KO"] = 62.5  # easiest way
print (mySeries)

# delete the P&G row
mySeries = mySeries.drop('P&G')
print(mySeries)

print(mySeries['IBM']) # index notation
print(mySeries[['IBM','KO']]) # index and list notation creates another series

myData = np.array([134.29, 136.97, 250.31, 312.28]) # becomes a column
mySeries = pd.Series(myData,index=['IBM','P&G','Microsoft','Home Depot'], name="Stock Price") # adds the index with a name
myData1 = np.array(['120.573B', '336.72B', '1.885T' , '335.974B']) # must be the same # of rows as firt series
mySeries1 = pd.Series(myData1, index=['IBM','P&G','Microsoft','Home Depot'], name="Market Cap") # second index, names must match

myDataFrame = pd.concat([mySeries, mySeries1], axis=1) # combines the series
# print(myDataFrame) removed as only needs to print once, this was a previous check

# add a name to the index column "Company"
myDataFrame.index.name = 'Company'

# add  Accenture as ACN, trading at 286.00, market cap 180B
myDataFrame.loc['ACN'] = [285.84, '180B']
print(myDataFrame)
'''

purchases = {
    'guava': [4, 8, 1, 11], 
    'pears': [44, 33, 88, 12],
    'avocados':[42, 100, 50, 900]
}
df = pd.DataFrame(purchases)
# print(df)

df.index=['Kroger', 'Publix', 'Remke', 'IGA']
df.index.name = 'Store'
print(df)

# Add two new rows by creating a new DataFrame and appending it to our DataFrame

newRows = {'guavas': [10, 20], # if this is 'guavas' then it will create NaN data
           'pears':[111,222], 
           'avocados':[200,3000]}
newDF = pd.DataFrame(newRows)
#print (newDF)
newDF.index=['Thriftway', 'Meijer']
newDF.index.name = 'Store'
#print(newDF)

# ignore_index = True means create a new index # for the row
# sort = False means don't sort the columns
df = pd.concat([newDF, df], ignore_index=False, sort=False)
print(df)

# we realized there is a problem with our guavas, delete all colmuns with missing values

# df.drop(['guava', 'guavas'], axis=1, inplace=True)
# second option is to tell it to drop anything with missing data using 
df.dropna(axis=1, inplace=True)
# third way 
# df = df.dropna(axis=1) can also change 1 to 'columns'
# print(df)

#very clunky way to do this
apples = {'apples':[1,2,3,4,5,6]}
# items() returns the iterator of the dictionary
for key,value in apples.items():
    df[key] = value
print(df)

# total apples across all stores
print(df["apples"].sum())

