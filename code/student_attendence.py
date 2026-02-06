import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# ---------------- LOAD DATA ----------------
df = pd.read_csv(
    "C:/Users/Admin/Desktop/Project/Project_1/Project-1---University-Student-Attendance-Analysis-----using-python-/data/AI_csv.csv"
)

# Drop unwanted first row if it is header junk
df = df.drop(index=0).reset_index(drop=True)

# Rename columns
df.columns = [
    "Roll_no", "Student_Name",
    "09_Jan", "10_Jan", "16_Jan", "17_Jan",
    "23_Jan", "24_Jan", "30_Jan", "31_Jan",
    "Month_Attended", "Month_Total", "Month_Percent",
    "Overall_Attended", "Overall_Total", "Overall_Percent"
]

# ---------------- ATTENDANCE CLEANING ----------------
attendance_cols = [
    "09_Jan", "10_Jan", "16_Jan", "17_Jan",
    "23_Jan", "24_Jan", "30_Jan", "31_Jan"
]

# Convert P/A to numeric
df[attendance_cols] = df[attendance_cols].replace({
    "P": 1,
    "A": 0,
    "": np.nan
})

# Force numeric (VERY IMPORTANT)
df[attendance_cols] = df[attendance_cols].apply(
    pd.to_numeric, errors="coerce"
)

# ---------------- PERCENTAGE CLEANING ----------------
percent_cols = ["Month_Percent", "Overall_Percent"]

for col in percent_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace("%", "", regex=False)
    )
    df[col] = pd.to_numeric(df[col], errors="coerce")

# ---------------- ANALYSIS ----------------
print("Average Overall Attendance:", df["Overall_Percent"].mean())

at_risk = df[df["Overall_Percent"] < 75]
print(at_risk[["Roll_no", "Student_Name", "Overall_Percent"]])

# ---------------- DAILY ATTENDANCE TREND ----------------
daily_attendance = df[attendance_cols].mean()

plt.figure()
daily_attendance.plot(kind="line", marker="o")
plt.title("Average Daily Attendance Trend")
plt.ylabel("Attendance Rate")
plt.xlabel("Date")
plt.show()

# ---------------- DISTRIBUTION ----------------
plt.figure()
plt.hist(df["Overall_Percent"], bins=5)
plt.title("Distribution of Overall Attendance")
plt.xlabel("Attendance Percentage")
plt.ylabel("Number of Students")
plt.show()

# ---------------- RISK CLASSIFICATION ----------------
def risk_level(x):
    if x < 75:
        return "High Risk"
    elif x < 85:
        return "Medium Risk"
    else:
        return "Low Risk"

df["Risk_level"] = df["Overall_Percent"].apply(risk_level)

# Target column for ML
df["Target_Risk"] = df["Overall_Percent"].apply(
    lambda x: 1 if x < 75 else 0
)

print(df.head())