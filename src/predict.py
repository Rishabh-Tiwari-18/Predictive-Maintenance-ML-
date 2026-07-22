import pandas as pd
import joblib

from pathlib import Path


from src.preprocessing import clean_column_names, scale_features
from src.feature_engineering import create_features



PROJECT_ROOT = Path(__file__).resolve().parent.parent

MODEL_DIR = PROJECT_ROOT / "models"



# Load trained model

model = joblib.load(
    MODEL_DIR / "Best_Model.pkl"
)



# Load feature names used during training

feature_names = joblib.load(
    MODEL_DIR / "feature_names.pkl"
)



def prepare_input(df):

    df = df.copy()


    # Clean column names

    df = clean_column_names(df)



    # Create engineered features

    df = create_features(df)



    # Encode Type column

    if "Type" in df.columns:

        df = pd.get_dummies(
            df,
            columns=["Type"],
            drop_first=False
        )



    # Add missing columns

    for col in feature_names:

        if col not in df.columns:

            df[col] = 0



    # Remove unwanted columns

    df = df[feature_names]



    # Scale numerical columns

    df = scale_features(df)



    return df




def predict_failure(df):


    processed_df = prepare_input(
        df
    )



    prediction = model.predict(
        processed_df
    )[0]



    probability = model.predict_proba(
        processed_df
    )[0][1]



    return prediction, probability