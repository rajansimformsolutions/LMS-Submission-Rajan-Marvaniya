# Task 4: Count Total Students and Grade 'A'

total_students = 0
grade_a_count = 0

with open("students.txt", "r") as file:
    next(file)  # Skip header
    for line in file:
        if line.strip():
                total_students += 1
                data = line.strip().split(",")
                if data[2] == "A":
                    grade_a_count += 1
       
    
print("Total Students:", total_students)
print("Students with Grade 'A':", grade_a_count)