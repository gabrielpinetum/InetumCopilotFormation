import pandas as pd
from random import randint, choice
from datetime import datetime, timedelta

# Lists of realistic first names and last names
first_names = ['John', 'Jane', 'Emily', 'Michael', 'Sarah', 'David', 'Laura', 'Robert', 'Linda', 'James']
last_names = ['Doe', 'Smith', 'Jones', 'Brown', 'Johnson', 'Williams', 'Miller', 'Davis', 'Garcia', 'Rodriguez']

# Generate a list of 50 employees
employees = []
for i in range(50):
    employee = {
        'firstname': choice(first_names),
        'lastname': choice(last_names),
        'age': randint(20, 60),
        'recruitment_date': (datetime.now() - timedelta(days=randint(0, 3650))).strftime('%Y-%m-%d')
    }
    employees.append(employee)

# Convert to pandas DataFrame
df = pd.DataFrame(employees)

# Print the DataFrame
print(df)
