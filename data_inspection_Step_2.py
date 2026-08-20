import pandas as pd

# We stored the csv file as a data frame in the data variable
data = pd.read_csv("C:/Users/omard/Desktop/Educational__Information/Data_Science_Projects/Data_Analysis/Python/Retail_Data/retail_data.csv")

#Checks all columns for duplicate records
print(f'There are {data.duplicated().sum()} duplicate records') 

print('\nColumns with unique values:\n')

for col in ['Customer_Type','Product','Category'
            ,'Region','Salesperson','Returned','Payment_Method']:
    print(f'{col} {data[col].unique()}')

print('\nColumns with duplicate values:\n')

for dup in ['Order_ID','Order_Date','Customer_ID','Customer_Type','Product','Category'
            ,'Region','Salesperson','Units','Unit_Price','Discount','Returned','Payment_Method','Customer_Rating']:
    print(f'There are {data[dup].duplicated().sum()} duplicated values for {dup}')

print('\nColumns with null values:\n')

for na in ['Order_ID','Order_Date','Customer_ID','Customer_Type','Product','Category'
            ,'Region','Salesperson','Units','Unit_Price','Discount','Returned','Payment_Method','Customer_Rating']:
    print(f'There are {data[na].isna().sum()} null values for {na}')

print('\nData types:\n')

print(data.dtypes)