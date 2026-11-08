import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

sales = [45000, 52000, 48000, 61000, 58000, 65000,
         62000, 70000, 68000, 75000, 72000, 80000]

# Find highest and lowest sales
highest = max(sales)
lowest = min(sales)

high_month = months[sales.index(highest)]
low_month = months[sales.index(lowest)]

# Line chart
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Revenue - Line Chart")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid()
plt.show()

# Bar chart
plt.figure(figsize=(10, 5))
plt.bar(months, sales)
plt.title("Monthly Sales Revenue - Bar Chart")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.show()

# Display highest and lowest sales
print("Highest Sales:", high_month, highest)
print("Lowest Sales:", low_month, lowest)