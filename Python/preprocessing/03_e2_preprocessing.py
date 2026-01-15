import pandas as pd

file_path = "/Users/jenny/Desktop/project/data/household_finances.xlsx"

xls = pd.ExcelFile(file_path)
xls.sheet_names

e2 = pd.read_excel(file_path, sheet_name="Data", header=1)
#e2.head(15)

e2.rename(columns={e2.columns[0]: "Date"}, inplace=True)
e2["Date"] = pd.to_datetime(e2["Date"], errors="coerce")

e2 = e2.iloc[9:].reset_index(drop=True)

e2 = e2[["Date", "Household debt to income", "Household debt to assets", "Household financial assets to income"]]

e2["Date"] = e2["Date"].dt.to_period("Q").astype(str)
e2.rename(columns={"Date": "Quarter"}, inplace=True)

e2.head(10)

e2.to_csv("/Users/jenny/Desktop/project/data/e2_clean.csv", index=False)