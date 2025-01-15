import pytest
from python_sql_connector_project import Database

@pytest.fixture
def db():
    return Database(host="localhost", user="root", password="****", database="python_db")

def test_insert(db):
    db.insert("John Doe", 30, "New York")
    result = db.select()
    assert ("John Doe", 30, "New York") in result

def test_update(db):
    db.update(1, "Jane Doe", 25, "Los Angeles")
    result = db.select()
    assert ("Jane Doe", 25, "Los Angeles") in result

def test_delete(db):
    db.delete(1)
    result = db.select()
    assert 1 not in [row[0] for row in result]