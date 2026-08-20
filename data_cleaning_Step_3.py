import pandas as pd

# We stored the csv file as a data frame in the data variable
data = pd.read_csv("C:/Users/omard/Desktop/Educational__Information/Data_Science_Projects/Data_Analysis/Python/Retail_Data/retail_data.csv")

# Organize the column names in arrays
acolm = ['Order_ID','Order_Date','Customer_ID','Customer_Type','Product','Category'
            ,'Region','Salesperson','Units','Unit_Price','Discount','Returned'
            ,'Payment_Method','Customer_Rating']

scolm = ['Category','Payment_Method','Salesperson','Region','Product'
        ,'Customer_Type','Returned','Customer_ID']

tcolm = ['Category','Payment_Method','Salesperson','Region','Product'
        ,'Customer_Type','Returned']

ncolm = ['Units','Unit_Price']
# Create for loops to standardize all the string columns

# .astype changes the column type to be a string
# .str means I want to perform a string operation on the columns

# .strip() truncates the values in the columns, removes empty spaces
for col in scolm:
    data[col] = data[col].astype('string').str.strip()

# .str.title() converts the string value to title, the first letter of each value is capitalized
for tcol in tcolm:
    data[tcol] = data[tcol].str.title()

for ncol in ncolm:
    data[ncol] = pd.to_numeric(data[ncol], errors = 'coerce')

# pd.to_datetime converts the value to a date value
# The errors = 'coerce' turns non date values into missing values NaT
# data['Order_Date'].dt.year
data['Order_Date'] = pd.to_datetime(data['Order_Date'], errors = 'coerce')


# Validate the cleaned data


# Validate categories are standardized
print(data.groupby('Category')['Units'].sum())



# Create a definition to standardize the discount column as a float value
def discount(x):
    if '.' in x:
        return float(x)
    else:
        return float(x.rstrip('%'))/100

# Apply the standardized float value to the Discount column
data['Discount'] = data['Discount'].apply(discount)

# Check the Discount column to see if any values are greater than 1 (i.e., > 100%)
if (data['Discount'] > 1.0).any() == True:
    print('Recheck the discount column')
else:
    print('All Discount values are ok')

# Check the Units column to make sure all units are greater than or equal to 0
if (data['Units'] < 0).any():
    print('Recheck the Units column')
else:
    print('All values in the units column are ok')

# Check for outliers in the customer rating column (must be between 1 - 5)
if (data['Customer_Rating']< 1.0).any():
    print('Recheck Customer Rating contains values less than 1')
elif (data['Customer_Rating'] > 5.0).any():
    print('Recheck Customer Rating contains values greater than 5')
else:
    print('The customer rating is ok')

# Now, we save the cleaned data into a csv 
# Set the index to false, if true then an extra column with the index will be added to the dataset
data.to_csv('C:/Users/omard/Desktop/Educational__Information/Data_Science_Projects/Data_Analysis/Python/Retail_Data/fixed_retail_data.csv', index = False)


