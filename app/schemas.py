from pydantic import BaseModel

class Userresponse(BaseModel):
    id:int
    name:str
    email:str

    class config:
        from_attributes=True