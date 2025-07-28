# ⚡ Electric Vehicle Data Analysis Project using Python

This project explores an electric vehicle dataset to extract insights, identify trends, and build a recommendation system.
The tasks involve data cleaning, filtering based on user needs, exploratory analysis, statistical testing, and an interactive EV recommender.

---

## 📁 Project Structure

| File | Description |
|------|-------------|
| `EV_Data_Analysis_and_Insights.ipynb` | Main notebook for data cleaning, filtering, EDA, outlier detection, and visualizations. |
| `EV_Recommender_CLASS.py` | Python class that filters EVs based on user-defined budget, range, and battery capacity. |
| `Get_EVs.ipynb` | Notebook to interactively use the `EVRecommender` class with user inputs. |
| `Hypothesis Testing.ipynb` | Statistical hypothesis testing between Tesla and Audi EVs using a two-sample t-test. |

---

## 📊 Dataset Features

The dataset includes technical and price specifications for electric vehicles:

- **Minimal price (gross) [PLN]**
- **Range (WLTP) [km]**
- **Battery capacity [kWh]**
- **Mean - Energy consumption [kWh/100 km]**
- **Engine power [KM]**
- **Car full name** and **Make (manufacturer)**

---

## 🧠 Key Tasks & Techniques

### ✅ Task 1: Customer-Focused Filtering
- Filter EVs with a **minimum range of 400 km** and **price under 350,000 PLN**.
- Group them by manufacturer (`Make`) and compute **average battery capacity**.

### ✅ Task 2: Outlier Detection
- Used **boxplots** and **Interquartile Range (IQR)** method to detect outliers in:
  - Mean Energy Consumption [kWh/100 km]

### ✅ Task 3: Correlation Analysis
- Scatter plot between **battery capacity** and **range**.
- Observed a strong **positive correlation**.

### ✅ Task 4: Recommender System
- Created `EVRecommender` class to allow users to input:
  - **Budget**
  - **Desired range**
  - **Minimum battery capacity**
- Returns a sorted list of suitable EVs.

### ✅ Task 5: Hypothesis Testing
- Performed **two-sample t-test** (`scipy.stats.ttest_ind`) to compare:
  - Mean **engine power** of **Tesla** vs **Audi**.
- Result: Identified statistically significant differences between the two manufacturers.

---

## 📌 How to Use the Project

### 1. Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn scipy 
