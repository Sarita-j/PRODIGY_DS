# ============================================================
# PRODIGY INFOTECH - DATA SCIENCE INTERNSHIP
# TASK 04: SENTIMENT ANALYSIS AND VISUALIZATION
# ============================================================

# -----------------------------
# 1. IMPORT LIBRARIES
# -----------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import os


# -----------------------------
# 2. CREATE OUTPUT FOLDER
# -----------------------------

output_folder = "outputs"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


# -----------------------------
# 3. LOAD DATASET
# -----------------------------

file_path = "twitter_training.csv"

df = pd.read_csv(
    file_path,
    header=None
)

print("\nDataset loaded successfully!")


# -----------------------------
# 4. DISPLAY BASIC INFORMATION
# -----------------------------

print("\nFirst 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nDataset Information:")
print(df.info())


# -----------------------------
# 5. RENAME COLUMNS
# -----------------------------

df.columns = [
    "ID",
    "Entity",
    "Sentiment",
    "Text"
]

print("\nColumns renamed successfully!")

print(df.head())


# -----------------------------
# 6. CHECK MISSING VALUES
# -----------------------------

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


# -----------------------------
# 7. REMOVE MISSING VALUES
# -----------------------------

df = df.dropna()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# -----------------------------
# 8. REMOVE DUPLICATE ROWS
# -----------------------------

print("\nDuplicate Rows Before Removing:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDuplicate Rows After Removing:")
print(df.duplicated().sum())


# -----------------------------
# 9. CLEAN TEXT DATA
# -----------------------------

def clean_text(text):

    # Convert text to string
    text = str(text)

    # Convert to lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)

    # Remove mentions
    text = re.sub(r"@\w+", "", text)

    # Remove hashtags symbol
    text = re.sub(r"#", "", text)

    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


df["Clean_Text"] = df["Text"].apply(clean_text)


print("\nText cleaning completed!")

print("\nOriginal Text:")
print(df["Text"].head())

print("\nCleaned Text:")
print(df["Clean_Text"].head())


# -----------------------------
# 10. CHECK SENTIMENT VALUES
# -----------------------------

print("\nUnique Sentiments:")
print(df["Sentiment"].unique())

print("\nSentiment Counts:")
print(df["Sentiment"].value_counts())


# -----------------------------
# 11. SENTIMENT DISTRIBUTION
# -----------------------------

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x="Sentiment",
    order=df["Sentiment"].value_counts().index
)

plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Tweets")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "sentiment_distribution.png"
    ),
    dpi=300
)

plt.show()


# -----------------------------
# 12. SENTIMENT PIE CHART
# -----------------------------

sentiment_counts = df["Sentiment"].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    sentiment_counts,
    labels=sentiment_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sentiment Distribution Percentage")

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "sentiment_pie_chart.png"
    ),
    dpi=300
)

plt.show()


# -----------------------------
# 13. TOP 10 ENTITIES
# -----------------------------

top_entities = df["Entity"].value_counts().head(10)

print("\nTop 10 Entities:")
print(top_entities)


# -----------------------------
# 14. TOP 10 ENTITIES BAR CHART
# -----------------------------

plt.figure(figsize=(12, 6))

sns.barplot(
    x=top_entities.values,
    y=top_entities.index
)

plt.title("Top 10 Most Mentioned Entities")

plt.xlabel("Number of Tweets")

plt.ylabel("Entity")

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "top_10_entities.png"
    ),
    dpi=300
)

plt.show()


# -----------------------------
# 15. SENTIMENT BY ENTITY
# -----------------------------

top_entity_names = top_entities.index

entity_sentiment = df[
    df["Entity"].isin(top_entity_names)
]


plt.figure(figsize=(14, 8))

sns.countplot(
    data=entity_sentiment,
    y="Entity",
    hue="Sentiment",
    order=top_entity_names
)

plt.title(
    "Sentiment Distribution Across Top 10 Entities"
)

plt.xlabel("Number of Tweets")

plt.ylabel("Entity")

plt.legend(
    title="Sentiment",
    bbox_to_anchor=(1.05, 1),
    loc="upper left"
)

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "sentiment_by_entity.png"
    ),
    dpi=300
)

plt.show()


# -----------------------------
# 16. TEXT LENGTH ANALYSIS
# -----------------------------

df["Text_Length"] = df["Clean_Text"].str.len()


print("\nText Length Statistics:")
print(df["Text_Length"].describe())


# -----------------------------
# 17. TEXT LENGTH HISTOGRAM
# -----------------------------

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x="Text_Length",
    bins=30,
    kde=True
)

plt.title("Distribution of Tweet Text Length")

plt.xlabel("Text Length")

plt.ylabel("Number of Tweets")

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "text_length_distribution.png"
    ),
    dpi=300
)

plt.show()


# -----------------------------
# 18. TEXT LENGTH BY SENTIMENT
# -----------------------------

plt.figure(figsize=(10, 6))

sns.boxplot(
    data=df,
    x="Sentiment",
    y="Text_Length"
)

plt.title("Tweet Text Length by Sentiment")

plt.xlabel("Sentiment")

plt.ylabel("Text Length")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "text_length_by_sentiment.png"
    ),
    dpi=300
)

plt.show()


# -----------------------------
# 19. SENTIMENT AND ENTITY HEATMAP
# -----------------------------

sentiment_entity_table = pd.crosstab(
    df[df["Entity"].isin(top_entity_names)]["Entity"],
    df[df["Entity"].isin(top_entity_names)]["Sentiment"]
)


plt.figure(figsize=(12, 8))

sns.heatmap(
    sentiment_entity_table,
    annot=True,
    fmt="d"
)

plt.title(
    "Sentiment Distribution Across Top 10 Entities"
)

plt.xlabel("Sentiment")

plt.ylabel("Entity")

plt.tight_layout()

plt.savefig(
    os.path.join(
        output_folder,
        "sentiment_entity_heatmap.png"
    ),
    dpi=300
)

plt.show()


# -----------------------------
# 20. SAVE CLEANED DATASET
# -----------------------------

cleaned_file = os.path.join(
    output_folder,
    "cleaned_twitter_data.csv"
)

df.to_csv(
    cleaned_file,
    index=False
)


# -----------------------------
# 21. FINAL SUMMARY
# -----------------------------

print("\n======================================")
print("TASK 04 COMPLETED SUCCESSFULLY!")
print("======================================")

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nFinal Sentiment Distribution:")
print(df["Sentiment"].value_counts())

print("\nTop 10 Entities:")
print(top_entities)

print("\nAll graphs have been saved inside:")
print("outputs/")

print("\nCleaned dataset saved as:")
print("outputs/cleaned_twitter_data.csv")