# Basic example of using NumPy arrays
import numpy as np

# Create a NumPy array with three elements
num = np.array([100, 200, 300])
# print(num)
# print(num[2])

# Multi-dimensional NumPy array
multi_num = np.array([[1, 2, 3], [4, 5, 6]])

# print the multi-dimensional array
# print(multi_num)

# Accessing a specific element of the multi-dimensional array
# print(multi_num[1, 1]) #expected output: 5

# Slicing a NumPy array
# print(multi_num[0:1]) #expected output: [[1 2 3]]

# Accessing a specific column of the multi-dimensional array
# print(multi_num[:, 1]) #expected output: [2 5]

b = np.array([[7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# print(b[-2])

# Add two NumPy arrays
sum_array = multi_num + b[:2]
print(sum_array)

# Transpose the multi-dimensional array
c = np.transpose(multi_num)
print(c)


cc = multi_num.T
print(cc)

# Matrix operations with NumPy
# Matrices are just 2-D arrays
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix addition
C = A + B

print("Matrix C:")
print(C)

# Matrix multiplication
D = np.dot(A, B)
print("Matrix D:")
print(D)


# Matrix Multiplication
X = np.array([[1,2,3],[4,5,6],[7,8,9]])
Y = np.array([[10,11,12],[13,14,15],[16,17,18]])

Z = np.dot(X, Y)
print("Matrix Z:")
print(Z)

# Matrix Multiplication
M = np.array([[1,2,3],[4,5,6],[7,8,9]])
N = np.array([[10,11,12],[13,14,15],[16,17,18], [19,20,21]])

O = np.dot(M, N.T)
print("\n\nMatrix O (from M and N):")
print(O)


# variance and standard deviation
data = np.array([10, 20, 30, 40, 50])
variance = np.var(data)
standard_deviation = np.std(data)
print("\n\nVariance and Standard Deviation of the data:")
print("Variance:", variance)
print("Standard Deviation:", standard_deviation)

# Mode (most frequent value) — NumPy has no np.mode(); use unique + counts
data = np.array([10, 20, 30, 40, 50, 20, 30, 40, 50])
values, counts = np.unique(data, return_counts=True)
mode = values[np.argmax(counts)]
print("\n\nMode of the data:")
print("Mode:", mode)

# Mean (average)
data = np.array([10, 20, 30, 40, 50])
mean = np.mean(data)
print("\n\nMean of the data:")
print("Mean:", mean)


# Median (middle value)
data = np.array([10, 20, 30, 40, 50])
median = np.median(data)
print("\n\nMedian of the data:")
print("Median:", median)

# Range (difference between max and min) — don't name it `range` (built-in function)
data = np.array([10, 20, 30, 40, 50])
data_range = np.max(data) - np.min(data)
print("\n\nRange of the data:")
print("Range:", data_range)

# Quartiles (25%, 50%, 75%)
data = np.array([10, 20, 30, 40, 50])
quartiles = np.percentile(data, [25, 50, 75])
print("Quartiles of the data:")
print("Quartiles:", quartiles)

# Percentiles (any percentile)
data = np.array([10, 20, 30, 40, 50])
percentile = np.percentile(data, 90)
print("90th Percentile of the data:")
print("90th Percentile:", percentile)


# Number pyramid: row i shows 1 2 ... i
paramid = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("\n\nNumber pyramid:")
for i in paramid:
    row = np.arange(1, i + 1)  # numbers from 1 up to i

    print(" ".join(map(str, row)))

# Print numbers in rows (3 per line): 1 2 3 / 4 5 6 / ...
square = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16,17, 18])
print("\n\nNumbers in rows (3 per line):")
grid = square.reshape(-1, 9)  # -1 rows as many as needed, 9 columns // 3 rows, 9 columns // 2 rows, 9 columns
for row in grid:
    print(" ".join(map(str, row)))
    


# Star grid: same idea as above, but print * instead of numbers (3 per row)
print("\n\nStar grid:")
cols = 9
total_stars = 18
stars = np.full(total_stars, "*")  # array of twelve "*"
star_grid = stars.reshape(-1, cols)
for row in star_grid:
    print(" ".join(row))

# Star pyramid: row i has i stars
for i in range(1, 9): # 1 to 8 stars in each row
    print(" ".join(np.full(i, "@")))

