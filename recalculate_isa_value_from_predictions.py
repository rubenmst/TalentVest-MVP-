import pandas as pd

# ISA valuation function with 15-year term
def value_isa_right(current_salary, salary_growth, isa_pct, investor_share, payment_start_delay, discount_rate, term_years=15):
    isa_value = 0.0
    for t in range(1, term_years + 1):
        if t >= payment_start_delay + 1:
            salary_t = current_salary * ((1 + salary_growth) ** (t - 1))
            payment_t = salary_t * isa_pct * investor_share
            discounted_payment = payment_t / ((1 + discount_rate) ** t)
            isa_value += discounted_payment
    return round(isa_value, 2)

# Update ISA valuation + profit and ROI
def update_isa_valuation(file_path):
    df = pd.read_csv(file_path)

    # Ensure required columns exist
    df["isa_pct"] = 0.15  # Set ISA % to 15
    if "investor_share" not in df.columns:
        df["investor_share"] = 0.25
    if "payment_start_delay" not in df.columns:
        df["payment_start_delay"] = 0
    if "initial_investment" not in df.columns:
        # Compute it if needed
        df["initial_investment"] = df["total_debt_required"] * df["investor_share"]

    # Compute ISA valuation (NPV)
    df["isa_value_estimate"] = df.apply(lambda row: value_isa_right(
        current_salary=row["predicted_salary"],
        salary_growth=row["salary_growth"],
        isa_pct=row["isa_pct"],
        investor_share=row["investor_share"],
        payment_start_delay=row["payment_start_delay"],
        discount_rate=row["discount_rate"]
    ), axis=1)

    # Add profit and ROI
    df["profit"] = df["isa_value_estimate"] - df["initial_investment"]
    df["roi"] = df["isa_value_estimate"] / df["initial_investment"]

    # Save back
    df.to_csv(file_path, index=False)
    print(f"✅ Updated: {file_path}")

# Apply to all datasets
update_isa_valuation("data/students.csv")
update_isa_valuation("data/students_trading.csv")
update_isa_valuation("data/portfolio_sample.csv")
