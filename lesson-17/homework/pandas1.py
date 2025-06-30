Homework 1:

import pandas as pd

data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 'Age': [25, 30, 35, 40], 'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']} df = pd.DataFrame(data)

1. Rename column names using function. "First Name" --> "first_name", "Age" --> "age

def to_clean(val):
    return val.strip().lower().replace(" ", "_")

df.rename(columns=to_clean, inplace=True)
print(df)

2. Print the first 3 rows of the DataFrame

print(df.head(3))

3. Find the mean age of the individuals

print(df.age.mean())

4. Select and print only the 'Name' and 'City' columns

print(df[['first_name','city']])

5. Add a new column 'Salary' with random salary values

import numpy as np
df['Salary'] = np.random.randint(50000, 100000, len(df))
print(df)

6. Display summary statistics of the DataFrame

df.describe()

Homework 2:

1. Create a DataFrame named sales_and_expenses with columns 'Month', 'Sales', and 'Expenses', representing monthly sales and expenses data. Use below table.
Month	Sales	Expenses
Jan	5000	3000
Feb	6000	3500
Mar	7500	4000
Apr	8000	4500

data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr'], 'Sales': [5000, 6000, 7500, 8000],  'Expenses':[3000, 3500, 4000, 4500]}
sales_and_expenses = pd.DataFrame(data)
print(sales_and_expenses)


2. Calculate and display the maximum sales and expenses.

print(sales_and_expenses.Sales.max(), sales_and_expenses.Expenses.max())

3. Calculate and display the minimum sales and expenses.

print(sales_and_expenses.Sales.min(), sales_and_expenses.Expenses.min())

4. Calculate and display the average sales and expenses.

print(sales_and_expenses.Sales.mean(), sales_and_expenses.Expenses.mean())

Homework 3:

1. Create a DataFrame named expenses with columns 'Category', 'January', 'February', 'March', and 'April', representing monthly expenses for different categories. Use below table.
Category	January	February	March	April
Rent	1200	1300	1400	1500
Utilities	200	220	240	250
Groceries	300	320	330	350
Entertainment	150	160	170	180


  data = {'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],  'January': [1200, 200, 300, 150], 'February': [1300, 220, 320, 160], 'March': [1400, 240, 330, 170], 'April': [1500, 250, 350, 180]}
expenses = pd.DataFrame(data)
print(expenses)

2. Calculate and display the maximum expense for each category.

expenses = expenses.set_index('Category')
print("Max per category:\n", expenses.max(axis=1))
                                            
3. Calculate and display the minimum expense for each category.
  
print("Min per category:\n", expenses.min(axis=1))
                                            
4. Calculate and display the average expense for each category.

print('Average per category:\n', expenses.mean(axis=1))



                                            
In this task, use .set_index method to make Category column as index.

Try this code, learn it and use it in the task.

expenses.set_index('Category')
