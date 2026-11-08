import xml.etree.ElementTree as ET

# Create root element
root = ET.Element("students")

# Add student
student = ET.SubElement(root, "student")

ET.SubElement(student, "name").text = "Rahul"
ET.SubElement(student, "roll").text = "101"
ET.SubElement(student, "marks").text = "85"

# Modify student marks
student.find("marks").text = "95"

# Create XML tree
tree = ET.ElementTree(root)

# Save XML file
tree.write("students.xml")

print("XML file created successfully!")

# Display modified data
print(ET.tostring(root, encoding="unicode"))