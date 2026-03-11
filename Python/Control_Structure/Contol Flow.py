

users = {
    "trainer1": "train@123",
    "trainer2": "train@234"
}

max_attempts = 3
attempt = 0
login_success = False

while attempt < max_attempts:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful\n")
        login_success = True
        break
    else:
        attempt += 1
        print("Invalid credentials.")

        if attempt == max_attempts:
            print("Access denied. Please contact admin.")

if not login_success:
    exit()



trainees = []

for i in range(3):
    print("\nEnter details for trainee", i + 1)
    name = input("Enter name: ")
    python_marks = int(input("Python marks: "))
    ds_marks = int(input("Data Structure marks: "))
    cf_marks = int(input("Control Flow marks: "))

    trainee = {
        "Name": name,
        "Python": python_marks,
        "Data Structures": ds_marks,
        "Control Flow": cf_marks
    }

    trainees.append(trainee)




grade_count = {}

for t in trainees:
    total = t["Python"] + t["Data Structures"] + t["Control Flow"]
    average = total / 3
    t["Average"] = average

    if average >= 85:
        t["Grade"] = "Excellent"
    elif average >= 70:
        t["Grade"] = "Good"
    elif average >= 50:
        t["Grade"] = "Average"
    else:
        t["Grade"] = "Needs Improvement"

   
    grade = t["Grade"]
    if grade in grade_count:
        grade_count[grade] += 1
    else:
        grade_count[grade] = 1



print("\n--- Trainee Results ---")
for t in trainees:
    print("\nName:", t["Name"])
    print("Average:", t["Average"])
    print("Grade:", t["Grade"])




highest = max(trainees, key=lambda x: x["Average"])
lowest = min(trainees, key=lambda x: x["Average"])

print("\nHighest Scorer:", highest["Name"])
print("Lowest Scorer:", lowest["Name"])



print("\nTrainee Count per Grade:")
for grade, count in grade_count.items():
    print(grade, ":", count)




print("\nTrainees who failed any subject:")
for t in trainees:
    if (t["Python"] < 40 or
        t["Data Structures"] < 40 or
        t["Control Flow"] < 40):
        print(t["Name"])




decision = input("\nDo you want to schedule remedial training? (yes/no): ").strip().lower()

if decision == "yes":
    print("\nTrainees needing remedial training:")

    remedial_list = [
        t["Name"] for t in trainees
        if (t["Python"] < 40 or
            t["Data Structures"] < 40 or
            t["Control Flow"] < 40)
    ]

    if remedial_list:
        for trainee in remedial_list:
            print("-", trainee)
    else:
        print("No trainees require remedial training.")

elif decision == "no":
    print("Report finalized successfully")

else:
    print("Invalid input. Please enter 'yes' or 'no'.")