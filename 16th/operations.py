from database import connect_database


def insert_student():
    roll_no = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    cgpa = float(input("Enter CGPA: "))

    connection = connect_database()
    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO students
            (roll_no, name, department, cgpa)
            VALUES (?, ?, ?, ?)
        """, (roll_no, name, department, cgpa))

        connection.commit()
        print("\nStudent record inserted successfully.")

    except Exception as e:
        print("\nError:", e)

    finally:
        connection.close()


def display_students():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    if len(students) == 0:
        print("\nNo student records found.")
    else:
        print("\n---------- Student Records ----------")

        for student in students:
            print("Roll Number :", student[0])
            print("Name        :", student[1])
            print("Department  :", student[2])
            print("CGPA        :", student[3])
            print("-------------------------------------")

    connection.close()


def search_student():
    roll_no = int(input("Enter Roll Number to search: "))

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found")
        print("Roll Number :", student[0])
        print("Name        :", student[1])
        print("Department  :", student[2])
        print("CGPA        :", student[3])
    else:
        print("\nStudent record not found.")

    connection.close()


def update_student():
    roll_no = int(input("Enter Roll Number to update: "))

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    if student:
        print("\nEnter new details:")

        name = input("Enter Student Name: ")
        department = input("Enter Department: ")
        cgpa = float(input("Enter CGPA: "))

        cursor.execute("""
            UPDATE students
            SET name = ?, department = ?, cgpa = ?
            WHERE roll_no = ?
        """, (name, department, cgpa, roll_no))

        connection.commit()

        print("\nStudent record updated successfully.")

    else:
        print("\nStudent record not found.")

    connection.close()


def delete_student():
    roll_no = int(input("Enter Roll Number to delete: "))

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll_no,)
    )

    student = cursor.fetchone()

    if student:
        cursor.execute(
            "DELETE FROM students WHERE roll_no = ?",
            (roll_no,)
        )

        connection.commit()

        print("\nStudent record deleted successfully.")

    else:
        print("\nStudent record not found.")

    connection.close()