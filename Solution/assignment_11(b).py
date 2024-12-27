import pandas as pd

# Load the dataset¶
df = pd.read_csv('employees.csv')
df.head(10)

# Replace missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())  # Age
df['Salary'] = df['Salary'].fillna(df['Salary'].median())  # Salary
df.sample(5)

# Drop rows where 'Department' is missing
df = df.dropna(subset=['Department'])
df.sample(5)


# Categorize employees based on salary
def categorize_salary(salary):
    if salary < 50000:
        return 'Low'
    elif 50000 <= salary < 100000:
        return 'Medium'
    else:
        return 'High'


employees = df['Salary_Category'] = df['Salary'].apply(categorize_salary)

print("\nDataset after handling missing values and categorization:")
print(employees)

# Average salary by department
average_salary_by_department = df.groupby('Department')['Salary'].mean()

print("\nAverage salary by department:")
print(average_salary_by_department)
