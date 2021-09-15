
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style= "darkgrid")
import sqlite3 as sql

apple = pd.read_csv("/Users/neha_gupta/APPLE.csv")
conn = sql.connect("/Users/neha_gupta/apple.db")
APPLE = pd.read_sql_query("SELECT * from APPLE", conn)
conn.close()
print(apple.head(420))
print("--------------------------------------------------------------")
print(APPLE.head(420))
print("--------------------------------------------------------------")