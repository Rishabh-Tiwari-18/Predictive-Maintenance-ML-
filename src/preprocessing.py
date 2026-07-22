import joblib
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


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


def scale_features(df):
    """
    Scale numerical features using the saved scaler.
    """

    df = df.copy()

    scaler = joblib.load(
        PROJECT_ROOT / "models" / "scaler.pkl"
    )

    numerical_features = [
        "Air_temperature_K",
        "Process_temperature_K",
        "Rotational_speed_rpm",
        "Torque_Nm",
        "Tool_wear_min"
    ]

    df[numerical_features] = scaler.transform(
        df[numerical_features]
    )

    return df