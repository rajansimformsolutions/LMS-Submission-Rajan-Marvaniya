total_sum = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total_sum += int(line.strip())
print("Sum of numbers from 1 to 1000:", total_sum)