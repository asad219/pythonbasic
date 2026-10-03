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
print("Matrix O (from M and N):")
print(O)
