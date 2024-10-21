import psycopg2
from errors.db_error import DBError


class DB:
    def __init__(self, host: str, port: int, database: str, user: str, password: str):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        try:
            self.conn = psycopg2.connect(port=self.port, user=self.user, password=self.password, host=self.host, database=self.database)
            return self.conn
        except DBError as e:
            print(f"Error:{str(e)}")
            return None

    def execute_query(self,conn, query):
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return cursor.fetchall()
        except DBError as e:
            self.conn.rollback()
            print(f"Error: {str(e)}")
            return None

    def close_connection(self,conn):
        if conn is not None:
            conn.close()
            print("PG connection closed.")

    def insert_data(self,conn, type: str, name: str, ingredients: str, instructions: str):
        try:
            cursor = conn.cursor()
            cursor.execute(
                f"INSERT INTO recipes (type, name, ingredients, instructions) VALUES ('{type}', '{name}', '{ingredients}', '{instructions}')")
            conn.commit()

        except DBError as e:
            self.conn.rollback()
            print(f"Error: {str(e)}")
            return None


