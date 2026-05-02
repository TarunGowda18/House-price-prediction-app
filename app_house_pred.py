import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="House Price Predictor", page_icon="🏠", layout="centered")

# load model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# header
st.title("🏠 House Price Prediction App")
st.caption("Enter property details to estimate the price")

st.divider()

# input section (no sidebar)
col1, col2 = st.columns(2)

with col1:
    sqft = st.number_input("Square Footage", 500, 5000, 2000)
    beds = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
    baths = st.selectbox("Bathrooms", [1, 2, 3])

with col2:
    year = st.number_input("Year Built", 1950, 2025, 2000)
    lot = st.number_input("Lot Size", 0.5, 5.0, 2.5)
    garage = st.selectbox("Garage Size", [0, 1, 2])
    quality = st.slider("Neighborhood Quality", 1, 10, 5)

# warning
if sqft < 800:
    st.warning("Low square footage may reduce price.")

st.divider()

# input summary
st.subheader("Input Summary")

input_df = pd.DataFrame({
    "Feature": ["Square Footage", "Bedrooms", "Bathrooms", "Year Built",
                "Lot Size", "Garage Size", "Neighborhood Quality"],
    "Value": [sqft, beds, baths, year, lot, garage, quality]
})

st.dataframe(input_df, use_container_width=True)

st.divider()

# prediction
if st.button("Predict Price", use_container_width=True):

    input_data = pd.DataFrame({
        "Square_Footage": [sqft],
        "Num_Bedrooms": [beds],
        "Num_Bathrooms": [baths],
        "Year_Built": [year],
        "Lot_Size": [lot],
        "Garage_Size": [garage],
        "Neighborhood_Quality": [quality]
    })

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    st.subheader("Prediction Result")

    st.metric("Estimated Price", f"₹ {prediction:,.2f}")

    error_margin = prediction * 0.1
    st.write(f"Estimated Range: ₹ {prediction - error_margin:,.0f} - ₹ {prediction + error_margin:,.0f}")

    if prediction > 800000:
        st.success("Premium Property")
    elif prediction > 400000:
        st.info("Mid-range Property")
    else:
        st.warning("Budget Property")

    report = pd.DataFrame({"Predicted Price": [prediction]})

    st.download_button(
        "Download Prediction",
        report.to_csv(index=False),
        "prediction.csv"
    )

st.divider()
st.caption("Built using Machine Learning | Linear Regression")