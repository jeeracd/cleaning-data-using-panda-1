import pandas as pd
import numpy as np

messyDataset = pd.read_csv('messy_dataset.csv')

emptyCells = messyDataset.isnull().sum()
#print(empty_cells) # Prints number of missing values in each column

messyDataset["Income"] = messyDataset["Income"].str.replace('k', '').str.replace(',', '').str.replace('K', '').astype(float) * 1000

incomeMode = messyDataset["Income"].mode()[0]
messyDataset["Income"] = messyDataset["Income"].apply(lambda x : incomeMode if x < 0 else x)

incomeAvg = messyDataset["Income"].mean()

print(f"Average Income: {incomeAvg}")

emptyCellsPct = (emptyCells / len(messyDataset)) * 100
print(emptyCellsPct)