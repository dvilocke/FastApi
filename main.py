#Python

from typing import Optional

#Pydantic -> Pydantic es una libreria que esta por debajo de FastApi, por eso se importa primero

from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

# Models
#quiere decir que nos debe enviar un json en ese formato, con esos campos
class Person(BaseModel):
    first_name : str
    last_name : str
    age : int
    hair_color : Optional[str] = None
    is_married : Optional[bool] = None

class Location(BaseModel):
    city : str
    state : str
    country : str


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
        name : Optional[str] = Query(
            None,
            min_length=1,
            max_length=50,
            title= 'Person Name',
            description='This is the person name'
        ),
        age : str = Query(
            ...,
            title='Person Age',
            description= 'This is the person age'
        )
):
    return {
        name : age
    }

#Validaciones : Path Parameters
#si defines dos funciones con el mismo nombre toma la ultima, esto lo hace python
#con respecto a los path Lo correcto es que intentará tomar el primero

@app.get('/person/detail/{person_id}')
def show_person(
        person_id : int = Path(
            ...,
            gt=0,
            title= 'Person Id',
            description= 'Person Id required'
        )
):
    return {
        person_id : "It exists"
    }

# Validaciones : Request body
#aqui le estamos diciendo, o le estamos pidiendo al cliente que nos debe ingresar en esta PATH
#dos json, el de Person y el de Location, como hago para dovolver estos dos en formaton JSON
#recordemos que fastAPI hace automaticamente las conversiones, nosotros enviamos un json
#en este caso el de formato person y el otro en el formato location, fastApi lo convierte
#automaticamente a diccionarios y despues nosotros retornamos el JSON, tambien automaticamente
#convertido, pero en este caso cuando nosotros queremos combinar dos json, tenemos que hacerlo
#de forma explicita, no podemos dejar a fastApi que haga el trabajo por si mismo
#tenemos que hacerlo nosotros

@app.put('/person/{person_id}')
def update_person(
        person_id : int = Path(
            ...,
            title= 'Person ID',
            description='This is the person ID',
            gt=0
        ),
        person : Person = Body(...),
        location : Location = Body(...)
):
    results = person.dict() | location.dict()
    return results








