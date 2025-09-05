# Right sided star pattern

# Take input from the user for the number of rows
n = int(input("Enter the number of rows: "))

# Loop through each row
for i in range(n):
    # Print spaces to shift stars to the right, then print stars
    # " " * (n - i - 1): Number of spaces decreases each row
    # "*" * (i + 1): Number of stars increases each row
    print(" " * (n - i - 1) + "*" * (i + 1))

