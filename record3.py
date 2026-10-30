student={}
def add_student():
    roll=input("Enter Roll No:" )
    name=input("Enter the name")
    dept=input("Enter the Departmant ")
    student[roll]={"Name":name,"Department":dept}
def view_students():
    if not student:
        print("No Stuent record found")
        print("\n--Student Records--")
    for roll,data in student.items():
        print("Roll No:",roll,"Name:",data["Name"],"|Department :",data["Department"])
def search_student():
    roll=input("Enter the Roll no:")

    if roll in student:
        print(student[roll])
    else:
        print("Student not found")
def delete_student():
    roll=int(input("Enter the roll "))

    if roll in student:
        del student[roll]
        print("Student data not found")
    else:
        print("Student data not found")
while True:
    print("\n 1 Add Studnet ")
    print(" 2.View Studnet")
    print("3. Search Student ")
    print("4. Delete Student ")
    print("5.Exit")

    choise=input("Enter your Choise")

    if choise=="1":
        add_student
    elif choise=="2":
        view_students
    elif choise=="3":
        search_student
    elif choise=="4":
        delete_student
    elif choise=="5":
        print("Exiting")
        break
    else:
        print("Invalid choise")