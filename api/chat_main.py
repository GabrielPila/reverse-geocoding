from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
import joblib
#from api import model, tfidf
from utils.utils import get_prediction_from_text

app = FastAPI()

model = joblib.load('../model/model.joblib')
tfidf = joblib.load('../model/tfidf.joblib')

class Message(BaseModel):
    message: str


@app.get("/")
def get_root():
    return {"message": "Welcome to the chat urgency predictor"}


@app.get("/predict")
def predict(text: Message):

    print(text)
    text_dict = text.dict()
    msg = text_dict['message']

#    prediction = get_prediction(request, model, tfidf)
    prediction = get_prediction_from_text(msg, model, tfidf)

    return {'prediction': prediction}