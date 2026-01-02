from fastapi import FastAPI
from pydantic import BaseModel
from typing import Annotated , Literal
from db import session , engine
import database_models

app=FastAPI()

database_models.base.metadata.create_all(bind=engine)

dummy_users = [
    database_models.user(name="Ali Khan", email="ali.khan@example.com"),
    database_models.user(name= "Sara Ahmed", email= "sara.ahmed@example.com"),
    database_models.user(name= "Usman Iqbal", email= "usman.iqbal@example.com"),
    database_models.user(name= "Zara Malik", email= "zara.malik@example.com"),
    database_models.user(name= "Bilal Raza", email= "bilal.raza@example.com")
]

def init_db():
    db=session()
    
    for user in dummy_users:
        db.add(user)

    db.commit()
    db.close()

init_db()

@app.get('/home')
def home():
    return {'message':'this is the first endpoint of this application'}


@app.get('users')
def users():
    db=session()