import pandas as pd

import sqlite3

data = pd.read_csv("bmi.csv", sep="\t")
print(data.tail(2))
