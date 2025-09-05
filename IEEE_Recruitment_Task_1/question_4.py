import numpy as np

# Create a 5x5 matrix
matrix = np.arange(1, 26).reshape(5, 5)
print("Original 5x5 matrix:")
print(matrix)

# Extract the middle 3x3 matrix
middle_matrix = matrix[1:4, 1:4]
print("\nMiddle 3x3 matrix:")
print(middle_matrix)

# Extract first row and last column of the 3x3 matrix
first_row = middle_matrix[0, :]
last_col = middle_matrix[:, -1]

print("\nFirst row of 3x3 matrix:", first_row)
print("Last column of 3x3 matrix:", last_col)

# Compute and print the dot product
dot_product = np.dot(first_row, last_col)
print("\nDot product:", dot_product)