import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Monthly sales and marketing metrics (AED thousands)
sales_ad_df = pd.DataFrame(
    {
        "Advertising": [45, 52, 48, 61, 58, 72, 68, 75, 70, 82, 78, 88],
        "Sales": [320, 335, 328, 360, 355, 390, 385, 410, 398, 425, 418, 440],
        "Promo_Discount": [5, 6, 5, 8, 7, 9, 8, 10, 9, 11, 10, 12],
        "Website_Visits": [12, 13, 12, 15, 14, 17, 16, 18, 17, 19, 18, 20],
    }
)

# 1. Terminal par data and correlation check
print("Sales & Advertising Data:")
print(sales_ad_df)

corr = sales_ad_df.corr()
print("\nCorrelation Matrix:")
print(corr.round(3))

# 2. Specific Columns (Advertising vs Sales) ka Dotted Scatter Plot
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=sales_ad_df,
    x="Advertising",
    y="Sales",
    s=120,            # Dot  size
    color="#1f77b4",  # Blue color
    edgecolor="black" # Dot border color
)

plt.title("Advertising Spend vs Sales (Dotted Scatter Plot)")
plt.xlabel("Advertising Spend (K AED)")
plt.ylabel("Sales (K AED)")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()

# # 3. All columns complete Dotted Grid (Pairplot)
# sns.pairplot(sales_ad_df, diag_kind="kde", plot_kws={"color": "#1f77b4", "s": 60})
# plt.suptitle("Pairwise Dotted Scatter Plot of All Metrics", y=1.02)
# plt.show()