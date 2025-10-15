import pandas as pd

# Step 1: Read CSV files into DataFrames
employees = pd.read_csv('employees.csv')
departments = pd.read_csv('departments.csv')

# Step 2: Perform JOIN on DID
merged_df = pd.merge(employees, departments, on='DID', how='inner')

# Step 3: Group by DName and calculate average salary
avg_salary_by_dept = merged_df.groupby('DName')['Salary'].mean()

# Step 4: Display the result
print("Average Salary per Department:\n")
for dname, avg_salary in avg_salary_by_dept.items():
    print(f"{dname}: ₹{avg_salary:.2f}")
