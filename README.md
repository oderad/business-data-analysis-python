# E-commerce business-data-analysis-python
This repository contains business data analysis for a practice e-commerce company utilizing python

## Business Problem
The business wants to understand what is driving sales,
whether discounts are effective, and whether there are
customer or product issues affecting performance.

## Objectives
- Analyze sales and revenue
- Evaluate discount performance
- Analyze customer behavior
- Identify return patterns
- Provide business recommendations

## Tools
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Key Findings
The customer mix is evenly divided between new and returning customers, with 75 orders from each group. Discounts are commonly applied to purchases and appear to increase sales activity, particularly for higher-priced products. Higher-priced products such as laptops, desks, and monitors generally receive larger discounts than lower-priced products. However, the data does not prove that discounts cause higher sales, so further testing is needed. There were also 8 returned orders, representing approximately 5.3% of all orders. Returns were concentrated among higher-priced products and were generally associated with low customer ratings.

## Recommendations
Implement or strengthen a customer rewards program designed to encourage repeat purchases, and measure whether the program increases the rate of second purchases. For higher-priced products, test targeted discount levels rather than simply increasing discounts, and evaluate the results based on units sold, revenue, and profit margin. Finally, investigate the causes of returns for higher-priced products, particularly those associated with low customer ratings, to determine whether product quality, customer expectations, or the sales process can be improved.

## Files
- summarized_data_Step_1.py — data summarization
- data_inspection_Step_2.py — data inspection
- data_cleaning_Step_3.py — data cleaning
- Create_Business_metrics_Step_4.py — Create data metrics and conduct data analysis, visuals included
- retail_data.csv — source dataset
- fixed_retail_data.csv — cleaned dataset
- visuals/ — charts used in the analysis
