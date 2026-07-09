# -----------------------------
# Prodigy InfoTech _ Data Science Internship
# TASK:01 Data Visualization
# -----------------------------
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv(
    "API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv",
    skiprows=4
)

# Remove the empty column
df = df.drop(columns=["Unnamed: 69"])

# Display first 5 rows
print(df.head())

# Display column names
print(df.columns)

# Keep only required columns
population_df = df[["Country Name", "2024"]]

# Remove rows where population is missing
population_df = population_df.dropna()

# Convert population column to numeric
population_df["2024"] = pd.to_numeric(population_df["2024"])

# Sort by population in descending order
top10 = population_df.sort_values(by="2024", ascending=False).head(10)

# -----------------------------
# Bar Chart
# -----------------------------
plt.figure(figsize=(12,6))

plt.bar(
    top10["Country Name"],
    top10["2024"],
    color="steelblue",
    edgecolor="black"
)

plt.title("Top 10 Most Populated Countries (2024)")
plt.xlabel("Country")
plt.ylabel("Population")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("bar_chart.png")
plt.show()

# -----------------------------
# Histogram
# -----------------------------
plt.figure(figsize=(10,6))

plt.hist(
    population_df["2024"],
    bins=20,
    color="orange",
    edgecolor="black"
)

plt.title("Distribution of Population (2024)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")

plt.tight_layout()

plt.savefig("histogram.png")
plt.show()
