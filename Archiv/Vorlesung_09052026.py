students = ["Johannes", "Peter", "Heinz", "Lukas", "Martin", "Uwe"]
studentsWithShortNames = []
for student in students: 
    if len(student) <= 4:
        studentsWithShortNames.append(student)

print(studentsWithShortNames)

