import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Different dataset: monthly sales (K AED) by department
sales_df = pd.DataFrame(
    {
        "Department": (
            ["Sales"] * 10
            + ["Engineering"] * 10
            + ["Marketing"] * 10
        ),
        "Monthly_Sales_K": [
            42, 55, 48, 61, 53, 47, 58, 50, 44, 52,
            38, 41, 45, 39, 43, 40, 46, 37, 42, 44,
            50, 62, 58, 65, 54, 59, 61, 57, 63, 56,
        ],
    }
)

print("Sample DataFrame:")
print(sales_df.head())
print("\nSummary by department:")
print(sales_df.groupby("Department")["Monthly_Sales_K"].describe())

sns.boxplot(data=sales_df, x="Department", y="Monthly_Sales_K", hue="Department", legend=False)
plt.title("Monthly Sales Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Monthly sales (K AED)")
plt.tight_layout()
plt.show()
