# -----------------------------
# Prodigy InfoTech _ Data Science Internship
# TASK:02  Data Cleaning and Exploratory Data Analysis (EDA)
# -----------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("train.csv")

# -----------------------------
# Basic Information
# -----------------------------
print("="*50)
print("FIRST 5 ROWS")
print("="*50)
print(df.head())

print("\n" + "="*50)
print("DATASET INFORMATION")
print("="*50)
print(df.info())

print("\n" + "="*50)
print("STATISTICAL SUMMARY")
print("="*50)
print(df.describe())

print("\nDataset Shape:", df.shape)

# -----------------------------
# Missing Values
# -----------------------------
print("\n" + "="*50)
print("MISSING VALUES")
print("="*50)
print(df.isnull().sum())

# -----------------------------
# Data Cleaning
# -----------------------------

# Fill missing Age values with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked values with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Drop Cabin column because it has many missing values
df.drop(columns=["Cabin"], inplace=True)

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# -----------------------------
# Set Plot Style
# -----------------------------
sns.set_style("whitegrid")

# =====================================================
# 1. Survival Count
# =====================================================

plt.figure(figsize=(6,4))
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Number of Passengers")
plt.savefig("survival_count.png")
plt.show()

# =====================================================
# 2. Gender Distribution
# =====================================================

plt.figure(figsize=(6,4))
sns.countplot(x="Sex", data=df)
plt.title("Gender Distribution")
plt.savefig("gender_distribution.png")
plt.show()

# =====================================================
# 3. Survival by Gender
# =====================================================

plt.figure(figsize=(6,4))
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival by Gender")
plt.savefig("survival_by_gender.png")
plt.show()

# =====================================================
# 4. Passenger Class Distribution
# =====================================================

plt.figure(figsize=(6,4))
sns.countplot(x="Pclass", data=df)
plt.title("Passenger Class Distribution")
plt.savefig("passenger_class.png")
plt.show()

# =====================================================
# 5. Survival by Passenger Class
# =====================================================

plt.figure(figsize=(6,4))
sns.countplot(x="Pclass", hue="Survived", data=df)
plt.title("Survival by Passenger Class")
plt.savefig("survival_by_class.png")
plt.show()

# =====================================================
# 6. Age Distribution
# =====================================================

plt.figure(figsize=(8,5))
sns.histplot(df["Age"], bins=30, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("age_distribution.png")
plt.show()

# =====================================================
# 7. Fare Distribution
# =====================================================

plt.figure(figsize=(8,5))
sns.histplot(df["Fare"], bins=30, kde=True)
plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.savefig("fare_distribution.png")
plt.show()

# =====================================================
# 8. Correlation Heatmap
# =====================================================

numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(10,8))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)
plt.title("Correlation Heatmap")
plt.savefig("correlation_heatmap.png")
plt.show()

# =====================================================
# 9. Boxplot of Age by Survival
# =====================================================

plt.figure(figsize=(6,4))
sns.boxplot(x="Survived", y="Age", data=df)
plt.title("Age vs Survival")
plt.savefig("age_vs_survival.png")
plt.show()

# =====================================================
# 10. Fare by Passenger Class
# =====================================================

plt.figure(figsize=(6,4))
sns.boxplot(x="Pclass", y="Fare", data=df)
plt.title("Fare by Passenger Class")
plt.savefig("fare_by_class.png")
plt.show()

# =====================================================
# 11. Pairplot
# =====================================================

sns.pairplot(
    df[["Survived","Age","Fare","Pclass"]],
    hue="Survived"
)
plt.savefig("pairplot.png")
plt.show()

# =====================================================
# Final Message
# =====================================================

print("\n" + "="*60)
print("EDA COMPLETED SUCCESSFULLY")
print("="*60)

print("""
Key Findings:

1. Females survived more than males.
2. First-class passengers had a higher survival rate.
3. Most passengers were between 20–40 years old.
4. Fare distribution is highly right-skewed.
5. Higher fare passengers generally had better survival chances.
6. Cabin column was removed due to excessive missing values.
7. Missing Age values were filled using the median.
8. Embarked missing values were filled using the mode.
""")