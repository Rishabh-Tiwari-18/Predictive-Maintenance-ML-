import streamlit as st
import pandas as pd
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))


PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.append(
    str(PROJECT_ROOT)
)


from src.predict import predict_failure



st.set_page_config(
    page_title="Predictive Maintenance",
    page_icon="⚙️",
    layout="centered"
)



st.title(
    "⚙️ Predictive Maintenance System"
)


st.write(
    "Machine Failure Prediction using Machine Learning"
)



machine_type = st.selectbox(
    "Machine Type",
    ["L","M","H"]
)


air_temp = st.number_input(
    "Air Temperature (K)",
    value=300.0
)


process_temp = st.number_input(
    "Process Temperature (K)",
    value=310.0
)


rpm = st.number_input(
    "Rotational Speed (rpm)",
    value=1500
)


torque = st.number_input(
    "Torque (Nm)",
    value=45.0
)


wear = st.number_input(
    "Tool Wear (min)",
    value=120
)



twf = st.selectbox(
    "Tool Wear Failure",
    [0,1]
)


hdf = st.selectbox(
    "Heat Dissipation Failure",
    [0,1]
)


pwf = st.selectbox(
    "Power Failure",
    [0,1]
)


osf = st.selectbox(
    "Overstrain Failure",
    [0,1]
)


rnf = st.selectbox(
    "Random Failure",
    [0,1]
)



if st.button("Predict Failure"):


    input_data = pd.DataFrame({

        "Type":[machine_type],

        "Air temperature [K]":[air_temp],

        "Process temperature [K]":[process_temp],

        "Rotational speed [rpm]":[rpm],

        "Torque [Nm]":[torque],

        "Tool wear [min]":[wear],

        "TWF":[twf],

        "HDF":[hdf],

        "PWF":[pwf],

        "OSF":[osf],

        "RNF":[rnf]

    })


    prediction, probability = predict_failure(
        input_data
    )


    probability = probability * 100



    if prediction == 1:

        st.error(
            "⚠️ Machine Failure Detected"
        )

    else:

        st.success(
            "✅ Machine Operating Normally"
        )


    st.metric(
        "Failure Probability",
        f"{probability:.2f}%"
    )