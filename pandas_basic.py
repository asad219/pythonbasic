import pandas as pd

print("Pandas Version:")
print(pd.__version__)

# Create a simple DataFrame
data = {
    'EmployeeId': [1, 2, 3, 4],
    'Name': ['Ahmed', 'Nabeel', 'Jawwad', 'Asad'],
    'Age': [25, 30, 35, 45],
    'City': ['Dubai', 'Ajman', 'Sharjah', 'Abu Dhabi'],
    'Country': ['PK', 'IND', 'UAE', None]
}

data1 = {
    'EmployeeId': [1, 2, 3, 4],
    'Name': ['Ahmed', 'Nabeel', 'Jawwad', 'Asad'],
    'Age': [25, 30, 35, 45],
    'City': ['Dubai', 'Ajman', 'Sharjah', 'Abu Dhabi'],
    'Country': ['PK', 'IND', 'UAE', 'Germany'],
    'Salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)
df1 = pd.DataFrame(data1)
print(df)

# Get a statistical summary of the DataFrame
print("\nStatistical Summary:")
print(df.describe())

# Get the column names of the DataFrame
print("\nShape of the DataFrame:")
print(df.shape)

# Get the column names of the DataFrame
print("\nColumn Names of the DataFrame:")
print(df.columns)

# Get the first few rows of the DataFrame
print("\nFirst Few Rows of the DataFrame:")
print(df.head())

# Get the last few rows of the DataFrame
print("\nLast Few Rows of the DataFrame:")
print(df.tail())

# Get a concise summary of the DataFrame
print("\nConcise Summary of the DataFrame:")
print(df.info())

# Get the number of missing values in each column of the DataFrame
print("\nMissing Values in Each Column of the DataFrame:")
print(df.isnull().sum())

# Drop rows with missing values and display the resulting DataFrame
K = df.dropna()
print("\nDataFrame After Dropping Rows with Missing Values:")
print(K)

# Fill missing values in the 'Country' column with a specific value
df["Country"] = df["Country"].fillna("Germany")
print("\nDataFrame After Filling Missing Values in 'Country' Column:")
print(df)

# Merge the DataFrame created from 'data' with the DataFrame created from 'data1'
merged = pd.merge(df, df1, on=['Name', 'Age', 'City', 'Country'])
print("\nMerged DataFrame:")
print(merged)
