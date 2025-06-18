import pandas as pd
import random

names = ["Alice","Bob","Charlie","Diana","Ethan","Fiona","George","Hannah",
         "Ian","Jade","Karl","Laura","Mike","Nina","Oliver","Paula","Quinn","Rachel","Steve","Tina"]
fields = ["Engineering","Data Science","Computer Science","Business","Art","Biology","Mathematics","Design"]

data = []
for name in names:
    field = random.choice(fields)
    gpa = round(random.uniform(2.5, 4.0), 2)
    salary = random.randint(50000, 120000)
    funding = random.randint(10000, 50000)
    data.append({
        "name": name,
        "field": field,
        "gpa": gpa,
        "expected_salary": salary,
        "funding_needed": funding
    })

df = pd.DataFrame(data)
df.to_csv("data/students.csv", index=False)
print("✅ Generated data/students.csv with 20 random student profiles.")
