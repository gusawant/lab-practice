# assignment 13
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset (for demonstration, we'll use a sample dataset)
df = pd.DataFrame({
    'Year': [2015, 2016, 2017, 2018, 2019],
    'Revenue': [50, 55, 60, 65, 70],
    'Salary': [30000, 35000, 40000, 45000, 50000],
    'Experience': [1, 2, 3, 4, 5]
})

# Line chart (Revenue over years)
plt.plot(df['Year'], df['Revenue'], marker='o')
plt.title("Company Revenue Over Years")
plt.xlabel("Year")
plt.ylabel("Revenue")
plt.show()

# Scatter plot (Salary vs Experience)
plt.scatter(df['Experience'], df['Salary'])
plt.title("Salary vs Experience")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# Heatmap (Correlation matrix)
sns.heatmap(df.corr(), annot=True)
plt.title("Correlation Matrix")
plt.show()
