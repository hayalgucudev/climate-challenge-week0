# Climate Challenge – Week 0

## Project Overview
This project analyzes climate data from Ethiopia, Kenya, Nigeria, Tanzania, and Sudan to explore temperature, precipitation, and climate variability trends relevant to COP32.

## Objectives
- Clean and profile climate datasets
- Perform exploratory data analysis (EDA)
- Compare climate patterns across countries
- Generate climate vulnerability insights

## Project Structure
```text
├── .github/workflows/
├── notebooks/
├── scripts/
├── README.md
├── requirements.txt
└── .gitignore
```

## Setup Instructions

Clone the repository:

```bash
git clone https://github.com/hayalgucudev/climate-challenge-week0.git
cd climate-challenge-week0
```

Create a virtual environment:

```bash
py -m venv venv
```

Activate it (Windows):

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## CI
GitHub Actions runs a basic workflow on pushes to verify the Python environment and dependencies.

## Data Notes
- Source: NASA POWER climate data (2015–2026)
- Missing values such as `-999` are handled during preprocessing
- Data files and cleaned CSVs are excluded from Git

## Author
Remetula Ali