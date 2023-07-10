student_details = {}


name = input("Enter the name: ")


age = int(input("Enter the age: "))
if age < 0:
    print("Age should be positive. Skipping details...")
else:
    
    marks = []
    for i in range(6):
        subject_marks = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(subject_marks)

    
    student_details["Name"] = name
    student_details["Age"] = age
    student_details["Marks"] = marks

print("Student Details:", student_details)
