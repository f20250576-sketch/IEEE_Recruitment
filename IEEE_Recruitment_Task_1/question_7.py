list1 = [3, 8, 5, 1, 4, 6, 9, 7, 7]  # Define the first list with some duplicate values
list2 = [10, 8, 11, 9, 9, 4, 6, 3]   # Define the second list, also with possible duplicates

# Find intersection without duplicates
intersection = list(set(list1) & set(list2))  
# set(list1) and set(list2) convert the lists to sets, removing duplicates
# The & operator finds common elements between the two sets (set intersection)
# Wrapping with list() converts the result back to a list

print("Intersection:", intersection)  # Output the intersection list