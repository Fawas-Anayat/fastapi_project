from sqlalchemy import Column , Integer , String ,Float 
from sqlalchemy.ext.declarative import declarative_base

base=declarative_base()

class user(base):

    __tablename__="user"

    name=Column(String,primary_key=True,index=True)
    email=Column(String,unique=True)
