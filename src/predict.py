import joblib
import pandas as pd

from pathlib import Path

import traceback

try:
    import joblib
except Exception:
    raise Exception(traceback.format_exc())

import pandas as pd

from pathlib import Path

from src.preprocessing import clean_column_names, scale_features
from src.feature_engineering import create_features


# Project Paths

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_DIR = PROJECT_ROOT / "models"

MODEL_PATH = MODEL_DIR / "best_model.pkl"
FEATURE_PATH = MODEL_DIR / "feature_names.pkl"


# Check Files

if not MODEL_PATH.exists():
    raise FileNotFoundError(
        f"Model file not found: {MODEL_PATH}"
    )

if not FEATURE_PATH.exists():
    raise FileNotFoundError(
        f"Feature names file not found: {FEATURE_PATH}"
    )


# Load Model

model = joblib.load(MODEL_PATH)

feature_names = joblib.load(FEATURE_PATH)


# Prepare Input

def prepare_input(df):

    df = df.copy()

    # Clean column names
    df = clean_column_names(df)

    # Feature Engineering
    df = create_features(df)

    # One-Hot Encoding
    if "Type" in df.columns:
        df = pd.get_dummies(
            df,
            columns=["Type"],
            drop_first=False
        )

    # Add Missing Columns
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0

    # Arrange Columns
    df = df[feature_names]

    # Scale Numerical Features
    df = scale_features(df)

    return df


# Prediction Function

def predict_failure(df):

    processed_df = prepare_input(df)

    prediction = model.predict(processed_df)[0]

    probability = model.predict_proba(processed_df)[0][1]

    return prediction, probability