import streamlit as st
import requests

st.set_page_config(page_title="Black Friday Sales Predictor", page_icon="🛍️")

st.title("🛍️ Black Friday Purchase Predictor")
st.markdown("Enter customer details to predict their purchase amount.")

# --- INPUT UI ---
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["M", "F"])
    age = st.selectbox("Age Group", ["0-17", "18-25", "26-35", "36-45", "46-50", "51-55", "55+"])
    occupation = st.number_input("Occupation Code (0-20)", min_value=0, max_value=20, value=10)
    city = st.selectbox("City Category", ["A", "B", "C"])

with col2:
    stay = st.selectbox("Years in City", ["0", "1", "2", "3", "4+"])
    marital = st.selectbox("Marital Status", [0, 1], format_func=lambda x: "Married" if x == 1 else "Single")
    cat1 = st.number_input("Product Category 1", min_value=1, max_value=20, value=1)
    cat2 = st.number_input("Product Category 2", min_value=0, max_value=20, value=0)
    cat3 = st.number_input("Product Category 3", min_value=0, max_value=20, value=0)

# --- PREDICTION LOGIC ---
if st.button("Predict Purchase Amount", type="primary"):
    # Prepare the data to match your API's expected JSON
    payload = {
        "Gender": gender,
        "Age": age,
        "Occupation": occupation,
        "City_Category": city,
        "Stay_In_Current_City_Years": stay,
        "Marital_Status": marital,
        "Product_Category_1": cat1,
        "Product_Category_2": float(cat2),
        "Product_Category_3": float(cat3)
    }

    try:
        # Send request to your FastAPI server
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        
        if response.status_code == 200:
            result = response.json()
            st.success(f"### Predicted Purchase: ${result['predicted_purchase']:,}")
            st.balloons()
        else:
            st.error(f"Error: {response.text}")
            
    except Exception as e:
        st.error(f"Could not connect to API. Is FastAPI running? \n({e})")
