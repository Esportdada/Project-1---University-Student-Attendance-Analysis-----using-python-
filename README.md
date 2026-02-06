# Project-1 ( University Student Attendance Analysis) -  using python 
The Student Attendance Management System is a simple project designed to record and manage student attendance digitally. It hlps reduce manual work and avoids errors found in traditional paper-based methods. The system stores student details and daily attendance records securely. Teachers can easily track attendance and calculate attendance percentages. Basic analysis helps identify irregulat attendance patterns. The project improves efficiency and accuracy in attendace management.
# University Student Attendance Analysis: Patterns, Risks & Insights

## 📌 Project Overview

This project focuses on analyzing real university student attendance data to uncover attendance patterns, identify students at risk of low attendance, and extract actionable academic insights using **Exploratory Data Analysis (EDA)**.

The goal of this project is **not prediction or machine learning**, but to demonstrate strong fundamentals in:

* Data understanding
* Data cleaning
* Exploratory analysis
* Feature engineering
* Insight-driven storytelling

This project is designed as **Project 1** in my data science journey, emphasizing clarity, logic, and real-world thinking.

---

## 📂 Dataset Information

* **Source:** Kaggle – University Attendance Sheet Dataset
* **Type:** Academic operational data
* **Granularity:** Student-level daily attendance records
* **Format:** CSV

### Key Characteristics

* Attendance marked as `P` (Present) and `A` (Absent)
* Multiple date-wise attendance columns
* Monthly and overall attendance summaries
* Structurally messy headers (real-world data issue)

---

## 🎯 Project Objectives

* Understand the structure and challenges of real academic data
* Clean and preprocess attendance records
* Analyze attendance distribution and trends
* Identify students with low or inconsistent attendance
* Categorize students based on attendance risk levels
* Generate insights useful for academic intervention

---

## 🛠 Tools & Technologies Used

* **Python**
* **Pandas** – data manipulation
* **NumPy** – numerical operations
* **Matplotlib** – data visualization

---

## 🔄 Project Workflow

### Phase 1: Data Understanding

* Examined raw dataset structure
* Identified duplicate headers and non-data rows
* Studied attendance marking patterns

### Phase 2: Data Cleaning

* Removed structural header rows
* Renamed columns for clarity
* Converted attendance values (`P/A`) to numerical format (`1/0`)
* Corrected data types for percentage fields

### Phase 3: Exploratory Data Analysis (EDA)

* Overall attendance distribution analysis
* Student-wise attendance comparison
* Date-wise attendance trend analysis
* Identification of attendance drop patterns

### Phase 4: Feature Engineering

* Attendance percentage calculations
* Monthly vs overall attendance comparison
* Attendance risk categorization:

  * **Low Risk** (≥ 85%)
  * **Medium Risk** (75–84%)
  * **High Risk** (< 75%)

### Phase 5: Insights & Recommendations

* Identified students requiring early academic intervention
* Observed attendance fatigue patterns across dates
* Suggested data-driven monitoring strategies for institutions

---

## 📊 Key Insights

* Majority of students maintain high attendance levels
* A small but critical group falls below acceptable attendance thresholds
* Attendance consistency is as important as attendance percentage
* Early identification of declining trends can prevent academic issues

---

## 📁 Repository Structure

```
Student-Attendance-Analysis/
│
├── code/
│   └── student_attendance.py
├── data/
│   └── student_attendance.csv
├── plots/
│   └── figure_1.png
|   |__ histogram.png
├── README.md
└── requirements.txt
```

---

## 🚀 Future Improvements

* Extend analysis to larger academic datasets
* Include subject-wise attendance patterns
* Apply machine learning models in a separate project
* Build a dashboard for real-time attendance monitoring

---

## 👤 Author

**Shubham Vatare**
B.Sc. (Voc.) Data Science & AI Student
Aspiring Data Analyst / Data Scientist

---

## 📎 Note

This project intentionally focuses on **EDA and analytics** to strengthen foundational data science skills. Predictive modeling and machine learning will be explored in future projects.

