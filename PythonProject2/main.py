import pandas as pd

import matplotlib.pyplot as plt


df = pd.read_csv("Space_Corrected.csv")
df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0,1'])


df.info()

print(df.info())
