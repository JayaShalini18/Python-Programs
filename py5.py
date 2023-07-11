def is_subset(set1, set2):
    return set1.issubset(set2)

# Get user input for the first set
set1 = set(input("Enter elements of the first set (space-separated): ").split())

# Get user input for the second set
set2 = set(input("Enter elements of the second set (space-separated): ").split())

# Call the function to check if set1 is a subset of set2
subset_check = is_subset(set1, set2)

# Print the result
if subset_check:
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")
