import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
filename = "dataset.csv"
df = pd.read_csv(filename, low_memory=False)

# Look at df shape and other info
print(df.head())
print("\nDF Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\n")
df.info()
print(df.describe())

# See what percent of each column is missing, sort by those with most missing
missing_counts = (df.isnull().mean() * 100).sort_values(ascending=False)
print(missing_counts)

# Check to make sure there are no duplicate rowws
duplicates = df.duplicated().sum()
print("\nDuplicates: ", duplicates)
