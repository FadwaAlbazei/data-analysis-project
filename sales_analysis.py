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

# Convert Date column to datetime
if 'Date' in data.columns:
    data['Date'] = pd.to_datetime(data['Date'])
    data.set_index('Date', inplace=True)

    # Monthly sales summary
    monthly_sales = data['Sales'].resample('M').sum()
    print("\nMonthly Sales Summary:")
    print(monthly_sales)

    # Plot monthly sales
    monthly_sales.plot(kind='bar')
    plt.title("Monthly Sales")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.show()
