# --------------------------------------------------
# Prodigy InfoTech Data Science Internship - Task 03
# Decision Tree Classifier
# --------------------------------------------------

# --------------------------------------------------
# 1. Import Libraries
# --------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# --------------------------------------------------
# 2. Load Dataset
# --------------------------------------------------

# Load Bank Marketing dataset
# bank.csv is present in the same Task-03 folder

df = pd.read_csv(
    r"D:\Prodigy InfoTech\tasks\task_03\bank.csv",
    sep=";"
)

print("\nDataset loaded successfully!")


# --------------------------------------------------
# 3. Display First 5 Rows
# --------------------------------------------------

print("\n" + "=" * 50)
print("FIRST 5 ROWS")
print("=" * 50)

print(df.head())


# --------------------------------------------------
# 4. Dataset Shape
# --------------------------------------------------

print("\n" + "=" * 50)
print("DATASET SHAPE")
print("=" * 50)

print(df.shape)


# --------------------------------------------------
# 5. Column Names
# --------------------------------------------------

print("\n" + "=" * 50)
print("COLUMN NAMES")
print("=" * 50)

print(df.columns.tolist())


# --------------------------------------------------
# 6. Dataset Information
# --------------------------------------------------

print("\n" + "=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

df.info()


# --------------------------------------------------
# 7. Statistical Summary
# --------------------------------------------------

print("\n" + "=" * 50)
print("STATISTICAL SUMMARY")
print("=" * 50)

print(df.describe())


# --------------------------------------------------
# 8. Check Missing Values
# --------------------------------------------------

print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)

print(df.isnull().sum())


# --------------------------------------------------
# 9. Check Duplicate Rows
# --------------------------------------------------

print("\n" + "=" * 50)
print("DUPLICATE ROWS")
print("=" * 50)

print(
    "Number of duplicate rows:",
    df.duplicated().sum()
)


# --------------------------------------------------
# 10. Remove Duplicate Rows
# --------------------------------------------------

df.drop_duplicates(
    inplace=True
)

print(
    "\nDataset shape after removing duplicates:",
    df.shape
)


# --------------------------------------------------
# 11. Convert Categorical Data
# --------------------------------------------------

# Machine Learning models require numerical data.
# LabelEncoder converts categorical text values into numbers.

label_encoder = LabelEncoder()

categorical_columns = df.select_dtypes(
    include=["object"]
).columns

print("\n" + "=" * 50)
print("CATEGORICAL COLUMNS")
print("=" * 50)

print(
    categorical_columns.tolist()
)


for column in categorical_columns:

    df[column] = label_encoder.fit_transform(
        df[column]
    )


# --------------------------------------------------
# 12. Display Data After Encoding
# --------------------------------------------------

print("\n" + "=" * 50)
print("DATA AFTER ENCODING")
print("=" * 50)

print(df.head())


# --------------------------------------------------
# 13. Separate Features and Target
# --------------------------------------------------

# X = Features
# y = Target

X = df.drop(
    "y",
    axis=1
)

y = df["y"]


print("\n" + "=" * 50)
print("FEATURES")
print("=" * 50)

print(
    X.columns.tolist()
)


print("\n" + "=" * 50)
print("TARGET")
print("=" * 50)

print(
    "Target column: y"
)


# --------------------------------------------------
# 14. Split Dataset
# --------------------------------------------------

# 80% Training Data
# 20% Testing Data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\n" + "=" * 50)
print("TRAINING AND TESTING DATA")
print("=" * 50)

print(
    "Training data shape:",
    X_train.shape
)

print(
    "Testing data shape:",
    X_test.shape
)


# --------------------------------------------------
# 15. Create Decision Tree Classifier
# --------------------------------------------------

model = DecisionTreeClassifier(
    random_state=42,
    max_depth=5
)


# --------------------------------------------------
# 16. Train the Model
# --------------------------------------------------

print(
    "\nTraining Decision Tree model..."
)

model.fit(
    X_train,
    y_train
)

print(
    "Model training completed!"
)


# --------------------------------------------------
# 17. Make Predictions
# --------------------------------------------------

y_pred = model.predict(
    X_test
)


# --------------------------------------------------
# 18. Calculate Accuracy
# --------------------------------------------------

accuracy = accuracy_score(
    y_test,
    y_pred
)


print("\n" + "=" * 50)
print("MODEL ACCURACY")
print("=" * 50)

print(
    "Accuracy:",
    accuracy
)

print(
    "Accuracy Percentage:",
    round(
        accuracy * 100,
        2
    ),
    "%"
)


# --------------------------------------------------
# 19. Classification Report
# --------------------------------------------------

print("\n" + "=" * 50)
print("CLASSIFICATION REPORT")
print("=" * 50)

print(
    classification_report(
        y_test,
        y_pred
    )
)


# --------------------------------------------------
# 20. Confusion Matrix
# --------------------------------------------------

cm = confusion_matrix(
    y_test,
    y_pred
)


print("\n" + "=" * 50)
print("CONFUSION MATRIX")
print("=" * 50)

print(cm)


# --------------------------------------------------
# 21. Save Confusion Matrix Graph
# --------------------------------------------------

plt.figure(
    figsize=(6, 5)
)

plt.imshow(
    cm,
    interpolation="nearest"
)

plt.title(
    "Confusion Matrix"
)

plt.colorbar()

plt.xlabel(
    "Predicted Label"
)

plt.ylabel(
    "Actual Label"
)

plt.xticks(
    [0, 1],
    ["No", "Yes"]
)

plt.yticks(
    [0, 1],
    ["No", "Yes"]
)


# Add values inside the confusion matrix

for i in range(
    cm.shape[0]
):

    for j in range(
        cm.shape[1]
    ):

        plt.text(
            j,
            i,
            cm[i, j],
            ha="center",
            va="center"
        )


plt.tight_layout()


# Save graph
plt.savefig(
    "confusion_matrix.png",
    dpi=300,
    bbox_inches="tight"
)


print(
    "\nConfusion Matrix saved as: confusion_matrix.png"
)


plt.show()


# --------------------------------------------------
# 22. Save Decision Tree Graph
# --------------------------------------------------

plt.figure(
    figsize=(20, 10)
)

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["No", "Yes"],
    filled=True,
    rounded=True
)

plt.title(
    "Decision Tree Classifier - Bank Marketing Dataset"
)

plt.tight_layout()


# Save graph
plt.savefig(
    "decision_tree.png",
    dpi=300,
    bbox_inches="tight"
)


print(
    "Decision Tree saved as: decision_tree.png"
)


plt.show()


# --------------------------------------------------
# 23. Final Message
# --------------------------------------------------

print("\n" + "=" * 60)

print(
    "TASK 03 COMPLETED SUCCESSFULLY!"
)

print("=" * 60)

print(
    """
The following tasks were completed:

1. Loaded Bank Marketing dataset
2. Explored the dataset
3. Checked missing values
4. Checked duplicate rows
5. Removed duplicate rows
6. Encoded categorical variables
7. Separated features and target
8. Split data into training and testing sets
9. Created Decision Tree Classifier
10. Trained the model
11. Made predictions
12. Calculated accuracy
13. Generated classification report
14. Generated confusion matrix
15. Saved confusion matrix graph
16. Saved decision tree graph

Files created:

- confusion_matrix.png
- decision_tree.png
"""
)