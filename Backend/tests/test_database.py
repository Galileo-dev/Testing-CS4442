import pytest
from database import Database

def test_basic_functionality_rooms():
    database = Database
    assert isinstance(database.getFirstRoom(database), str)
    
def test_basic_functionality_users():
    database = Database
    assert isinstance(database.getFirstUser(database), str)
    
def test_get_name_from_uid():
    database = Database
    assert database.getNameFromUID(database, "KlhITEDxj5akF0cK7cymJmmonC93")["displayName"] == "Dara Newsome"
    
