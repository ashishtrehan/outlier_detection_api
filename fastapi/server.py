import io
from starlette.responses import Response
from fastapi import FastAPI, File
from pydantic import BaseModel
from typing import Any, Dict, AnyStr, List, Union



class Sentence(BaseModel):
    text: str

class Contact(BaseModel):
    contact_id:int
    first_name:str
    last_name:str
    user_name:str
    password:str


app = FastAPI(
    title="Outlier Detection",
    description="""Pass Outlier Data and return Outliers""",
    version="0.1.0",
)
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post('/lowercase')
def lower_case(sentence: Sentence):
    return {'text': sentence.text.lower()}

@app.post('/contact')
async def create_contact(contact: Contact):
    return contact


