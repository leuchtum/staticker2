import os
from peewee import SqliteDatabase, Model, CharField, DateTimeField

DIR_NAME = ".staticker"
DB_NAME = "data.db"

class DirManager:
    def __init__(self):
        self.dir_path = f"{os.path.expanduser('~')}/{DIR_NAME}"
        
    def exists(self):
        return os.path.exists(self.dir_path)
    
    def create(self):
        if not self.exists():
            os.mkdir(self.dir_path)
            
    def get_directory(self):
        return self.dir_path
            
         
class DBManager:
    dm = DirManager()
    dm.create()
    
    db_path = f"{dm.get_directory()}/{DB_NAME}"
    db = SqliteDatabase(db_path)
    
    def get_database(self):
        return self.db
    
    def create_tables(self, tables: list):
        self.db.create_tables(tables)
    
        
class User(Model):
    username = CharField(unique=True)
    password = CharField()
    
    class Meta:
        database = DBManager().get_database()
        db_table = 'user'
    
if __name__ == "__main__":
    dbm = DBManager()
    dbm.create_tables([User])
    
    