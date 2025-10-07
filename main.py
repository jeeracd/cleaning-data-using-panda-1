import pandas as pd
import numpy as np

messyDataset = pd.read_csv('messy_dataset.csv')

emptyCells = messyDataset.isnull().sum()
#print(empty_cells) # Prints number of missing values in each column

income = pd.to_numeric(messyDataset["Income"], errors='coerce')
nonNumeric = income.isna().sum()
print(f"Non-numeric Income entries: {nonNumeric}")

#messyDataset["Signup_Date"] = pd.to_datetime(messyDataset["Signup_Date"])

print(messyDataset.dtypes)
stringColumns = messyDataset.select_dtypes(include=['object']).columns.tolist()
print(f"String columns: {stringColumns}")
'''
messyDataset["Income"] = messyDataset["Income"].str.replace('k', '').str.replace(',', '').str.replace('K', '').astype(float) * 1000

incomeMode = messyDataset["Income"].mode()[0]
messyDataset["Income"] = messyDataset["Income"].apply(lambda x : incomeMode if x < 0 else x)

incomeAvg = messyDataset["Income"].mean()
incomestd = messyDataset["Income"].std()

print(f"Average Income: {incomeAvg}")
print(f"Income Standard Deviation: {incomestd}")


messyDataset["Purchase_Amount"] = (messyDataset["Purchase_Amount"].astype(str).str.replace('$', '').str.replace(',', '').str.strip())
messyDataset["Purchase_Amount"] = pd.to_numeric(messyDataset["Purchase_Amount"], errors='coerce')
purchaseAmountMedian = messyDataset["Purchase_Amount"].median()
messyDataset["Purchase_Amount"] = messyDataset["Purchase_Amount"].fillna(purchaseAmountMedian)
paMin = messyDataset["Purchase_Amount"].min()
paMax = messyDataset["Purchase_Amount"].max()  


messyDataset["Purchase_Amount"] = ((messyDataset["Purchase_Amount"] - paMin) / (paMax - paMin))
print(messyDataset["Purchase_Amount"].describe())


emptyCellsPct = (emptyCells / len(messyDataset)) * 100
#print(emptyCellsPct)

# find duplicate rows
duplicates = pd.Series({col: messyDataset[col].duplicated().sum() for col in messyDataset.columns})
print(duplicates)

messyDataset = messyDataset.drop_duplicates()
total_rows = len(messyDataset)
nonDuplicates = messyDataset["ID"].nunique()

print(f"ID count: {nonDuplicates}")

duplicateNames = messyDataset.groupby("Name")["ID"].nunique()
print(f"Same name, different ID: " , duplicateNames.sum())

#Get Range
ageRange = messyDataset["Age"].max() - messyDataset["Age"].min()
print(f"Age Range: {ageRange}")

extremeValues = messyDataset["Income"].nlargest(5).tolist()
print(extremeValues)

messyDataset["Purchase_Amount"] = pd.to_numeric(messyDataset["Purchase_Amount"], errors='coerce')

median = messyDataset["Purchase_Amount"].median()
messyDataset["Purchase_Amount"] = messyDataset["Purchase_Amount"].fillna(median)
messyDataset["Purchase_Amount"] = messyDataset["Purchase_Amount"].astype(float)
print(messyDataset["Purchase_Amount"].describe())'''