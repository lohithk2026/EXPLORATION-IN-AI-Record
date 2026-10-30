
import csv

student = [
    {"Roll no": "101", "Name": "Anitha", "Department": "CSE", "Marks": 99},
    {"Roll no": "102", "Name": "Bala", "Department": "CSE", "Marks": 91},
    {"Roll no": "103", "Name": "Chitra", "Department": "ESE", "Marks": 78}
]

course = ("Python", 4)
print("Course Tuple:", course)

# Write student records to CSV
with open("students.csv", "w", newline="") as file:
    fields = ["Roll no", "Name", "Department", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()

    for stu in student:
        writer.writerow(stu)

print("Records from CSV file:")

# Read student records from CSV
with open("students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(
            row["Roll no"],
            row["Name"],
            row["Department"],
            row["Marks"]
        )
