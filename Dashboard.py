import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

df = pd.read_excel("educational_center_Python_sample.xlsx", sheet_name="Sheet1")

users = {"admin": "admin123", "user1": "password1"}

def login():
    st.title("Space Zee Dashboard - Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state["authenticated"] = True
        else:
            st.error("Invalid credentials")

def dashboard():
    st.title("Space Zee Dashboard")

    with st.sidebar:
        st.header("Filter Options")
        gender_filter = st.multiselect("Select Gender", options=df["Gender"].unique(), default=df["Gender"].unique())
        course_filter = st.multiselect("Select Course", options=df["Course"].unique(), default=df["Course"].unique())
        name_search = st.text_input("Search Student Name")

    filtered_df = df[
        (df["Gender"].isin(gender_filter)) &
        (df["Course"].isin(course_filter)) &
        (df["Name"].str.contains(name_search, case=False, na=False))
    ]

    st.subheader("Filtered Student Records")
    st.dataframe(filtered_df)

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(px.histogram(filtered_df, x="Course", color="Gender", barmode="group", title="Students per Course"))
    with col2:
        fees_by_gender = filtered_df.groupby("Gender")["Fees_Paid"].sum().reset_index()
        st.plotly_chart(px.bar(fees_by_gender, x="Gender", y="Fees_Paid", title="Total Fees Paid by Gender"))

    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(px.pie(filtered_df, names="Course", title="Course Distribution"))
    with col4:
        assessment_cols = [col for col in filtered_df.columns if "Assessment" in col]
        assessment_avg = pd.DataFrame({
            "Assessment": assessment_cols,
            "Average Score": [filtered_df[col].mean() for col in assessment_cols]
        })
        st.plotly_chart(px.line(assessment_avg, x="Assessment", y="Average Score", markers=True, title="Average Scores per Assessment"))

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    login()
else:
    dashboard()
