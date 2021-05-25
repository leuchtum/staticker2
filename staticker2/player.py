from .database import BaseModel
from peewee import CharField, DateTimeField

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()
    
