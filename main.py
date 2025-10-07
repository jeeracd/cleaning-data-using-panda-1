import pandas as pd
import numpy as np

messyDataset = pd.read_csv('messy_dataset.csv')

emptyCells = messyDataset.isnull().sum()
#print(empty_cells) # Prints number of missing values in each column

messyDataset["Income"] = messyDataset["Income"].str.replace('k', '').str.replace(',', '').str.replace('K', '').astype(float) * 1000

incomeMode = messyDataset["Income"].mode()[0]
messyDataset["Income"] = messyDataset["Income"].apply(lambda x : incomeMode if x < 0 else x)

incomeAvg = messyDataset["Income"].mean()

#print(f"Average Income: {incomeAvg}")

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
print(messyDataset["Purchase_Amount"].describe())