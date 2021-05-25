import pytest
from staticker2.database import DirManager, DB_NAME, DBManager
import os
import shutil

def test_DirManager(dbtests):

    dm = DirManager()
    
    if os.path.exists(dm.dir_path):
            shutil.rmtree(dm.dir_path)
        
    assert os.path.exists(dm.dir_path) == False
    assert dm.exists() == False
    
    dm.create()
    
    assert os.path.exists(dm.dir_path) == True
    
    dm.create()
    
    assert os.path.exists(dm.dir_path) == True


def test_DBManager(dbtests):
    dm = DirManager()
    dm.create()
    
    db_path = f"{dm.get_directory()}/{DB_NAME}"
    if os.path.exists(db_path):
        os.unlink(db_path)
    
    assert os.path.exists(db_path) == False
