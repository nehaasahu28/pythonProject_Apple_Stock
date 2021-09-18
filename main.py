
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
#%matplotlib inline
import seaborn as sns
sns.set(style= "darkgrid")
import sqlite3 as sql
#importing data
apple_df = pd.read_csv("/Users/neha_gupta/APPLE.csv",
                        index_col=0,
                        parse_dates=True)
conn = sql.connect("/Users/neha_gupta/apple.db")
stock_data = pd.read_sql_query("SELECT * from apple", conn)
conn.close()
print(apple_df.head())
print("--------------------------------------------------------------")
print(stock_data.head())
print("--------------------------------------------------------------")
# Describing the Shape of the Data
print("Apple Stock Details:")
print(apple_df.shape)
print(apple_df.dtypes)
print(apple_df.describe(include="all"))
print("--------------------------- \n")

print("Apple shape: ")
print(stock_data.shape)
print(stock_data.dtypes)
print(stock_data.describe(include="all"))

g = sns.pairplot(apple_df[['Open','High','Low']], plot_kws={'color':'#bddc0e'})

#apple.drop(columns='Volume', inplace=True)
#apple.isnull().sum()

#apple.dropna(subset = ['Adj Close'], inplace=True)
#print(apple.shape)
#print(apple.isnull().sum())

#apple["Low"].fillna('Lowest', inplace=True)

#print(apple.shape)
#print(apple.isnull().sum())
#print(APPLE.isnull().sum())

