import xml.etree.ElementTree as ET

# Read XML file
tree = ET.parse("students.xml")
root = tree.getroot()

# Display student information
for student in root.findall("student"):
    name = student.find("name").text
    roll = student.find("roll").text
    marks = student.find("marks").text

    print("Name:", name)
    print("Roll:", roll)
    print("Marks:", marks)
    print()