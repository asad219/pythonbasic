import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Sales (K AED) by department and quarter
sales_df = pd.DataFrame(
    {
        "Department": ["Sales"] * 4 + ["Engineering"] * 4 + ["Marketing"] * 4,
        "Quarter": ["Q1", "Q2", "Q3", "Q4"] * 3,
        "Sales_K": [
            520, 580, 610, 640,
            410, 435, 450, 470,
            590, 620, 655, 680,
        ],
    }
)

heatmap_data = sales_df.pivot(index="Department", columns="Quarter", values="Sales_K")

print("Heatmap data (Department × Quarter, sales in K AED):")
print(heatmap_data)

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".0f",
    cmap="YlOrRd",
    linewidths=0.5,
    cbar_kws={"label": "Sales (K AED)"},
)
plt.title("Quarterly Sales by Department")
plt.xlabel("Quarter")
plt.ylabel("Department")
plt.tight_layout()
plt.show()
