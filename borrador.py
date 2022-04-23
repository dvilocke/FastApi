
from pydantic import BaseModel, validator

class UserModel(BaseModel):
    name : str
    username : str
    password1 : str
    password2 : str

    @validator('name')
    def name_must_contain_space(cls, v : str):
        if ' ' not in v:
            raise ValueError('must contain a space')

class X(str):

    def __init__(self):
        self.cosa = 'hola'


user = UserModel(
    name='samuel colvin',
    username='scolvin',
    password1='zxcvbn',
    password2='zxcvbn',
)

cosita = X()