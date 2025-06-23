import pandas as pd
import random
import numpy as np

# Constants
countries = ["Romania", "Ukraine"]
fields = ["Computer Science", "Data Science", "Business Analytics", "IT"]
universities = ["TU München", "TU Berlin", "TU Darmstadt", "TU Aachen"]
degrees = ["Bachelors", "Masters"]
industries = ["Consulting", "Tech", "Automobile", "Industry", "Startup", "Finance", "Manufacturing", "Academia", "Non-profit", "Government"]

# Generate synthetic data
data = []
for i in range(500):
    student_id = f"TVSTU{i+1:04d}"  # e.g. TVSTU0001
    status = random.choices(["studying", "working", "dropout"], weights=[0.6, 0.3, 0.1])[0]
    program_duration = random.choice([36, 48, 60])  # in months
    progress = round(random.uniform(0.0, 1.0 if status != "dropout" else random.uniform(0.0, 0.6)), 2)
    gpa = round(random.normalvariate(3.0, 0.4), 2)
    gpa = min(max(gpa, 1.5), 4.0)
    field = random.choice(fields)
    university = random.choice(universities)
    degree = random.choice(degrees)
    internships = random.randint(0, 4)
    internship_quality = min(5, max(1, int(gpa * 1.25) + random.choice([-1, 0, 1])))
    work_while_studying = random.choice(["yes", "no"])
    extracurricular = random.choice(["yes", "no"])
    country = random.choice(countries)
    german_skills = random.randint(1, 5 if country == "Romania" else 4)
    age = random.randint(20, 32)
    debt_taken = random.randint(0, 20000)
    prof_score = random.randint(1, 5)
    talentvest_score = random.randint(1, 5)
    target_industry = random.choice(industries)
    relocation = random.choice(["yes", "no"])
    motivation = random.randint(1, 5)

    # Salary and salary growth logic
    base_salary = int(gpa * 10000 + internship_quality * 2000 + random.randint(-3000, 3000))
    base_salary = max(base_salary, 20000)
    salary_growth = round(random.uniform(0.02, 0.06), 3)

    # Discount rate logic
    risk_score = (6 - prof_score + 6 - talentvest_score + (5 - motivation)) / 3
    discount_rate = round(min(max(0.06 + risk_score * 0.02, 0.06), 0.15), 3)

    data.append({
        "student_id": student_id,
        "status": status,
        "program_duration_months": program_duration,
        "program_progress": progress,
        "gpa": gpa,
        "field": field,
        "university": university,
        "degree": degree,
        "internship_count": internships,
        "internship_quality": internship_quality,
        "work_while_studying": work_while_studying,
        "extracurricular_activities": extracurricular,
        "country": country,
        "german_skills": german_skills,
        "age": age,
        "debt_taken": debt_taken,
        "professor_score": prof_score,
        "talentvest_score": talentvest_score,
        "target_industry": target_industry,
        "willing_to_relocate": relocation,
        "predicted_salary": base_salary,
        "salary_growth": salary_growth,
        "discount_rate": discount_rate,
        "motivation_score": motivation
    })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("data/simulated_student_ISA_dataset.csv", index=False)
print("✅ Generated data/simulated_student_ISA_dataset.csv with 500 student profiles.")
