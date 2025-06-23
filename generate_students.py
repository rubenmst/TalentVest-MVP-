import pandas as pd
import random

# Constants
names = [
    "Alice Popescu", "Bogdan Ionescu", "Carla Nowak", "Dimitri Petrov", "Elena Novak",
    "Filip Ivanov", "Greta Kolar", "Hristo Dimitrov", "Ivana Horvat", "Jakub Kowalski",
    "Katerina Ilieva", "Luka Jankovic", "Mira Vasileva", "Nina Dragomir", "Oleg Romanov",
    "Petra Novak", "Radek Zelenka", "Stefan Marinov", "Tereza Blazek", "Vlad Stanescu"
]
countries = ["Romania", "Ukraine"]
fields = ["Computer Science", "Data Science", "Business Analytics", "IT"]
universities = ["TU München", "TU Berlin", "TU Darmstadt", "TU Aachen"]
degrees = ["Bachelors", "Masters"]
industries = ["Consulting", "Tech", "Automobile", "Industry", "Startup", "Finance", "Manufacturing", "Academia", "Non-profit", "Government"]

# Generate synthetic student data
data = []
for i, name in enumerate(names):
    student_id = f"TVSTU{i+1:04d}"
    country = random.choice(countries)
    field = random.choice(fields)
    university = random.choice(universities)
    degree = random.choice(degrees)
    program_duration = random.choice([36, 48, 60])
    program_progress = 0.0  # Not started yet
    gpa = round(random.normalvariate(3.0, 0.4), 2)
    gpa = min(max(gpa, 1.5), 4.0)
    internships = random.randint(0, 1)  # likely no experience
    internship_quality = random.randint(1, 3)
    work_while_studying = "no"
    extracurricular = random.choice(["yes", "no"])
    german_skills = random.randint(1, 4)
    age = random.randint(18, 23)
    debt_taken = 0
    prof_score = random.randint(2, 5)
    talentvest_score = random.randint(3, 5)
    target_industry = random.choice(industries)
    relocation = random.choice(["yes", "no"])
    motivation = random.randint(3, 5)

    total_debt_required = random.randint(20000, 50000)
    funding_needed = random.randint(5000, total_debt_required)
    isa_share_pct = 10
    term_years = 10
    documents_verified = random.choice(["Yes", "No"])
    willing_to_work = random.choice(["Yes", "No"])
    max_isa_right_share = round(funding_needed / total_debt_required, 2)

    data.append({
        "student_id": student_id,
        "name": name,
        "status": "studying",
        "program_duration_months": program_duration,
        "program_progress": program_progress,
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
        "motivation_score": motivation,
        "total_debt_required": total_debt_required,
        "funding_needed": funding_needed,
        "isa_share_pct": isa_share_pct,
        "term_years": term_years,
        "max_isa_right_share": max_isa_right_share,
        "documents_verified": documents_verified,
        "willing_to_work": willing_to_work
    })

# Create DataFrame and save
df = pd.DataFrame(data)
df.to_csv("data/students.csv", index=False)
print("✅ Generated data/students.csv with early-stage applicant profiles.")


