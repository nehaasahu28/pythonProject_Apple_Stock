
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style= "darkgrid")
import sqlite3 as sql

apple_st = pd.read_csv("APPLE.csv")
conn = sql.connect("apple.db")
APPLE = pd.read_sql_query("SELECT * from APPLE", conn)
conn.close()
print(apple_st.head(7))
print("--------------------------------------------------------------")
print(APPLE.head(7))
print("--------------------------------------------------------------")