import numpy as np

marks = [78, 85, 92, 67, 88, 73, 95, 81, 76, 89]

temperatures = [28.5, 30.2, 29.8, 31.4, 27.9, 32.1, 30.5]

sales = [12500, 13800, 14200, 11900, 15100, 14750, 16000]


def calculate_statistics(data):
    n = len(data)

    mean = sum(data) / n

    sorted_data = sorted(data)

    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] +
                  sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    variance = sum((x - mean) ** 2 for x in data) / n
    standard_deviation = variance ** 0.5

    minimum = min(data)
    maximum = max(data)

    return mean, median, standard_deviation, minimum, maximum


datasets = {
    "Marks": marks,
    "Temperatures": temperatures,
    "Sales": sales
}

for name, data in datasets.items():

    print("\n", name)

    # Without NumPy
    result = calculate_statistics(data)

    print("Without NumPy:")
    print("Mean:", result[0])
    print("Median:", result[1])
    print("Standard Deviation:", result[2])
    print("Minimum:", result[3])
    print("Maximum:", result[4])

    # With NumPy
    array = np.array(data)

    print("\nWith NumPy:")
    print("Mean:", np.mean(array))
    print("Median:", np.median(array))
    print("Standard Deviation:", np.std(array))
    print("Minimum:", np.min(array))
    print("Maximum:", np.max(array))