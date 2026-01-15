import pandas as pd

e1 = pd.read_csv("/Users/jenny/Desktop/project/data/e1_clean.csv")
e2 = pd.read_csv("/Users/jenny/Desktop/project/data/e2_clean.csv")

df = pd.merge(e1, e2, on="Quarter", how="left")
df = df.dropna()

df.to_csv("/Users/jenny/Desktop/project/data/analysis_df.csv", index=False)