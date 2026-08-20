import pandas as pd

data = pd.read_csv("C:/Users/omard/Desktop/Educational__Information/Data_Science_Projects/Data_Analysis/Python/Retail_Data/retail_data.csv")

print(data.head()) # Displays a summary of the date, the first 5 rows
print(data.shape) # Displays the dimension of data (150,14) means 150 rows/14 columns
print(data.info()) #Displays the column names, what they represent, the datatype and non null value count
print(data.describe(include="all"))


