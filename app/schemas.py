from pydantic import BaseModel

class Userresponse(BaseModel):
    id:int
    name:str
    email:str

    class Config:    # a special inner class used to configure the pydantic models
        from_attributes=True   #it is used to directly read the ORM objects