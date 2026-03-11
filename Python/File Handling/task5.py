updated_lines = []

with open("students.txt", "r") as file:
    for line in file:
        if line.startswith("Sophie"):
            updated_lines.append("Sophie,23,C\n")
        else:
            updated_lines.append(line)
with open("students.txt", "w") as file:
    file.writelines(updated_lines)

print("Sophie’s age updated successfully.")