import os
import pandas as pd


def load_clean_data():
    """
    Load all *_clean.csv files
    from local data directory.
    """

    data_path = os.path.join(
        os.getcwd(),
        "data"
    )

    files = [
        os.path.join(data_path, f)
        for f in os.listdir(data_path)
        if f.endswith("_clean.csv")
    ]

    if not files:
        raise FileNotFoundError(
            "No cleaned CSV files found in data/"
        )

    dfs = [
        pd.read_csv(f)
        for f in files
    ]

    return pd.concat(
        dfs,
        ignore_index=True
    )


def calculate_vulnerability(df):
    """
    Climate vulnerability ranking
    based on variability +
    extreme heat +
    dry day frequency.
    """

    heat_days = (
        df[
            df["T2M_MAX"] > 35
        ]
        .groupby("Country")
        .size()
    )

    dry_days = (
        df[
            df["PRECTOTCORR"] < 1
        ]
        .groupby("Country")
        .size()
    )

    summary = pd.DataFrame({
        "TempStd":
            df.groupby(
                "Country"
            )["T2M"].std(),

        "RainStd":
            df.groupby(
                "Country"
            )["PRECTOTCORR"].std(),

        "HeatDays":
            heat_days,

        "DryDays":
            dry_days

    }).fillna(0)

    summary["VulnerabilityScore"] = (
        summary["TempStd"] +
        summary["RainStd"] +
        (summary["HeatDays"] / 100) +
        (summary["DryDays"] / 100)
    )

    return summary.sort_values(
        "VulnerabilityScore",
        ascending=False
    )