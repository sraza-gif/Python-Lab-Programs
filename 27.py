import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Student examination data
data = {
    "Mathematics": [78, 85, 67, 90, 73, 81, 69, 94, 76, 88],
    "Physics": [72, 88, 70, 92, 75, 79, 68, 90, 74, 85],
    "Chemistry": [75, 82, 65, 88, 78, 83, 72, 92, 79, 86],
    "English": [80, 84, 72, 91, 76, 80, 70, 95, 77, 89]
}

df = pd.DataFrame(data)

# Subject-wise score distributions
for subject in df.columns:
    sns.histplot(df[subject], kde=True)
    plt.title(subject + " Score Distribution")
    plt.show()

# Pairwise relationships
sns.pairplot(df)
plt.show()

# Correlation heatmap
correlation = df.corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Student Score Correlation")
plt.show()