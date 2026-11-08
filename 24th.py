import pandas as pd

# Create dataset
data = {
    "Name": ["Rahul", "Amit", "Priya", "Rahul", None],
    "Age": [20, 21, None, 20, 22],
    "Marks": [85, 90, 75, 85, None]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Handle missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nCleaned Dataset:")
print(df)

# Display information
print("\nDataset Information:")
print(df.info())