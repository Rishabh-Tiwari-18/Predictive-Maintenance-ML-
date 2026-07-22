import joblib
import pandas as pd

from pathlib import Path


# Project Paths

PROJECT_ROOT = Path(__file__).resolve().parent.parent

SCALER_PATH = PROJECT_ROOT / "models" / "scaler.pkl"


# Check Scaler

if not SCALER_PATH.exists():
    raise FileNotFoundError(
        f"Scaler file not found: {SCALER_PATH}"
    )


# Load Scaler

scaler = joblib.load(SCALER_PATH)


# Clean Column Names

def clean_column_names(df):
    """
    Clean column names for consistent training and inference.
    """

    df = df.copy()

    df.columns = (
        df.columns
        .str.replace("[", "", regex=False)
        .str.replace("]", "", regex=False)
        .str.replace("<", "", regex=False)
        .str.replace(">", "", regex=False)
        .str.replace(" ", "_")
        .str.replace("/", "_")
    )

    return df


# Scale Numerical Features

def scale_features(df):
    """
    Scale numerical features using the saved scaler.
    """

    df = df.copy()

    numerical_features = [
        "Air_temperature_K",
        "Process_temperature_K",
        "Rotational_speed_rpm",
        "Torque_Nm",
        "Tool_wear_min"
    ]

    missing_columns = [
        col for col in numerical_features
        if col not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing numerical columns: {missing_columns}"
        )

    df[numerical_features] = scaler.transform(
        df[numerical_features]
    )

    return df