# 🤖 AI Tools Usage & Student Productivity Analyzer

## 📌 Project Overview

The **AI Tools Usage & Student Productivity Analyzer** is a Python-based data analysis project that explores how students use Artificial Intelligence (AI) tools and examines their perceived impact on productivity and academic performance.

The project analyzes student survey responses and presents meaningful insights through interactive visualizations and a Streamlit dashboard.

It focuses on popular AI tools such as ChatGPT, Google Gemini, Claude, and Perplexity to understand students' usage patterns, academic applications, and experiences with AI-assisted learning.

## 🎯 Objectives

- Analyze the usage of AI tools among students.
- Identify the most popular AI tools for academic purposes.
- Study the relationship between AI usage and student productivity.
- Explore students' perceptions of AI's impact on academic performance.
- Compare AI usage patterns across different departments and academic years.
- Present insights through interactive charts, graphs, and summary metrics.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data cleaning and manipulation |
| Streamlit | Interactive dashboard development |
| Plotly / Matplotlib | Data visualization, depending on the implementation |
| Excel / CSV | Survey data storage |
| Git | Version control |
| GitHub | Source code management and collaboration |
| GitHub Actions | Automated testing or CI workflows, if configured |

## 📂 Project Structure

```text
AI-Tools-Student-Productivity-Analyzer/
│
├── app.py
├── Student_Survey_AI_Tools_(Responses).xlsx
├── requirements.txt
├── README.md
├── .gitignore
│
└── .github/
    └── workflows/
        └── ci.yml
```

*Note: The `.github/workflows/ci.yml` file should be included only if you have created a GitHub Actions workflow. Adjust the filenames and folders to match your actual repository.*

## 📊 Dataset Description

The dataset contains responses collected through a student survey about AI tool usage, academic activities, productivity, and academic performance.

**Dataset file:** `Student_Survey_AI_Tools_(Responses).xlsx`

The survey may include information such as:

- Department and academic year
- AI tools used by students
- Frequency and purpose of AI tool usage
- Time spent using AI tools
- Perceived changes in productivity
- Students' assessment of their academic performance after using AI tools

The exact columns depend on the final survey form and response sheet.

## ⚙️ Key Features

### 1. Interactive Dashboard
Displays survey insights in an organized and user-friendly interface using Streamlit.

### 2. Data Analysis
Processes survey responses to identify trends, distributions, and patterns in AI tool usage.

### 3. AI Tool Usage Analysis
Helps identify which AI tools students prefer and how they use them for academic activities.

### 4. Productivity Analysis
Explores students' reported productivity levels and their experiences with AI-assisted learning.

### 5. Academic Performance Insights
Examines students' perceptions of the relationship between AI tool usage and academic performance.

### 6. Department and Year Filters
Allows users to filter survey results by department and academic year to compare different student groups.

### 7. Data Visualization
Uses charts and graphs to make survey findings easier to interpret.

## 📈 Expected Outcomes

The project aims to provide insights into:

- Popular AI tools among students.
- Differences in AI adoption across academic departments and years.
- Common academic applications of AI tools.
- Students' perceived productivity improvements.
- Students' perceptions of AI's relationship with academic performance.

**Important:** These are research questions and intended insights, not predetermined findings. Actual conclusions should be based on the collected survey data.

## 🚀 Installation and Setup

### Prerequisites

- Python 3.10 or a compatible version
- pip package manager
- Visual Studio Code or another Python IDE
- Git (optional, for version control)

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate into the project folder:

```bash
cd AI-Tools-Student-Productivity-Analyzer
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

If the requirements file is not available, install the necessary packages:

```bash
pip install streamlit pandas openpyxl matplotlib plotly
```

Install only the libraries used by your actual implementation.

### Step 4: Run the Application

```bash
streamlit run app.py
```

Streamlit will provide a local URL, usually:

```text
http://localhost:8501
```

Open the URL in your browser to access the dashboard.

## 🔄 Project Workflow

1. Collect student responses through a survey form.
2. Export the responses to an Excel or CSV file.
3. Load the dataset using Pandas.
4. Inspect and clean the data as required.
5. Analyze AI tool usage, productivity, and academic performance responses.
6. Generate charts and summary metrics.
7. Display the results through an interactive Streamlit dashboard.
8. Use Git and GitHub to manage project versions and collaborate.
9. Test the application and improve it based on the results.

## 🧪 Testing

The project can be tested by:

- Verifying that the dataset loads correctly.
- Checking for missing or invalid values.
- Confirming that charts display the correct information.
- Testing department and academic-year filters.
- Ensuring the dashboard handles empty or filtered datasets.
- Checking that the application starts without errors.

Automated testing and GitHub Actions can be added to validate the application whenever code changes are pushed.

## 🔮 Future Enhancements

- Add more interactive visualizations.
- Include additional AI tools and academic use cases.
- Add more advanced statistical analysis.
- Introduce machine learning models to explore patterns in student responses.
- Export filtered reports as PDF or Excel files.
- Deploy the dashboard online for public access.
- Add automated tests and a continuous integration workflow.

## ⚠️ Limitations

- Survey findings depend on the quality and representativeness of the responses.
- Self-reported productivity and academic performance may be subjective.
- Observed associations do not establish that AI usage causes changes in academic performance.
- Results may not generalize to all students or institutions.

## 🔐 Data Privacy

Survey data should be handled responsibly. Avoid publishing students' names, email addresses, contact details, or other personally identifiable information. Share only data that is appropriate for public release.

## 👨‍💻 Author

**Project:** AI Tools Usage & Student Productivity Analyzer

**Domain:** Python, Data Analytics, Data Visualization

**Purpose:** Academic project and student survey analysis

## 📜 License

This project can be distributed under the MIT License if you choose to include one. Add a `LICENSE` file before claiming that the repository is licensed under MIT.

---

⭐ If you find this project useful, consider starring the repository and sharing your feedback.
