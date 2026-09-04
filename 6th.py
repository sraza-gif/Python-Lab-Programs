# Program to read student marks from a file

input_file = open("students.txt", "r")
output_file = open("results.txt", "w")

for line in input_file:
    data = line.split()

    roll = data[0]
    name = data[1]

    marks = []
    for i in range(2, len(data)):
        marks.append(float(data[i]))

    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    result = (
        "Roll: " + roll +
        ", Name: " + name +
        ", Total: " + str(total) +
        ", Average: " + str(round(average, 2)) +
        ", Grade: " + grade + "\n"
    )

    print(result)
    output_file.write(result)

input_file.close()
output_file.close()

print("Results written to results.txt")