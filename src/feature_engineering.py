def create_features(df):

    df = df.copy()

    df["Temperature_Difference"] = (
        df["Process_temperature_K"]
        - df["Air_temperature_K"]
    )

    df["Machine_Power"] = (
        df["Torque_Nm"]
        * df["Rotational_speed_rpm"]
    )

    df["Wear_Rate"] = (
        df["Tool_wear_min"]
        / (df["Rotational_speed_rpm"] + 1)
    )

    df["Heat_Index"] = (
        df["Air_temperature_K"]
        * df["Process_temperature_K"]
    )

    df["Mechanical_Stress"] = (
        df["Torque_Nm"]
        * df["Tool_wear_min"]
    )

    df["Temperature_Ratio"] = (
        df["Process_temperature_K"]
        / df["Air_temperature_K"]
    )

    df["RPM_per_Torque"] = (
        df["Rotational_speed_rpm"]
        / (df["Torque_Nm"] + 1)
    )

    return df