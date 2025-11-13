# 🎬 Netflix Data Cleaning & Preprocessing Project  
**Data Analyst Internship — Task 1**

---

## 🎯 Objective  
Clean and prepare a raw **Netflix Movies & TV Shows** dataset for analysis by handling:  
- Missing values  
- Duplicate records  
- Inconsistent date and text formats  
- Wrong data types  

This project follows all the required steps from the internship **Task 1 – Data Cleaning and Preprocessing**.

---

## 🧰 Tools & Libraries  
- **Language:** Python 3  
- **Libraries:** pandas, os  
- **Environment:** VS Code / Jupyter Notebook  

---

## 📂 Dataset Details  
- **File Used:** `netflix_dataset.csv`  
- **Rows Before Cleaning:** *depends on dataset (e.g. 16000)*  
- **Columns:** (e.g. 18 original columns)  
- **Dataset Source:** Netflix Movies & TV Shows data (from Kaggle / provided internship file)

---

## 🧹 Steps Performed  

### 🪣 1. Load Dataset  
Loaded the raw Netflix CSV file using pandas and checked its structure and missing values.  

### 🧩 2. Standardize Column Names  
Converted all column names to lowercase and replaced spaces with underscores.  
Example: `Date Added` → `date_added`

### 🧱 3. Handle Missing Values  
- Text columns (`director`, `cast`, `country`, `genres`, `description`, `listed_in`) → replaced with **"Unknown"**  
- Numeric columns (`rating`, `popularity`, `vote_count`, `vote_average`, `budget`, `revenue`) → filled using **median**  

### 🔁 4. Remove Duplicates & Empty Rows  
Dropped all duplicate records and completely empty rows (if any).

### 📅 5. Fix Date Formats  
Converted `date_added` into a consistent **`dd-mm-yyyy`** format using pandas datetime.

### 🔢 6. Convert Data Types  
Ensured numeric columns are stored as integers and strings are trimmed and cleaned.

### 💰 7. Add Derived Columns  
Created a new column **`profit` = `revenue` − `budget`** for further financial analysis.

### 🧼 8. Clean Text Fields  
Removed extra spaces and standardized all string fields for uniformity.

---

## 📊 After Cleaning  

| Metric | Count |
|:--|--:|
| Original Rows | 16 000 (example) |
| Duplicates Removed | 0 |
| Empty Rows Dropped | 0 |
| Final Rows | 16 000 |
| Final Columns | 19 |

