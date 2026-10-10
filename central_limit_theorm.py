import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 1. 1,000 people's height data generate
# np.random.seed(42)
heights = np.random.normal(loc=170, scale=10, size=1000)  # Mean=170, Std=10

# 2. Histogram and Bell Curve plot
count, bins, ignored = plt.hist(heights, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')

# Theoretical Bell Curve line (PDF)
x = np.linspace(130, 210, 200)
p = stats.norm.pdf(x, loc=170, scale=10)
plt.plot(x, p, 'r-', linewidth=2.5, label='Normal Distribution (Bell Curve)')

plt.title("Height Distribution (Mean = 170cm, SD = 10cm)")
plt.xlabel("Height (cm)")
plt.ylabel("Probability Density")
plt.legend()
plt.show()