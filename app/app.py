import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Predictive Maintenance", layout="wide")
st.title("🛠️ Predictive Maintenance - Failure Classifier")

# Upload file
uploaded_file = st.file_uploader("📤 Upload your sensor CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    # Drop unnecessary columns
    data.drop(["UDI", "Product ID", "Failure Type"], axis=1, inplace=True, errors="ignore")

    # One-hot encode 'Type' column if present
    if "Type" in data.columns:
        data = pd.get_dummies(data, columns=["Type"], drop_first=True)

    st.write("📊 Input Data Preview", data.head())

    # Load trained model
    model = joblib.load(r"C:\Users\bilaw\OneDrive\Desktop\predictive-maintenance\models\maintenance_model.pkl")

    # Ensure correct columns (align with training)
    data = data.reindex(columns=model.feature_names_in_, fill_value=0)

    if st.button("🚀 Predict Failures"):
        preds = model.predict(data)
        st.write("🔍 Prediction Result (0 = OK, 1 = Failure):")
        st.write(preds)
