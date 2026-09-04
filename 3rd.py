# Program to manage student records using lists and dictionaries

students = []

while True:
    print("\n--- Student Record Management ---")
    print("1. Insert Student")
    print("2. Delete Student")
    print("3. Search Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Insert student
    if choice == 1:
        roll = int(input("Enter roll number: "))
        name = input("Enter student name: ")
        department = input("Enter department: ")
        cgpa = float(input("Enter CGPA: "))

        student = {
            "roll": roll,
            "name": name,
            "department": department,
            "cgpa": cgpa
        }

        students.append(student)
        print("Student record inserted successfully.")

    # Delete student
    elif choice == 2:
        roll = int(input("Enter roll number to delete: "))
        found = False

        for student in students:
            if student["roll"] == roll:
                students.remove(student)
                found = True
                print("Student record deleted successfully.")
                break

        if not found:
            print("Student record not found.")

    # Search student
    elif choice == 3:
        roll = int(input("Enter roll number to search: "))
        found = False

        for student in students:
            if student["roll"] == roll:
                print("\nStudent Found:")
                print("Roll Number:", student["roll"])
                print("Name:", student["name"])
                print("Department:", student["department"])
                print("CGPA:", student["cgpa"])
                found = True
                break

        if not found:
            print("Student record not found.")

    # Display all students
    elif choice == 4:
        if len(students) == 0:
            print("No student records available.")
        else:
            print("\n--- All Student Records ---")

            for student in students:
                print("Roll Number:", student["roll"])
                print("Name:", student["name"])
                print("Department:", student["department"])
                print("CGPA:", student["cgpa"])
                print("-------------------------")

    # Exit
    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice. Please try again.")