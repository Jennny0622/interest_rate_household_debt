import pandas as pd
file_path = "/Users/jenny/Desktop/project/data/household_business_balance_sheet.xlsx"

xls = pd.ExcelFile(file_path)
xls.sheet_names

e1 = pd.read_excel(file_path, sheet_name="Data", header=1)
#e1.head(15)

e1.rename(columns={e1.columns[0]: "Date"}, inplace=True)
e1["Date"] = pd.to_datetime(e1["Date"], errors="coerce")

e1 = e1[e1["Date"].notna()].reset_index(drop=True)

#e1.columns
e1 = e1[["Date", "Household total liabilities", "Household net worth", "Household dwellings"]]

e1["Date"] = e1["Date"].dt.to_period("Q").astype(str)
e1.rename(columns={"Date": "Quarter"}, inplace=True)
#e1.head(10)

e1.to_csv("/Users/jenny/Desktop/project/data/e1_clean.csv", index=False)