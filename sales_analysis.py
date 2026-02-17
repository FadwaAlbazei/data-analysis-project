import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales.csv")

# Show first 5 rows
print("First 5 rows:")
print(data.head())

# Show basic statistics
print("\nDataset Info:")
print(data.describe())

# Plot Sales column (make sure your dataset has a column named 'Sales')
if 'Sales' in data.columns:
    data['Sales'].plot(kind='line')
    plt.title("Sales Over Time")
    plt.xlabel("Index")
    plt.ylabel("Sales")
    plt.show()
else:
    print("Column 'Sales' not found in dataset.")
