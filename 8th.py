import numpy as np

midsem = np.array([
    [65, 70, 68, 72],
    [78, 75, 80, 77],
    [55, 60, 58, 62],
    [82, 85, 80, 88],
    [70, 68, 72, 74]
])

endsem = np.array([
    [72, 78, 75, 80],
    [84, 82, 86, 83],
    [65, 68, 66, 70],
    [88, 90, 85, 92],
    [78, 75, 80, 82]
])

students = ["S1", "S2", "S3", "S4", "S5"]

mid_total = np.sum(midsem, axis=1)
end_total = np.sum(endsem, axis=1)

mid_average = np.mean(midsem, axis=1)
end_average = np.mean(endsem, axis=1)

percentage_improvement = ((end_total - mid_total) / mid_total) * 100

print("Student  Mid Total  End Total  Mid Average  End Average  Improvement")

for i in range(len(students)):
    print(
        students[i],
        mid_total[i],
        end_total[i],
        round(mid_average[i], 2),
        round(end_average[i], 2),
        round(percentage_improvement[i], 2), "%"
    )