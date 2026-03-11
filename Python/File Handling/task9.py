with open("students.txt","r") as source:
    content = source.read()

with open("student_backup.txt", "w") as backup:
    backup.write(content)

print("file copied successfully.")    