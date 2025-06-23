import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Set custom page config and theme-aware design
st.set_page_config(page_title="TalentVest - Matching Platform", layout="centered")

# Logo
logo = Image.open("static/logo.png")
col1, col2 = st.columns([1, 5])
with col1:
    st.image(logo, width=100)
with col2:
    st.title("TalentVest – Matching Platform")

# Initialize session state to track user role and student step
if "role" not in st.session_state:
    st.session_state.role = None
if "student_step" not in st.session_state:
    st.session_state.student_step = None
if "investor_index" not in st.session_state:
    st.session_state.investor_index = 0
if "portfolio" not in st.session_state:
    st.session_state.portfolio = []

# Load data only if needed later
DATA_PATH = "data/students.csv"
df = pd.read_csv(DATA_PATH)

# Home page: User role selection
if st.session_state.role is None:
    st.title("Welcome to TalentVest")
    st.markdown("### Empowering Education through Income Share Agreements")
    st.write("Select your role to get started:")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("I am a Student"):
            st.session_state.role = "student"
    with col2:
        if st.button("I am an Investor"):
            st.session_state.role = "investor"

# Student section with options
elif st.session_state.role == "student" and st.session_state.student_step is None:
    st.title("Student Portal")
    st.write("Choose what you want to do:")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("I want to apply for funding!"):
            st.session_state.student_step = "form"
    with col2:
        if st.button("I want to manage my education!"):
            st.session_state.student_step = "manage"
    if st.button("Back to Role Selection"):
        st.session_state.role = None
        st.session_state.student_step = None

# Student application form
elif st.session_state.role == "student" and st.session_state.student_step == "form":
    st.title("Student Application Form")
    with st.form("student_form"):
        first_name = st.text_input("First Name")
        last_name = st.text_input("Name")
        birthday = st.date_input("Birthday")
        country = st.text_input("Country")
        city = st.text_input("City")
        highschool = st.text_input("Highschool")
        grad_year = st.number_input("Graduation Year", min_value=1900, max_value=2100, step=1)
        degree = st.text_input("Highschool Degree")
        grade = st.text_input("Highschool Grade")
        birth_cert = st.file_uploader("Upload Birth Certificate", type=["pdf", "jpg", "png"])
        diploma = st.file_uploader("Upload Diploma", type=["pdf", "jpg", "png"])
        submitted = st.form_submit_button("Continue to Questionnaire")
        if submitted:
            st.session_state.student_step = "questionnaire"
    if st.button("Back"):
        st.session_state.student_step = None

# Placeholder for questionnaire
elif st.session_state.role == "student" and st.session_state.student_step == "questionnaire":
    st.title("Student Questionnaire (Coming Soon)")
    st.info("This section will contain motivation and background questions.")
    if st.button("Back"):
        st.session_state.student_step = None

# Student education management
elif st.session_state.role == "student" and st.session_state.student_step == "manage":
    st.title("Manage My Education")
    st.markdown("This section helps you keep your investors updated with academic progress and insights.")

    # Mocked student summary table
    st.subheader("Current Academic Summary")
    student_summary = {
        "Name": "Alex Student",
        "Study": "Business Analytics",
        "University": "University of Amsterdam",
        "Semester": "3rd",
        "Overall GPA": 3.6,
        "Recent Grades": "Finance A-, Data Science B+",
        "Recent News": "Accepted for summer internship at Deloitte."
    }
    st.table(pd.DataFrame(student_summary.items(), columns=["Field", "Value"]))

    # Quarterly questionnaire section
    st.markdown("---")
    st.subheader("Quarterly Update Questionnaire")
    st.markdown("Please fill in your latest updates for the investors. Transparency helps build trust!")

    with st.form("quarterly_form"):
        academic_progress = st.text_area("Academic Progress:", "Share course performance, completed credits, or any academic challenges.")
        personal_growth = st.text_area("Personal Growth:", "Share personal development, mentorships, leadership, etc.")
        future_plans = st.text_area("Plans Ahead:", "What are your plans for the next quarter? Any internships, projects, job search?")
        support_needed = st.text_area("Support Needed:", "Are there areas where you’d benefit from investor support or advice?")
        grade_transcript = st.file_uploader("Upload Recent Grade Transcript", type=["pdf", "jpg", "png"])
        other_documents = st.file_uploader("Upload Other Relevant Documents", type=["pdf", "jpg", "png"])
        submitted = st.form_submit_button("Submit Quarterly Update")

        if submitted:
            st.success("Your quarterly update has been submitted. Thank you for keeping your investors informed!")

    if st.button("Back"):
        st.session_state.student_step = None

# Investor dashboard view with card carousel and portfolio
elif st.session_state.role == "investor":
    st.title("Investor Dashboard")
    st.write("Explore and fund talented students through Income Share Agreements.")

        # Initialize toggles once
    if "show_details" not in st.session_state:
        st.session_state.show_details = False
    if "show_financials" not in st.session_state:
        st.session_state.show_financials = False

    # Section 1: New Funding Possibilities
    st.header("New Funding Opportunities")
    fields = ["All"] + sorted(df["field"].unique())
    chosen_field = st.selectbox("Filter by field of study:", fields)
    if chosen_field != "All":
        filtered_df = df[df["field"] == chosen_field].reset_index(drop=True)
    else:
        filtered_df = df.reset_index(drop=True)

    if len(filtered_df) > 0:
        current_index = st.session_state.investor_index
        student = filtered_df.iloc[current_index]

        st.markdown("---")
        st.subheader(f" {student['name']}")
        st.markdown(f"**University:** {student['university']}")
        st.markdown(f"**Field:** {student['field']}")
        st.markdown(f"**Country:** {student['country']}")
        st.markdown(f"**Total Debt Required:** €{round(student['total_debt_required'], 2)}")
        st.markdown(f"**Funding Needed:** €{round(student['funding_needed'], 2)}")
        st.markdown(f"**GPA:** {round(student['gpa'], 2)}")

        # Buttons to toggle expanders
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Show Details"):
                st.session_state.show_details = not st.session_state.show_details
        with col2:
            if st.button("Financials"):
                st.session_state.show_financials = not st.session_state.show_financials
        with col3:
            fund_placeholder = st.empty()
            if st.button("Funding", key="funding_button"):
                with fund_placeholder.container():
                    funding_amount = st.number_input("Enter your funding amount (€):", min_value=1.0, step=100.0, format="%.2f", key="funding_input")
                    if st.button("Submit Funding", key="submit_funding"):
                        st.success(f"You have committed €{funding_amount:.2f} to this student! (placeholder logic)")
                        st.session_state.portfolio.append({**student, "committed_funding": funding_amount})

        # Conditionally render expanders
        if st.session_state.show_details:
            with st.expander(f"Profile Details: {student['name']}", expanded=True):
                st.markdown("### Profile Characteristics")
                detail_keys = [
                    "program_duration_months", "degree", "internship_count", "extracurricular_activities",
                    "german_skills", "age", "target_industry", "willing_to_relocate", "motivation_score"
                ]
                for key in detail_keys:
                    if key in student:
                        st.write(f"**{key.replace('_',' ').capitalize()}**: {student[key]}")

        if st.session_state.show_financials:
            with st.expander(f"Financial Overview: {student['name']}", expanded=True):
                st.markdown("### Financial & Analytical Data")
                financial_keys = [
                    "total_debt_required", "funding_needed", "max_isa_right_share",
                    "predicted_salary", "salary_growth", "discount_rate",
                    "isa_value_estimate", "initial_investment", "profit", "roi"
                ]
                st.write(f"**ISA Share Pct (Fixed):** 15.00%")
                for key in financial_keys:
                    if key in student:
                        val = student[key]
                        if isinstance(val, (float, int)):
                            val = round(val, 2)
                        st.write(f"**{key.replace('_',' ').capitalize()}**: {val}")

        # Navigation
        nav_col1, nav_col2 = st.columns([1, 1])
        with nav_col1:
            if st.button("Previous"):
                if st.session_state.investor_index > 0:
                    st.session_state.investor_index -= 1
                    st.session_state.show_details = False
                    st.session_state.show_financials = False
        with nav_col2:
            if st.button("Next"):
                if st.session_state.investor_index < len(filtered_df) - 1:
                    st.session_state.investor_index += 1
                    st.session_state.show_details = False
                    st.session_state.show_financials = False
    else:
        st.info("No students available in this category.")


    # Initialize trading toggles once
    if "show_trade_details" not in st.session_state:
        st.session_state.show_trade_details = False
    if "show_trade_financials" not in st.session_state:
        st.session_state.show_trade_financials = False

    # Section 2: Trading Opportunities
    st.markdown("---")
    st.header("Trading Opportunities")

    trading_df = pd.read_csv("data/students_trading.csv")

    if "trading_index" not in st.session_state:
        st.session_state.trading_index = 0

    if len(trading_df) > 0:
        current_index = st.session_state.trading_index
        trade_student = trading_df.iloc[current_index]

        st.subheader(f"{trade_student['name']}")
        st.markdown(f"**University:** {trade_student['university']}")
        st.markdown(f"**Field:** {trade_student['field']}")
        st.markdown(f"**Country:** {trade_student['country']}")
        st.markdown(f"**Program Progress:** {trade_student['status'].capitalize()}")
        st.markdown(f"**GPA:** {round(trade_student['gpa'], 2)}")

        # Buttons to toggle expanders
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("Show Details", key="btn_trade_details"):
                st.session_state.show_trade_details = not st.session_state.show_trade_details
        with col2:
            if st.button("Financials", key="btn_trade_financials"):
                st.session_state.show_trade_financials = not st.session_state.show_trade_financials
        with col3:
            offer_placeholder = st.empty()
            if st.button("Make an Offer", key="offer_trade"):
                with offer_placeholder.container():
                    offer_amount = st.number_input("Enter your offer amount (€):", min_value=1.0, step=100.0, format="%.2f", key="offer_input_trade")
                    if st.button("Submit Offer", key="submit_offer_trade"):
                        st.success(f"Offer of €{offer_amount:.2f} submitted to rights owner! (placeholder logic)")

        # Conditionally render expanders
        if st.session_state.show_trade_details:
            with st.expander(f"Profile Details: {trade_student['name']}", expanded=True):
                st.markdown("### Profile Characteristics")
                trade_detail_keys = [
                    "program_duration_months", "degree", "internship_count", "internship_quality", "work_while_studying",
                    "extracurricular_activities", "german_skills", "professor_score", "talentvest_score",
                    "target_industry", "willing_to_relocate", "motivation_score"
                ]
                for key in trade_detail_keys:
                    if key in trade_student:
                        st.write(f"**{key.replace('_',' ').capitalize()}**: {trade_student[key]}")

        if st.session_state.show_trade_financials:
            with st.expander(f"Financial Overview: {trade_student['name']}", expanded=True):
                st.markdown("### Financial & Analytical Data")
                st.write(f"**ISA Share Pct:** {round(trade_student['isa_pct'], 2)}%")
                trade_financial_keys = [
                    "total_debt_required", "initial_investment", "investor_share", "predicted_salary",
                    "salary_growth", "discount_rate", "isa_value_estimate", "profit", "roi"
                ]
                for key in trade_financial_keys:
                    if key in trade_student:
                        val = trade_student[key]
                        if isinstance(val, (float, int)):
                            val = round(val, 2)
                        st.write(f"**{key.replace('_',' ').capitalize()}**: {val}")

        # Navigation
        nav_col1, nav_col2 = st.columns([1, 1])
        with nav_col1:
            if st.button("Previous", key="prev_trade"):
                if st.session_state.trading_index > 0:
                    st.session_state.trading_index -= 1
                    st.session_state.show_trade_details = False
                    st.session_state.show_trade_financials = False
        with nav_col2:
            if st.button("Next", key="next_trade"):
                if st.session_state.trading_index < len(trading_df) - 1:
                    st.session_state.trading_index += 1
                    st.session_state.show_trade_details = False
                    st.session_state.show_trade_financials = False
    else:
        st.info("No ISA rights currently available for trading.")

    # Section 3: Portfolio Overview
    st.markdown("---")
    st.header("My Investment Portfolio")

    if "portfolio_view" not in st.session_state:
        st.session_state.portfolio_view = None

    portfolio_df = pd.read_csv("data/portfolio_sample.csv")

    if st.session_state.portfolio_view is None:
        for index, row in portfolio_df.iterrows():
            col1, col2, col3 = st.columns([3, 3, 2])
            with col1:
                if st.button(row["name"], key=f"portfolio_name_{index}"):
                    st.session_state.portfolio_view = row["name"]
            with col2:
                st.write(f"{row['university']} – {row['field']}")
            with col3:
                st.write(f"NPV: €{round(row['isa_value_estimate'], 2)}")
    else:
        selected = portfolio_df[portfolio_df["name"] == st.session_state.portfolio_view].squeeze()

        st.title(f"Detailed View: {selected['name']}")

        # --- Profile Section ---
        with st.expander("Profile Overview", expanded=True):
            profile_keys = [
                "name", "status", "gpa", "field", "university", "degree", "internship_count", "internship_quality",
                "work_while_studying", "extracurricular_activities", "country", "german_skills", "age", "debt_taken",
                "professor_score", "talentvest_score", "target_industry", "willing_to_relocate", "motivation_score"
            ]
            for key in profile_keys:
                if key in selected:
                    st.write(f"**{key.replace('_',' ').capitalize()}**: {selected[key]}")

        # --- Financials Section ---
        with st.expander("Financials & Analytics", expanded=True):
            financial_keys = [
                "predicted_salary", "salary_growth", "discount_rate", "isa_pct", "investor_share",
                "payment_start_delay", "total_debt_required", "initial_investment", "isa_value_estimate"
            ]
            for key in financial_keys:
                if key in selected:
                    val = selected[key]
                    if isinstance(val, (float, int)):
                        val = round(val, 2)
                    st.write(f"**{key.replace('_',' ').capitalize()}**: {val}")

            # Financial bar chart
            st.markdown("#### Financial Breakdown Comparison")
            metrics = {
                "Initial Investment": selected.get("initial_investment", 0),
                "ISA Value Estimate": selected.get("isa_value_estimate", 0),
                "Total Debt Required": selected.get("total_debt_required", 0)
            }
            fig, ax = plt.subplots()
            bars = ax.bar(metrics.keys(), [round(v, 2) for v in metrics.values()])
            ax.set_ylabel("€")
            ax.set_title("Investment vs. Return Potential")
            st.pyplot(fig)

        if st.button("Back to Portfolio"):
            st.session_state.portfolio_view = None

    # Back to role selection
    if st.button("Back to Role Selection"):
        st.session_state.role = None
        st.session_state.investor_index = 0
        st.session_state.portfolio = []








