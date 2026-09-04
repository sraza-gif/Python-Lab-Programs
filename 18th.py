import sqlite3


def create_database():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL
        )
    """)

    conn.commit()
    conn.close()


def add_employee():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    try:
        cursor.execute("""
            INSERT INTO employees
            VALUES (?, ?, ?, ?)
        """, (emp_id, name, department, salary))

        conn.commit()
        print("Employee added successfully.")

    except sqlite3.IntegrityError:
        print("Employee ID already exists.")

    conn.close()


def display_report():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    department = input("Enter Department: ")

    cursor.execute("""
        SELECT emp_id, name, salary
        FROM employees
        WHERE department = ?
    """, (department,))

    records = cursor.fetchall()

    if not records:
        print("No employees found in this department.")
    else:
        print("\n===== Department-wise Salary Report =====")
        print("Department:", department)
        print("-" * 45)

        total_salary = 0

        for record in records:
            print("Employee ID:", record[0])
            print("Name      :", record[1])
            print("Salary    :", record[2])
            print("-" * 45)

            total_salary += record[2]

        print("Total Employees:", len(records))
        print("Total Salary   :", total_salary)
        print("Average Salary :", total_salary / len(records))

    conn.close()


def main():
    create_database()

    while True:
        print("\n===== Employee Salary Management =====")
        print("1. Add Employee")
        print("2. Generate Department-wise Salary Report")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            display_report()

        elif choice == "3":
            print("Program terminated.")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
    