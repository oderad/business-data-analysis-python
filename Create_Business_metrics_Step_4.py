import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# We stored the csv file as a data frame in the data variable
data = pd.read_csv("C:/Users/fixed_retail_data.csv")

# Create metrics

# Create the calculated discount column
data['Calculated_Discount'] = 1 - data['Discount'] 

# Create a revenue column
data['Revenue'] = (data['Units'] * data['Unit_Price'] * data['Calculated_Discount'])

# Create The returned revenue column
for a in data['Returned']:
    if a == 'Yes':
        data['Returned_Revenue'] = data['Returned']
    else: data['Returned'] = 0

# Create a net revenue column
# Net Revenue is the revenue a company makes after returns, discounts, etc. 
data['Net_Revenue'] = data['Revenue'] - data['Returned_Revenue']

##### Now, start asking questions

# Find the net revenue by product
# Looking for:
# Top products
# Bottom products
# Concentration of revenue
#Products with unusually high/low performance
prod_rev = data.groupby('Product')['Net_Revenue'].sum().sort_values(ascending = False)

# Find the net revenue by category
# Looking for:
# Top categories
# Bottom categories
cat = data.groupby('Category')['Net_Revenue'].sum().sort_values(ascending = False)

# Find the net revenue by customer_type
# New vs Returning customer value
# Average Order differences
# Customer retention opportunities
cust = data.groupby('Customer_Type')['Net_Revenue'].agg( ['sum','mean','count'])

# Find the net revenue by region
# Looking for:
# Strong regions
# Weak regions
# Large performance gaps
reg = data.groupby('Region')['Net_Revenue'].sum().sort_values(ascending = False)

# Find the net revenue by salesperson
# Looking for:
# Best performing sellers
# Underperforming sellers
sper = data.groupby('Salesperson')['Net_Revenue'].sum().sort_values(ascending = False)

# This analysis helps to understand what actually drives the business 
print(prod_rev)
print(cat)
print(cust)
print(reg)
print(sper)

# Specifically answer the VPs question

danal = data.groupby('Discount').agg(
    Revenue = ('Net_Revenue','sum'),
    Units = ('Units','sum'),
    Orders = ('Order_ID','count'),
    Avg_Price = ('Unit_Price','mean')
)
# Does applying a discount appear to generate enough additional volume
# Looking for:
# If the discount increases do the unit sales increase
# If discount increases does the net revenue increase
print(danal)

# Analyze returns
# Looking for products with high returns
# Regions with high returns

returns = []

for a in data['Returned']:
    if a == 'Yes':
        returns.append(1)
    else:
        returns.append(0)

data['Return'] = returns

ret = data.groupby('Product')['Return'].mean()
 # In this case there is a 0 return rate so no need to go further
print(ret)

# Create visuals to answer questions, dont create visuals just to create

# Question 1 Which category generates the most revenue
plt.figure()
sns.barplot(
    data=data,
    x="Category",
    y="Net_Revenue",
    errorbar = None
)
plt.title('Category Net Revenue')

# Question 2 How are regions performing
plt.figure()
sns.barplot(
    data=data,
    x='Region',
    y='Net_Revenue',
    errorbar = None
)
plt.title('Region Revenue')

# Do discounts relate to revenue
plt.figure()
sns.scatterplot(
    data=data,
    x='Discount',
    y='Unit_Price'
)

data['Discounts'] = (data['Discount']*100)

dsc = data.groupby('Discounts')['Unit_Price'].mean()
plt.figure()
plt.scatter(dsc.index, dsc)
plt.xlabel('Discounts')
plt.ylabel('Average Unit Price')

plt.figure()
sns.barplot(
    data=data,
    x='Customer_Type',
    y='Discount',
    errorbar = None
)
plt.title('Region Revenue')

plt.show()

rcus = data.groupby('Customer_Type')['Discount'].sum()
print(rcus)
