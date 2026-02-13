from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

model = pickle.load(open("../model/model.pkl", "rb"))

@app.get("/")
def home():
    return {"message": "Fraud Detection API Running"}

@app.get("/predict")
def predict(time: float, amount: float):


    data = np.zeros((1, 30))

    data[0][0] = time
    data[0][-1] = amount

    prediction = model.predict(data)[0]

    if prediction == 1:
        return {"prediction": "Fraud"}
    else:
        return {"prediction": "Not Fraud"}