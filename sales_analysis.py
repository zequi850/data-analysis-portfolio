import pandas as pd

# Sample sales dataset
sales_data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer"],
    "Units_Sold": [120, 450, 300, 150, 80],
    "Unit_Price": [800, 25, 50, 250, 150]
}

df = pd.DataFrame(sales_data)

# Calculate revenue
df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]

# Summary statistics
total_revenue = df["Revenue"].sum()
best_selling_product = df.loc[df["Revenue"].idxmax(), "Product"]

print("Sales Analysis Report")
print(df)
print("\nTotal Revenue:", total_revenue)
print("Top Revenue Product:", best_selling_product)