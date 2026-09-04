# Program to analyse student course enrolments using sets and tuples

# Tuples to store student details
student1 = (101, "Rahul", "CSE")
student2 = (102, "Priya", "CSE")

# Sets to store courses
courses_student1 = {"Python", "DBMS", "Mathematics", "Data Structures"}
courses_student2 = {"Python", "DBMS", "Operating Systems", "Computer Networks"}

print("Student 1 Details:", student1)
print("Student 2 Details:", student2)

print("\nStudent 1 Courses:", courses_student1)
print("Student 2 Courses:", courses_student2)

# Union
union_courses = courses_student1.union(courses_student2)
print("\nUnion of courses:")
print(union_courses)

# Intersection
common_courses = courses_student1.intersection(courses_student2)
print("\nCommon courses:")
print(common_courses)

# Difference
unique_student1 = courses_student1.difference(courses_student2)
print("\nCourses unique to Student 1:")
print(unique_student1)

unique_student2 = courses_student2.difference(courses_student1)
print("\nCourses unique to Student 2:")
print(unique_student2)