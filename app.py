import gradio as gr
import joblib
import pandas as pd
import numpy as np

# Load the trained Random Forest model 
model = joblib.load("RandomForest.pkl")

# Define prediction function
def predict_car_price(Present_Price, Car_Age, Driven_kms, Fuel_Type, Selling_type, Transmission, Owner):
    # Encode categorical inputs manually (based on your training data encoding)
    fuel_diesel = 1 if Fuel_Type == "Diesel" else 0
    fuel_petrol = 1 if Fuel_Type == "Petrol" else 0
    seller_individual = 1 if Selling_type == "Individual" else 0
    transmission_manual = 1 if Transmission == "Manual" else 0

    # Prepare input for the model
    input_data = pd.DataFrame([{
        'Present_Price': Present_Price,
        'Driven_kms': Driven_kms,
        'Owner': Owner,
        'Car_Age': Car_Age,
        'Fuel_Type_Diesel': fuel_diesel,
        'Fuel_Type_Petrol': fuel_petrol,
        'Selling_type_Individual': seller_individual,
        'Transmission_Manual': transmission_manual
    }])

    # Predict
    prediction = model.predict(input_data)[0]
    return f"Estimated Selling Price: ₹ {round(prediction, 2)} lakhs"

# Create Gradio interface
interface = gr.Interface(
    fn=predict_car_price,
    inputs=[
        gr.Number(label="Present Price (in lakhs)"),
        gr.Number(label="Car Age (in years)"),
        gr.Number(label="Driven Kms"),
        gr.Radio(["Petrol", "Diesel", "CNG"], label="Fuel Type"),
        gr.Radio(["Dealer", "Individual"], label="Seller Type"),
        gr.Radio(["Manual", "Automatic"], label="Transmission"),
        gr.Number(label="Number of Previous Owners", value=0)
    ],
    outputs=gr.Textbox(label="Predicted Selling Price"),
    title="Car Price Prediction App",
    description="Predict the selling price of a used car based on its specifications."
)

# Launch the app
interface.launch()

