import psycopg2
import pytest
from PG.db import DB

@pytest.fixture(scope="function")
def db_connection():
    db = DB()
    conn = db.connect()
    yield conn
    db.close_connection(conn)

@pytest.fixture(scope="function")
def db():
    db = DB()
    conn = db.connect()
    yield db
    db.close_connection(conn)


def test_connect(db_connection):
    assert db_connection is not None

def test_execute_query():
    db = DB()
    conn=db.connect()
    query = "SELECT * FROM recipes;"
    result = db.execute_query(conn, query)
    assert result is not None

def test_insert_data(db_connection):
    db = DB()
    type = "Main Course"
    name = "Test Recipe"
    ingredients = "test ingredients"
    instructions = "test instructions"
    db.insert_data(db_connection, type, name, ingredients, instructions)
    query = "SELECT * FROM recipes WHERE name = 'Test Recipe';"
    result = db.execute_query(db_connection, query)
    assert result is not None and len(result) > 0

def test_insert_data2(db_connection):
    db = DB()
    type = "Main Course"
    name = "Test Recipe"
    ingredients = "test ingredients"
    instructions = "test instructions" * 1000
    result = db.insert_data(db_connection, type, name, ingredients, instructions)
    assert result is not None and len(result) > 0

def test_close_connection():
    db = DB()
    conn = db.connect()
    db.close_connection(conn)
    try:
        conn.cursor()
        assert False, "Connection should be closed"
    except psycopg2.InterfaceError:
        assert True

def test_execute_query_failure(db_connection):
    db = DB()
    query = "SELECT * FROM non_existent_table;"
    try:
        db.execute_query(db_connection, query)
    except psycopg2.errors.UndefinedTable:
        assert True

