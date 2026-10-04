import streamlit as st
import pandas as pd

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Tools & Student Productivity Analyzer",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("🤖 AI Tools Usage & Student Productivity Analyzer")

st.write(
    "Analyze how students use different AI tools and study "
    "their impact on student productivity."
)

# ---------------------------------------------------
# LOAD DATASET
# ---------------------------------------------------

df = pd.read_csv("data/ai_student_usage.csv")

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

st.sidebar.header("🔎 Dashboard Filters")

# Department filter
department_options = ["All"] + sorted(
    df["Department"].unique().tolist()
)

selected_department = st.sidebar.selectbox(
    "🏫 Department",
    department_options
)

# Year filter
year_options = ["All"] + sorted(
    df["Year"].unique().tolist()
)

selected_year = st.sidebar.selectbox(
    "📚 Year",
    year_options
)

# ---------------------------------------------------
# APPLY FILTERS
# ---------------------------------------------------

filtered_df = df.copy()

if selected_department != "All":
    filtered_df = filtered_df[
        filtered_df["Department"] == selected_department
    ]

if selected_year != "All":
    filtered_df = filtered_df[
        filtered_df["Year"] == selected_year
    ]

# ---------------------------------------------------
# FILTER STATUS
# ---------------------------------------------------

st.subheader("🔎 Current Selection")

st.write(
    f"Showing **{len(filtered_df)} students** "
    f"out of **{len(df)} total students**."
)

# ---------------------------------------------------
# DATASET PREVIEW
# ---------------------------------------------------

st.subheader("📋 Student AI Usage Data")

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ---------------------------------------------------
# BASIC STATISTICS
# ---------------------------------------------------

st.subheader("📊 Basic Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Students",
        len(filtered_df)
    )

with col2:
    st.metric(
        "AI Tools",
        filtered_df["AI_Tool"].nunique()
    )

with col3:
    if len(filtered_df) > 0:
        average_usage = filtered_df[
            "Hours_Per_Week"
        ].mean()

        st.metric(
            "Average AI Usage",
            f"{average_usage:.1f} hrs/week"
        )
    else:
        st.metric(
            "Average AI Usage",
            "N/A"
        )

with col4:
    if len(filtered_df) > 0:
        average_productivity = filtered_df[
            "Productivity_After"
        ].mean()

        st.metric(
            "Average Productivity",
            f"{average_productivity:.2f}/5"
        )
    else:
        st.metric(
            "Average Productivity",
            "N/A"
        )

# ---------------------------------------------------
# CHECK EMPTY DATA
# ---------------------------------------------------

if len(filtered_df) == 0:

    st.warning(
        "⚠️ No students match the selected filters. "
        "Please change your filters."
    )

    st.stop()

# ---------------------------------------------------
# CHARTS
# ---------------------------------------------------

st.subheader("📊 AI Usage Analysis")

# ---------------------------------------------------
# CHART 1 - MOST USED AI TOOLS
# ---------------------------------------------------

st.write("### 🤖 Most Used AI Tools")

tool_count = filtered_df[
    "AI_Tool"
].value_counts()

st.bar_chart(tool_count)

# ---------------------------------------------------
# CHART 2 - AI USAGE BY PURPOSE
# ---------------------------------------------------

st.write("### 🎯 AI Usage by Purpose")

purpose_count = filtered_df[
    "AI_Purpose"
].value_counts()

st.bar_chart(purpose_count)

# ---------------------------------------------------
# CHART 3 - USAGE FREQUENCY
# ---------------------------------------------------

st.write("### 📅 AI Usage Frequency")

frequency_count = filtered_df[
    "Usage_Frequency"
].value_counts()

st.bar_chart(frequency_count)

# ---------------------------------------------------
# CHART 4 - DEPARTMENT-WISE AI USAGE
# ---------------------------------------------------

st.write("### 🏫 Department-wise AI Usage")

department_usage = (
    filtered_df
    .groupby("Department")["Hours_Per_Week"]
    .mean()
    .round(2)
)

st.bar_chart(department_usage)

# ---------------------------------------------------
# CHART 5 - PRODUCTIVITY BEFORE VS AFTER AI
# ---------------------------------------------------

st.write("### 📈 Productivity Before vs After AI")

productivity_data = pd.DataFrame({
    "Productivity": [
        filtered_df["Productivity_Before"].mean(),
        filtered_df["Productivity_After"].mean()
    ]
}, index=[
    "Before AI",
    "After AI"
])

st.bar_chart(productivity_data)

# ---------------------------------------------------
# CHART 6 - AI DEPENDENCY
# ---------------------------------------------------

st.write("### ⚠️ AI Dependency Distribution")

dependency_count = filtered_df[
    "AI_Dependence"
].value_counts()

st.bar_chart(dependency_count)

# ---------------------------------------------------
# PRODUCTIVITY SUMMARY
# ---------------------------------------------------

st.subheader("📈 Productivity Summary")

productivity_before = filtered_df[
    "Productivity_Before"
].mean()

productivity_after = filtered_df[
    "Productivity_After"
].mean()

improvement = (
    productivity_after -
    productivity_before
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Productivity Before AI",
        f"{productivity_before:.2f}/5"
    )

with col2:
    st.metric(
        "Productivity After AI",
        f"{productivity_after:.2f}/5"
    )

with col3:
    st.metric(
        "Average Improvement",
        f"{improvement:+.2f}"
    )