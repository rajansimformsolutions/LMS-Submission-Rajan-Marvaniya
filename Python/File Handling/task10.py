import os

confirm = input("Are you sure you want to delete students_backup.txt? (yes/no): ")

if confirm.lower() == "yes":
    if os.path.exists("student_backup.txt"):
        os.remove("student_backup.txt")
        print("File deleted successfully.")
    else:
        print("File does not exist.")
else:
    print("File deletion cancelled.")