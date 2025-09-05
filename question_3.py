import numpy as np

# Create a 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, size=(5, 5))

# Print the matrix in grid format
print("Original Matrix:")
for row in matrix:
    print(' '.join(f"{num:3d}" for num in row))

# Calculate statistics
max_val = matrix.max()
min_val = matrix.min()
mean_val = matrix.mean()

print(f"\nMaximum: {max_val}")
print(f"Minimum: {min_val}")
print(f"Mean: {mean_val:.2f}")

# Normalize the matrix between 0 and 1
normalized_matrix = (matrix - min_val) / (max_val - min_val)
print("\nNormalized Matrix:")
for row in normalized_matrix:
    print(' '.join(f"{num:0.2f}" for num in row))

# Flatten and sort the matrix
flattened = matrix.flatten()
sorted_flattened = np.sort(flattened)
print("\nFlattened and Sorted Array:")
print(sorted_flattened)
