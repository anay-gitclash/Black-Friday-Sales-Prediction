from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from catboost import CatBoostRegressor

app = FastAPI(title="Black Friday Sales API")

# Load model
model = CatBoostRegressor()
model.load_model("model/catboost_model.cbm")

class PurchaseInput(BaseModel):
    Gender: str
    Age: str
    Occupation: int
    Stay_In_Current_City_Years: str
    Marital_Status: int
    Product_Category_1: int
    Product_Category_2: float = 0.0
    Product_Category_3: float = 0.0
    City_Category: str

# Mappings
gender_map = {'F': 0, 'M': 1}
age_map = {'0-17': 0, '18-25': 1, '26-35': 2, '36-45': 3, '46-50': 4, '51-55': 5, '55+': 6}
city_map = {'A': 0, 'B': 1, 'C': 2}
stay_map = {'0': 0, '1': 1, '2': 2, '3': 3, '4+': 4}

@app.post("/predict")
def predict_purchase(data: PurchaseInput):
    input_data = data.dict()

    # 1. Standard Encodings
    input_data['Gender'] = gender_map.get(input_data['Gender'], 0)
    input_data['Age'] = age_map.get(input_data['Age'], 2)
    input_data['Stay_In_Current_City_Years'] = stay_map.get(input_data['Stay_In_Current_City_Years'], 1)

    # 2. ONE-HOT ENCODING FIX for City_Category
    # We create the 'A', 'B', and 'C' columns the model expects
    input_data['A'] = 1 if data.City_Category == "A" else 0
    input_data['B'] = 1 if data.City_Category == "B" else 0
    input_data['C'] = 1 if data.City_Category == "C" else 0

    input_df = pd.DataFrame([input_data])

    # 3. THE RECONSTRUCTED ORDER
    # Based on your error: Position 8 is 'B'. 
    # Usually, get_dummies puts them in alphabetical order at the end.
    training_order = [
        "Gender", 
        "Age", 
        "Occupation", 
        "Stay_In_Current_City_Years", 
        "Marital_Status", 
        "Product_Category_1", 
        "Product_Category_2", 
        "Product_Category_3",
        "A", "B", "C"  # The model sees these as separate features
    ]
    
    input_df = input_df[training_order]

    prediction = model.predict(input_df)[0]

    return {
        "predicted_purchase": round(float(max(0, prediction)), 2)
    }
