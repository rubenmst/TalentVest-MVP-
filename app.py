import streamlit as st
import pandas as pd

st.set_page_config(page_title="Student-Investor Match Dashboard", layout="centered")

# Title and description
st.title("Student–Investor Matching Dashboard")
st.write("Welcome! Here you can explore student profiles and find candidates to invest in. "
         "Use the filters below to narrow down students by field or other criteria.")

# Load student data
DATA_PATH = "data/students.csv"
df = pd.read_csv(DATA_PATH)

# Display all students initially
st.subheader("All Students")
st.dataframe(df)

# Filter by field of study
fields = ["All"] + sorted(df["field"].unique())  # ✅ lowercase
chosen_field = st.selectbox("Filter by field of study:", fields)
if chosen_field and chosen_field != "All":
    filtered_df = df[df["field"] == chosen_field]
else:
    filtered_df = df

st.write(f"**Displaying {len(filtered_df)} students**")
st.dataframe(filtered_df)

# Select a student and fund
student_names = filtered_df["name"].tolist()
if student_names:
    selected_student = st.selectbox("Select a student to fund:", student_names)
    if st.button("💰 Fund this student"):
        st.success(f"You have chosen to fund **{selected_student}**! 🎉")
