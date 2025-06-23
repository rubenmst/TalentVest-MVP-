import pandas as pd
import random

import pandas as pd
import random

# Constants
names = [
    "Andrei Rusu", "Bianca Stoica", "Cristian Lupescu", "Daria Ciobanu", "Emil Iancu",
    "Florina Olaru", "Gabriel Vasilescu", "Helena Toma", "Ilie Cristea", "Jana Muresan",
    "Kiril Georgiev", "Lavinia Tudor", "Matei Sava", "Nikolai Draganov", "Olga Ionescu",
    "Petru Barbu", "Raluca Neagu", "Sorin Albu", "Tatiana Vekilova", "Vasile Rotaru"
]
countries = ["Romania", "Ukraine"]
fields = ["Computer Science", "Data Science", "Business Analytics", "IT"]
universities = ["TU München", "TU Berlin", "TU Darmstadt", "TU Aachen"]
degrees = ["Bachelors", "Masters"]
industries = ["Consulting", "Tech", "Automobile", "Industry", "Startup", "Finance", "Manufacturing", "Academia", "Non-profit", "Government"]

# ISA valuation function
def value_isa_right(current_salary, salary_growth, isa_pct, investor_share, payment_start_delay, discount_rate, term_years=10):
    isa_value = 0.0
    for t in range(1, term_years + 1):
        if t >= payment_start_delay + 1:
            salary_t = current_salary * ((1 + salary_growth) ** (t - 1))
            payment_t = salary_t * isa_pct * investor_share
            discounted_payment = payment_t / ((1 + discount_rate) ** t)
            isa_value += discounted_payment
    return round(isa_value, 2)

# Generate student data
data = []
for i, name in enumerate(names):
    student_id = f"TVTRADE{i+1:04d}"
    status = "studying"  # All are already in education
    country = random.choice(countries)
    university = random.choice(universities)
    field = random.choice(fields)
    degree = random.choice(degrees)
    program_duration = random.choice([36, 48, 60])
    program_progress = round(random.uniform(0.1, 0.95), 2)  # already started
    gpa = round(random.normalvariate(3.0, 0.4), 2)
    gpa = min(max(gpa, 1.5), 4.0)
    internship_count = random.randint(0, 3)
    internship_quality = min(5, max(1, int(gpa * 1.25) + random.choice([-1, 0, 1])))
    work_while_studying = random.choice(["yes", "no"])
    extracurricular_activities = random.choice(["yes", "no"])
    german_skills = random.randint(1, 5 if country == "Romania" else 4)
    age = random.randint(21, 32)
    debt_taken = random.randint(1000, 20000)
    prof_score = random.randint(1, 5)
    talentvest_score = random.randint(1, 5)
    target_industry = random.choice(industries)
    willingness_to_relocate = random.choice(["yes", "no"])
    motivation_score = random.randint(1, 5)

    # Predicted salary logic
    estimated_salary = int(gpa * 10000 + internship_quality * 2000 + random.randint(-3000, 3000))
    estimated_salary = max(estimated_salary, 20000)
    salary_growth = round(random.uniform(0.02, 0.06), 3)

    # Risk-based discounting
    risk_score = (6 - prof_score + 6 - talentvest_score + (5 - motivation_score)) / 3
    discount_rate = round(min(max(0.06 + risk_score * 0.02, 0.15), 0.06), 3)

    # ISA variables
    isa_pct = 0.10
    investor_share = random.choice([0.10, 0.25, 0.50])
    payment_start_delay = random.choice([1, 2, 3])
    total_debt_required = random.randint(20000, 50000)
    initial_investment = round(total_debt_required * investor_share, 2)

    # NPV valuation
    isa_value_estimate = value_isa_right(
        current_salary=estimated_salary,
        salary_growth=salary_growth,
        isa_pct=isa_pct,
        investor_share=investor_share,
        payment_start_delay=payment_start_delay,
        discount_rate=discount_rate
    )

    data.append({
        "student_id": student_id,
        "name": name,
        "status": status,
        "program_duration_months": program_duration,
        "program_progress": program_progress,
        "gpa": gpa,
        "field": field,
        "university": university,
        "degree": degree,
        "internship_count": internship_count,
        "internship_quality": internship_quality,
        "work_while_studying": work_while_studying,
        "extracurricular_activities": extracurricular_activities,
        "country": country,
        "german_skills": german_skills,
        "age": age,
        "debt_taken": debt_taken,
        "professor_score": prof_score,
        "talentvest_score": talentvest_score,
        "target_industry": target_industry,
        "willing_to_relocate": willingness_to_relocate,
        "motivation_score": motivation_score,
        "predicted_salary": estimated_salary,
        "salary_growth": salary_growth,
        "discount_rate": discount_rate,
        "isa_pct": isa_pct,
        "investor_share": investor_share,
        "payment_start_delay": payment_start_delay,
        "total_debt_required": total_debt_required,
        "initial_investment": initial_investment,
        "isa_value_estimate": isa_value_estimate
    })

# Save DataFrame
df = pd.DataFrame(data)
df.to_csv("data/students_trading.csv", index=False)
print("✅ Updated data/students_trading.csv with full feature set and ISA valuation.")



