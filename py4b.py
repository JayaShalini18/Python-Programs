def reverse_tuple(tuple_value):
    reversed_tuple = tuple_value[::-1]
    return reversed_tuple

# Get user input for the number of elements
num_elements = int(input("Enter the number of elements in the tuple: "))

# Get user input for the values of the elements
elements = []
for i in range(num_elements):
    value = input("Enter the value of element {}: ".format(i + 1))
    elements.append(value)

# Convert the list to a tuple
tuple_value = tuple(elements)

# Call the function to reverse the tuple
reversed_tuple = reverse_tuple(tuple_value)

# Print the original tuple and the reversed tuple
print("Original Tuple:", tuple_value)
print("Reversed Tuple:", reversed_tuple)
