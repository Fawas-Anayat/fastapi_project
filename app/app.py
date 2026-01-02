from fastapi import FastAPI
from db import session, engine
import database_models
from schemas import Userresponse

app = FastAPI()

database_models.base.metadata.create_all(bind=engine)

def init_db():
    db = session()

    if db.query(database_models.user).first() is None:
        users = [
            database_models.User(name="Usman Khan", email="usman@example.com"),
            database_models.User(name="Ali Khan", email="ali.khan@example.com"),
            database_models.User(name="Sara Ahmed", email="sara.ahmed@example.com"),
        ]
        db.add_all(users)
        db.commit()

    db.close()

init_db()

@app.get("/")
def root():
    return {"message": "FastAPI is running"}

@app.get("/home")
def home():
    return {"message": "This is the first endpoint of this application"}

@app.get("/users",response_model=list[Userresponse])
def get_users():
    db = session()
    users = db.query(database_models.user).all()
    db.close()
    return users
