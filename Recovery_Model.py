import streamlit as st
import pandas as pd
import joblib
from PIL import Image

# ---------------------------
# Load Model
# ---------------------------
model = joblib.load("recovery_model.pki")

# ---------------------------
# App Banner Image
# ---------------------------
image = Image.open("Image_fx.png.jpg")
st.image(image, use_container_width=True)

# ---------------------------
# Title & Description
# ---------------------------
st.title("Farmer Recovery Status Prediction")
st.write("This app predicts whether a farmer has recovered after experiencing a shock.")

# ---------------------------
# User Inputs
# ---------------------------
age = st.number_input("Age", 18, 100)
gender = st.selectbox("Gender", ["Male", "Female"])
household = st.number_input("Household Size", 1, 20)
experience = st.number_input("Years of Experience", 0, 50)
land_size = st.number_input("Land Size (hectares)", 0.0, 20.0)
plots = st.number_input("Number of Plots", 1, 10)

irrigation = st.selectbox("Irrigation Used", ["Yes", "No"])
improved_seeds = st.selectbox("Improved Seeds Used", ["Yes", "No"])
fertilizer = st.selectbox("Fertilizer Used", ["Yes", "No"])
pests = st.selectbox("Pests or Diseases", ["Yes", "No"])

yield_kg = st.number_input("Tomato Yield (kg)", 0.0, 50000.0)
labor_cost = st.number_input("Labor Cost", 0.0)
input_cost = st.number_input("Input Cost", 0.0)

market_type = st.selectbox("Market Type", ["Local", "Urban"])
price_per_kg = st.number_input("Price per Kg", 0.0)
quantity_sold = st.number_input("Quantity Sold (kg)", 0.0)
income = st.number_input("Total Income", 0.0)

shock = st.selectbox("Shock Experienced", ["Yes", "No"])

# ---------------------------
# Encode Categorical Inputs
# ---------------------------
gender = 1 if gender == "Male" else 0
irrigation = 1 if irrigation == "Yes" else 0
improved_seeds = 1 if improved_seeds == "Yes" else 0
fertilizer = 1 if fertilizer == "Yes" else 0
pests = 1 if pests == "Yes" else 0
market_type = 1 if market_type == "Urban" else 0
shock = 1 if shock == "Yes" else 0

# ---------------------------
# Prediction
# ---------------------------
if st.button("Predict Recovery Status"):
    input_data = pd.DataFrame([[
        age,
        gender,
        household,
        experience,
        land_size,
        plots,
        irrigation,
        improved_seeds,
        fertilizer,
        yield_kg,
        pests,
        labor_cost,
        input_cost,
        market_type,
        price_per_kg,
        quantity_sold,
        income,
        shock
    ]], columns=model.feature_names_in_)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Farmer has RECOVERED")
    else:
        st.error("❌ Farmer has NOT recovered")
