def is_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False 
    return True


input_str = input("Enter a list of numbers (separated by spaces): ")
num_list = list(map(int, input_str.split()))


if is_ascending(num_list):
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")




