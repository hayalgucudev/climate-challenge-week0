import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils import (
    load_clean_data,
    calculate_vulnerability
)

# ---------------------------------
# Page config
# ---------------------------------
st.set_page_config(
    page_title="Climate Dashboard",
    layout="wide"
)

st.title("🌍 African Climate Dashboard")
st.write(
    "Interactive dashboard for cross-country climate comparison."
)

# ---------------------------------
# Load data
# ---------------------------------
@st.cache_data
def cached_load():
    return load_clean_data()

df = cached_load()

# ---------------------------------
# Sidebar Filters
# ---------------------------------
st.sidebar.header("Filters")

countries = sorted(
    df["Country"].dropna().unique()
)

selected_countries = st.sidebar.multiselect(
    "Select Countries",
    countries,
    default=countries
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)

df = df[
    df["Country"].isin(
        selected_countries
    )
]

# ---------------------------------
# Date Handling
# ---------------------------------
df["DATE"] = pd.to_datetime(
    df["YEAR"] * 1000 + df["DOY"],
    format="%Y%j"
)

min_year = int(
    df["YEAR"].min()
)

max_year = int(
    df["YEAR"].max()
)

year_range = st.sidebar.slider(
    "Year Range",
    min_year,
    max_year,
    (min_year, max_year)
)

df = df[
    (df["YEAR"] >= year_range[0]) &
    (df["YEAR"] <= year_range[1])
]

# ---------------------------------
# KPI Cards
# ---------------------------------
st.subheader("📌 Climate KPIs")

col1, col2, col3 = st.columns(3)

avg_temp = df["T2M"].mean()
avg_rain = df["PRECTOTCORR"].mean()
extreme_heat_days = (
    df["T2M_MAX"] > 35
).sum()

col1.metric(
    "Avg Temperature (°C)",
    f"{avg_temp:.2f}"
)

col2.metric(
    "Avg Precipitation",
    f"{avg_rain:.2f}"
)

col3.metric(
    "Extreme Heat Days",
    f"{extreme_heat_days:,}"
)

# ---------------------------------
# Trend Line
# ---------------------------------
st.subheader(
    f"📈 {variable} Trend"
)

trend = (
    df.groupby(
        ["YEAR", "Country"]
    )[variable]
      .mean()
      .reset_index()
)

st.line_chart(
    trend.pivot(
        index="YEAR",
        columns="Country",
        values=variable
    )
)

# ---------------------------------
# Precipitation Boxplot
# ---------------------------------
st.subheader(
    "🌧️ Precipitation Distribution (Boxplot)"
)

fig, ax = plt.subplots()

df.boxplot(
    column="PRECTOTCORR",
    by="Country",
    ax=ax
)

plt.suptitle("")
ax.set_title(
    "PRECTOTCORR by Country"
)

st.pyplot(fig)

# ---------------------------------
# Vulnerability Ranking
# ---------------------------------
st.subheader(
    "⚠ Climate Vulnerability Ranking"
)

ranking = calculate_vulnerability(df)

st.dataframe(ranking)

most_vulnerable = ranking.index[0]

st.info(
    f"{most_vulnerable} currently ranks highest "
    "based on climate variability, extreme heat, "
    "and dry-day frequency."
)

# ---------------------------------
# Data Preview
# ---------------------------------
st.subheader(
    "📊 Data Preview"
)

st.dataframe(
    df.head(50)
)