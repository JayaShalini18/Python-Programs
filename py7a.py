numbers = input("Enter the list of numbers (separated by spaces): ").split()


numbers = [int(x) for x in numbers]

try:
    
    index = int(input("Enter the index: "))
    
    
    element = numbers[index]
    print("Element at index", index, ":", element)

except IndexError:
    print("Error: Index is out of range")
