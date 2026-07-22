import pandas as pd


def create_features(df):
    """
    Create engineered features used during model training.
    """

    df = df.copy()

    # Temperature Difference

    df["Temperature_Difference"] = (
        df["Process_temperature_K"]
        - df["Air_temperature_K"]
    )

    # Machine Power

    df["Machine_Power"] = (
        df["Torque_Nm"]
        * df["Rotational_speed_rpm"]
    )

    # Wear Rate

    df["Wear_Rate"] = (
        df["Tool_wear_min"]
        / (df["Rotational_speed_rpm"] + 1)
    )

    # Heat Index

    df["Heat_Index"] = (
        df["Air_temperature_K"]
        * df["Process_temperature_K"]
    )

    # Mechanical Stress

    df["Mechanical_Stress"] = (
        df["Torque_Nm"]
        * df["Tool_wear_min"]
    )

    # Temperature Ratio

    df["Temperature_Ratio"] = (
        df["Process_temperature_K"]
        / (df["Air_temperature_K"] + 1e-6)
    )

    # RPM per Torque

    df["RPM_per_Torque"] = (
        df["Rotational_speed_rpm"]
        / (df["Torque_Nm"] + 1)
    )

    # Power per Wear

    df["Power_per_Wear"] = (
        df["Machine_Power"]
        / (df["Tool_wear_min"] + 1)
    )

    # Torque per Temperature

    df["Torque_per_Temp"] = (
        df["Torque_Nm"]
        / (df["Process_temperature_K"] + 1)
    )

    # Wear × Temperature

    df["Wear_Temp_Product"] = (
        df["Tool_wear_min"]
        * df["Process_temperature_K"]
    )

    return df