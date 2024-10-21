import psycopg2
import pytest
from PG.db import DB

@pytest.fixture(scope="function")
def db_connection():
    db = DB("localhost", 5430, "recipes_data", "postgres", "password")
    conn = db.connect()
    yield conn
    db.close_connection(conn)

@pytest.fixture(scope="function")
def db():
    db = DB("localhost", 5430, "recipes_data", "postgres", "password")
    conn = db.connect()
    yield db
    db.close_connection(conn)


def test_connect(db_connection):
    assert db_connection is not None

def test_execute_query():
    db = DB("localhost", 5430, "recipes_data", "postgres", "password")
    conn=db.connect()
    query = "SELECT * FROM recipes;"
    result = db.execute_query(conn, query)
    assert result is not None

# def test_insert_data(db_connection):
#     db = DB("localhost", 5430, "recipes_data", "postgres", "password")
#     type = "Main Course"
#     name = "Test Recipe"
#     ingredients = "test ingredients"
#     instructions = "test instructions"
#     db.insert_data(db_connection, type, name, ingredients, instructions)
#     query = "SELECT * FROM recipes WHERE name = 'Test Recipe';"
#     result = db.execute_query(db_connection, query)
#     assert result is not None and len(result) > 0
#
# def test_insert_data_failure(db_connection):
#     db = DB("localhost", 5430, "recipes_data", "postgres", "password")
#     type = "Main Course"
#     name = "Test Recipe"
#     ingredients = "test ingredients"
#     instructions = "test instructions" * 1000
#     result = db.insert_data(db_connection, type, name, ingredients, instructions)
#     assert result is not None and len(result) > 0

def test_close_connection():
    db = DB("localhost", 5430, "recipes_data", "postgres", "password")
    conn = db.connect()
    db.close_connection(conn)
    try:
        conn.cursor()
        assert False, "Connection should be closed"
    except psycopg2.OperationalError:
        assert True

def test_execute_query_failure(db_connection):
    db = DB("localhost", 5430, "recipes_data", "postgres", "password")
    query = "SELECT * FROM non_existent_table;"
    result = db.execute_query(db_connection, query)
    assert result is None

