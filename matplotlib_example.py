import matplotlib.pyplot as plt
import seaborn as sns

order_values = [250, 180, 90, 320, 150, 450, 220, 80, 275, 410]
order_values_labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# Histogram plot creating
sns.histplot(order_values, bins=5, kde=True)
plt.title("Customer Order Value Distribution")
plt.xlabel("Order Value (AED)")
plt.ylabel("Customer Count")
# plt.show()

# Bar plot creating
sns.barplot(x=order_values_labels, y=order_values)
plt.title("Customer Order Value Distribution")
plt.xlabel("Order Value (AED)")
plt.ylabel("Customer Count")
plt.show()

