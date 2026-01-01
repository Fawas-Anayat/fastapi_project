from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated , Literal

app=FastAPI()
@app.get('/home')
def home():
    return {'message':'this is the first endpoint of this application'}