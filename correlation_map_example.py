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

print("Sales & advertising data:")
print(sales_ad_df)

corr = sales_ad_df.corr()
print("\nCorrelation matrix:")
print(corr.round(3))

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    center=0,
    linewidths=0.5,
    square=True,
    cbar_kws={"label": "Pearson correlation"},
)
plt.title("Correlation Map: Sales vs Advertising (and related metrics)")
plt.tight_layout()
plt.show()
