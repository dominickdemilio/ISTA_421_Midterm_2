import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report  # for precision & recall

"""
Step 6: Choose Algorithm

In this step, I chose to use Random Forest as the algorithm for classification of facility performance. 
It is robust, allows for handling of missing values, and is less prone to overfitting as some or the 
other algorithms discussed in chapters 5-8 of the ISLP. The board would like this model because it 
identifies specific metrics (features) that have a strong correlation with facilities consistently
underperforming.
"""

# Load the dataset
filename = "dataset.csv"
df = pd.read_csv(filename, low_memory=False)

# Clean the dataset
numeric_cols = [
    "Number of Discharges",
    "Footnote",
    "Excess Readmission Ratio",
    "Predicted Readmission Rate",
    "Expected Readmission Rate",
    "Number of Readmissions",
]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["Start Date"] = pd.to_datetime(df["Start Date"], errors="coerce")
df["End Date"] = pd.to_datetime(df["End Date"], errors="coerce")

# Filter out columns where "Excess Readmission Ratio" is null
df = df[~df["Excess Readmission Ratio"].isnull()].copy()

# Gauge facility perfomance
# Label facility as over-performing (0) or under-performing (1) based on the Excess Readmission Ratiol
df["Performance"] = (df["Excess Readmission Ratio"] > 1).astype(int)

# Combine multiple measures into a single calculation
# Since hospitals have multiple measures/operations, we need to aggregate them so we have one row per hospital
hospital_df = (
    df.groupby(["Facility Name", "Facility ID", "State"])
    .agg(
        {
            "Excess Readmission Ratio": "median",
            "Predicted Readmission Rate": "median",
            "Expected Readmission Rate": "median",
            "Number of Discharges": "median",
            "Performance": "mean",  # average proportion (from 0 to 1) of underperforming measures (basically a fraction)
        }
    )
    .reset_index()
)

# If >50% of measures are underperforming, classify the facility as underperforming (1). Else, overperforming (0)
hospital_df["Final_Performance"] = (hospital_df["Performance"] >= 0.5).astype(
    int
)

# Features that contribute to performance metrics:
features = [
    "Excess Readmission Ratio",
    "Predicted Readmission Rate",
    "Expected Readmission Rate",
    "Number of Discharges",
]
target_var = "Final_Performance"
hospital_df = hospital_df.dropna(
    subset=features + [target_var]
)  # Remove rows with missing data
X = hospital_df[features]
y = hospital_df[target_var]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Build/train the random forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test the model on the test set
y_pred = model.predict(X_test)

# Use scikit to create a classification report for my model
# Get valuable metrics like precision, recall, and model accuracy
print(classification_report(y_test, y_pred))
