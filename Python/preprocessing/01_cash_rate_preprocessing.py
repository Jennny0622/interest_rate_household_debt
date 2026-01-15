import pandas as pd
df = pd.read_excel('/Users/jenny/Desktop/project/cash_rate.xlsx', skiprows=11, header=None)
df = df.iloc[:,:2]
df.columns = ['date', 'cash_rate']
#print(df.head())

df['cash_rate'] = df['cash_rate'].ffill()
# print(df.info())

df['quarter'] = df['date'].dt.to_period('Q')
#print(df[["date", "quarter"]].head(10))

df_quarter = df.groupby("quarter")['cash_rate'].mean().reset_index()
df_quarter_10 = df_quarter.loc[(df_quarter['quarter']>="2015Q1") & (df_quarter['quarter']<='2025Q4')].copy()
#print(df_quarter_10.head(10))

df_quarter_10['rate_change'] = df_quarter_10['cash_rate'].diff()
#print(df_quarter_10.head())

df_quarter_10.to_csv('cash_rate_recent.csv', index=False)