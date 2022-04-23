#Python

from typing import Optional

#Pydantic -> Pydantic es una libreria que esta por debajo de FastApi, por eso se importa primero

from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()

# Models

class Person(BaseModel):
    first_name : str
    last_name : str
    age : int
    hair_color : Optional[str] = None
    is_married : Optional[bool] = None


@app.get('/')
def home():
    return {
        'Hello': 'World'
    }

@app.get('/tweets/{tweet_id}/')
def tweets(tweet_id):
    return {
        'tweet_id' : tweet_id
    }

# Request and Response Body

@app.post('/person/new/')
def create_person(person : Person = Body(...)):
    return person



