def can_obtain_from_first(first, second):
    i = 0
    j = 0

    while i < len(first) and j < len(second):
        if first[i] == second[j]:
            i += 1
            j += 1
        else:
            i += 1

    if j == len(second):
        return "YES"
    elif i == len(first):
        return "NO"
    else:
        return "YES"

first_string = "abcdef"
second_string = "acef"
print(can_obtain_from_first(first_string, second_string))  
