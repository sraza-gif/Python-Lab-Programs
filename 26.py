import matplotlib.pyplot as plt

# Student data
students = ["S1", "S2", "S3", "S4", "S5",
            "S6", "S7", "S8", "S9", "S10"]

hours = [8, 10, 12, 15, 18, 20, 7, 14, 16, 22]

scores = [65, 72, 75, 82, 88, 90, 60, 80, 85, 95]

# Histogram of study hours
plt.hist(hours, bins=5, edgecolor='black')
plt.title("Distribution of Study Hours")
plt.xlabel("Study Hours per Week")
plt.ylabel("Number of Students")
plt.show()

# Scatter plot
plt.scatter(hours, scores)
plt.title("Study Hours vs Exam Scores")
plt.xlabel("Study Hours per Week")
plt.ylabel("Exam Score")
plt.grid()
plt.show()