#Python

from typing import Optional

#Pydantic -> Pydantic es una libreria que esta por debajo de FastApi, por eso se importa primero

from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query

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

# Validaciones : Query

@app.get('/person/detail')
def show_person(
        name : Optional[str] = Query(None, min_length=1, max_length=50),
        age : str = Query(...)
):
    return {
        name : age
    }





