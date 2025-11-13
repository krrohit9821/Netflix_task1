import pandas as pd
import os

# ======================
# Step 1: Load Dataset
# ======================
file_path = "netflix_dataset .csv"  # ✅ fixed filename (no space)
if not os.path.exists(file_path):
    raise FileNotFoundError("⚠️ Please upload your Netflix CSV file and name it 'netflix_dataset.csv'")

df = pd.read_csv(file_path, low_memory=False)
print("✅ Dataset Loaded Successfully!")
print(f"Rows: {len(df)}, Columns: {len(df.columns)}")
print("-" * 50)

# ======================
# Step 2: Inspect Data
# ======================
print(" Checking Missing Values...")
print(df.isnull().sum().sort_values(ascending=False).head())

# ======================
# Step 3: Standardize Column Names
# ======================
df.columns = [col.strip().lower().replace(" ", "_").replace("-", "_") for col in df.columns]

# ======================
# Step 4: Handle Missing Values
# ======================
fill_text = ['director', 'cast', 'country', 'genres', 'description', 'listed_in']
for col in fill_text:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")

fill_numeric = ['rating', 'popularity', 'vote_count', 'vote_average', 'budget', 'revenue']
for col in fill_numeric:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())  # ✅ no inplace warning

# ======================
# Step 5: Remove Duplicates & Empty Rows
# ======================
initial_rows = len(df)
df = df.drop_duplicates()
df = df.dropna(how='all')
print(f" Removed {initial_rows - len(df)} duplicate or empty rows.")

# ======================
# Step 6: Fix Date Formats
# ======================
if 'date_added' in df.columns:
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    df['date_added'] = df['date_added'].dt.strftime("%d-%m-%Y")

# ======================
# Step 7: Convert Data Types
# ======================
if 'release_year' in df.columns:
    df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce').astype("Int64")

# ======================
# Step 8: Add Derived Columns
# ======================
if {'budget', 'revenue'}.issubset(df.columns):
    df['profit'] = df['revenue'] - df['budget']

# ======================
# Step 9: Clean Text Fields
# ======================
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype(str).str.strip()

# ======================
# Step 10: Save Cleaned Dataset
# ======================
output_file = "cleaned_netflix_dataset.csv"
df.to_csv(output_file, index=False)

# ======================
# Step 11: Generate Summary Report
# ======================
summary = {
    "Original Rows": initial_rows,
    "Cleaned Rows": len(df),
    "Total Columns": len(df.columns),
    "Duplicates Removed": initial_rows - len(df),
}

summary_text = f"""
Data Cleaning Summary
========================
Dataset: Netflix Dataset
Original Rows: {summary['Original Rows']}
Cleaned Rows: {summary['Cleaned Rows']}
Total Columns: {summary['Total Columns']}
Duplicates Removed: {summary['Duplicates Removed']}

✅ Changes Performed:
- Standardized column names
- Filled missing values ('Unknown' / median)
- Fixed date format (dd-mm-yyyy)
- Converted data types
- Removed duplicates
- Added 'profit' column
- Cleaned text formatting
"""

with open("changes_summary.txt", "w", encoding="utf-8") as f:
    f.write(summary_text.strip())

print(summary_text)
print("Cleaned dataset saved as:", output_file)
print(" Summary report saved as: changes_summary.txt")
print("-" * 50)
print(" Netflix data cleaning completed successfully!")
