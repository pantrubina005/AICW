import pickle 
import pandas as  pd

#import the ml model
with open('D:/Insurance Premium Prediction/model/model_data.pkl', 'rb') as f:
    model = pickle.load(f)

#ML FLOW
MODEL_VERSION= '1.0.0'

def predict_output(user_input:dict):
    input_df = pd.DataFrame([user_input])
    #Predict
    output =model.predict(input_df)[0]
    return output