import streamlit as st
import pickle
import numpy as np
import pandas as pd
 

with open("knn_model_pickle.pkl", "rb") as f:
    model = pickle.load(f)

st.title("NBA Win Percentage Prediction App")

TEAM_NAME = st.selectbox("Team Name", [
    "Wizards", "Cavaliers", "Heat", "Celtics", "Lakers"
])

TEAM_NAME = int(st.number_input("TEAM_NAME", value=0))
FG_PCT = int(st.number_input("FG_PCT", value=0))
PTS = int(st.number_input("PTS", value=0))
PLUS_MINUS = int(st.number_input("PLUS_MINUS", value=0))
EFG_PCT = int(st.number_input("EFG_PCT", value=0))


if st.button("Predict WIN %"):

    input_df = pd.DataFrame([{
        "TEAM_NAME": TEAM_NAME,
        "FG_PCT": FG_PCT,
        "PTS": PLUS_MINUS,
        "PLUS_MINUS": PLUS_MINUS,                                  
        "EFG_PCT": EFG_PCT,
    }])

    result = model.predict(input_df)[0]

    st.success(f"Predicted WIN % : {result:.2f}")