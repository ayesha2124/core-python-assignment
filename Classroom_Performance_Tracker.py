def calculate_average(marks):
    marks = list(map(int, marks))
    total = sum(marks)
    average = total / len(marks)
    return round(average)


students = {}
n = int(input("How many students do you want to add? "))

for _ in range(n):
    name = input("Enter student name: ")
    marks = input(f"Enter marks for {name} (separate numbers by commas): ").split(",")
    average = calculate_average(marks)
    students[name] = average

top_student = max(students, key=students.get)

print("Average Marks:", students)
print(f"Top Performer: {top_student}")
