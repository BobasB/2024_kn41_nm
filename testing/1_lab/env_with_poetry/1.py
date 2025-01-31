import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [90, 85, 88]
    }
df = pd.DataFrame(data)

# Perform a basic operation
average_age = df["Age"].mean()
max_score = df["Score"].max()

# Print results
print("DataFrame:")
print(df)
print("\nAverage Age:", average_age)
print("Max Score:", max_score)
