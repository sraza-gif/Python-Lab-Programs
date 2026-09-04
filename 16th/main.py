from database import create_table
from operations import (
    insert_student,
    display_students,
    search_student,
    update_student,
    delete_student
)


def main():

    # Create database table
    create_table()

    while True:

        print("\n===================================")
        print(" STUDENT INFORMATION MANAGEMENT")
        print("===================================")
        print("1. Insert Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("===================================")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            insert_student()

        elif choice == 2:
            display_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_student()

        elif choice == 5:
            delete_student()

        elif choice == 6:
            print("\nThank you!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()