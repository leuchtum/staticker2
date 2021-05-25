from peewee import SqliteDatabase, Model, CharField, DateTimeField


DATABASE = "test_db.db"
database = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = database
        
        
class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()