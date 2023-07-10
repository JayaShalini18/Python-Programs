def find_number():
    n = int(input("Enter the number of elements in the list: "))
    numbers = []
    positive_indices = []
    negative_indices = []

    for i in range(n):
        num = int(input(f"Enter element {i + 1}: "))
        numbers.append(num)

    target = int(input("Enter the number to search: "))

    for i in range(len(numbers)):
        if numbers[i] == target:
            positive_indices.append(i)
            negative_indices.append(i - len(numbers))

    if positive_indices:
        print(f"The number {target} is present in the list.")
        print(f"Positive indices: {positive_indices}")
        print(f"Negative indices: {negative_indices}")
        print(f"Number of occurrences: {len(positive_indices)}")
    else:
        print(f"The number {target} is not present in the list.")


find_number()

