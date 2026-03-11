with open("students.txt","r") as file:
    content = file.read()

    print("full content :\n")
    print(content)

    print("line by line:\n")

with open("students.txt","r") as file:
    for line in file:
        print(line.strip())
