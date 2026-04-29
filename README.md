# Climate Challenge – Week 0

## Project Overview
This project analyzes climate data from Ethiopia, Kenya, Nigeria, Tanzania, and Sudan using NASA POWER data (2015–2026) to identify climate trends, assess vulnerability, and generate insights relevant to COP32.

## Objectives
- Perform data profiling and cleaning on climate datasets
- Conduct exploratory data analysis (EDA)
- Compare climate trends across countries
- Generate climate vulnerability insights
- Develop an interactive dashboard for visualization

---

# Task 1: Git and Environment Setup

Completed:
- Created GitHub repository: climate-challenge-week0
- Set up Python virtual environment
- Added `.gitignore`
- Generated `requirements.txt`
- Configured GitHub Actions CI workflow
- Used branching and pull request workflow
- Documented environment setup in README

## Setup Instructions

Clone repository:

```bash
git clone https://github.com/hayalgucudev/climate-challenge-week0.git
cd climate-challenge-week0
```

Create virtual environment:

```bash
py -m venv venv
```

Activate environment (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## CI
GitHub Actions validates Python dependencies on pushes to `main`.

---

# Task 2: Data Profiling, Cleaning and EDA

Completed:
- Loaded climate data for five countries
- Converted YEAR and DOY to datetime
- Added country and month features
- Replaced NASA `-999` sentinel values
- Handled missing values and duplicates
- Detected outliers using Z-score
- Exported cleaned datasets
- Produced:
  - Temperature trend analysis
  - Precipitation analysis
  - Correlation analysis
  - Distribution analysis

Country notebooks completed:
- Ethiopia EDA
- Kenya EDA
- Nigeria EDA
- Tanzania EDA
- Sudan EDA

---

# Task 3: Cross-Country Comparison and Vulnerability Ranking

Completed:
- Combined all five cleaned datasets
- Compared temperature trends
- Compared precipitation variability
- Analyzed extreme heat events
- Analyzed dry-day frequency
- Performed statistical testing
- Produced climate vulnerability ranking
- Documented COP32-focused findings

Key outputs:
- Temperature comparison plots
- Precipitation boxplots
- Extreme-event analysis
- Vulnerability ranking table

---

# Bonus: Interactive Dashboard

Completed:
- Built Streamlit dashboard

Features:
- Country selector
- Year range filter
- Variable selector
- Interactive trend visualization
- Precipitation distribution visualization

---

## Project Structure

```text
├── .github/workflows/
├── notebooks/
├── app/
├── scripts/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Data Notes
- Source: NASA POWER climate data (2015–2026)
- Missing values such as `-999` handled during preprocessing
- Raw and cleaned data excluded from Git

## Author
Remetula Ali