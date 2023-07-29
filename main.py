'''
Data Analysis is a process of inspecting, cleansing, transforming 
and modeling data with the goal of discovering useful information, 
informing conclusion and support decision-making.
--AUTO MANAGED TOOLS        Programming language
Qlik Q                      Python
tableau                     R
looker                      Julia
ZOHO Analytics

Auto-managed closed tools are closed source, expensive, limited & easy to learn
Programming languages are open source, free, extremely powerful 

-Data Analysis Process
Data Extraction > Data Cleaning > Data Wrangling > Analysis > Action

Python Libraries for Data Analysis
pandas - cornerstone of Data Analysis job with Python
matplotlib - foundational library for visualization
numpy - numeric library for calculations in python
seaborn - statistical visualization tool built on top of matplotlib
statsmodels - library with many advanced statistical functions
scipy - advanced scientific computing, including functions for optimization,
        linear algebra, image processing and much more.
scikit-learn - Machine Learning library for Python(not deep learning)

'''
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# # print(!head PandaExample/data/sales_data.csv)
# sales = pd.read_csv(
#     'PandaExample/data/sales_data.csv',
#     parse_dates=['Date'])
# print(sales)

# print(sales.head())
# print(sales.shape)    #Gives out no. of rows and column
# print(sales.info())   #gives column title and type
# print(sales.describe())   #gives statistical data 

# sum_of_numbers = 0

# # # perform the calculation here
# for i in range(18,535):
#     if i % 7 == 0:
#         sum_of_numbers = sum_of_numbers + i
# print(sum_of_numbers)

start = 18
end = 534
divisible_by_7_sum = 0

for num in range(start, end + 1):
    if num % 7 == 0:
        divisible_by_7_sum += num

print("The sum of all numbers divisible by 7 between {} and {} is: {}".format(start, end, divisible_by_7_sum))
