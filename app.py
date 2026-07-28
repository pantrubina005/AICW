from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal
from typing_extensions import Annotated
import pickle
import pandas as pd
from schema.user_input import UserInput
from predict import predict_output, model, MODEL_VERSION
import uvicorn


app = FastAPI()


#Human Readable       
@app.get('/')
def home():
    return {'message':'Insurance Premium Prediction API'}

#Machine Redable/have to deploy on cloud services
@app.get('/health')
def health_check():
    return {
        'Status': 'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }
       
@app.post('/predict')
def predict_premium(data:UserInput):
    #creating new data frame
    user_input= {
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation': data.occupation
    }
    #This line to Debug
    #print(input_df.dtypes)
    try:
        prediction =predict_output(user_input)

        return JSONResponse(status_code=200, content={"Predicted_category": prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})


if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=False)
    