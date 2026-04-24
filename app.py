import gradio as gr
import pickle
import pandas as pd
import numpy as np


with open('water_potability_model.pkl', 'rb') as f:
    model = pickle.load(f);

def predict_water_potability(ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity):
    input_df = pd.DataFrame([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]],
                            columns=['ph', 'Hardness', 'Solids', 'Chloramines', 'Sulfate', 'Conductivity', 'Organic_carbon', 'Trihalomethanes', 'Turbidity'])
    
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        return "The water is potable."
    else:
        return "The water is not potable."
    

input = [
    gr.Slider(0.0,14.0,step=0.1,label="pH",value=7.0),
    gr.Slider(0.0,350.00,step=0.1,label="Hardness",value=200.0),
    gr.Slider(0.0,70000.0,step=1.0,label="Solids",value=20000.0),
    gr.Slider(0.0, 15.0, step=0.1, label="Chloramines", value=7.0),
    gr.Slider(0.0, 500.0, step=0.1, label="Sulfate", value=330.0),
    gr.Slider(0.0, 800.0, step=0.1, label="Conductivity", value=420.0),
    gr.Slider(0.0, 30.0, step=0.1, label="Organic Carbon", value=14.0),
    gr.Slider(0.0, 130.0, step=0.1, label="Trihalomethanes", value=66.0),
    gr.Slider(0.0, 10.0, step=0.1, label="Turbidity", value=4.0)
]


output = [gr.Textbox(label="Predictions")]

demo = gr.Interface(
    fn=predict_water_potability,
    inputs=input,
    outputs=output,
    title="Water Potability Prediction",
    description="it will predict whether the water is potable or not"
)

if __name__ == "__main__":
    demo.launch()
