import streamlit as st
import pickle
import warnings
warnings.filterwarnings('ignore')

st.header("🚕 Ride Demand Prediction System")

price=st.number_input("Enter price per week:")
population=st.number_input("Enter population:")
income=st.number_input("Enter monthly income")
parking=st.number_input("Enter average parking per month:")
button=st.button("Predict Riders")
if button:
    model=pickle.load(open("taxi.pkl","rb"))
    res=model.predict([[price,population,income,parking]])[0]
    st.success(f"🚀 Expected Riders per Week:  {int(res)}")