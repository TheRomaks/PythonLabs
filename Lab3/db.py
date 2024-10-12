import psycopg2

from Lab3.errors.db_error import DBError


class DB:
    def __init__(self,host:str,port:int,database:str,user:str,password:str):
        self.host=host
        self.port=port
        self.database=database
        self.user=user
        self.password=password

    def connect(self):
        try:
            conn = psycopg2.connect(port=self.port, user=self.user, password=self.password, host=self.host,database=self.database)
            return conn
        except DBError as e:
            print(f"Error:{str(e)}")

    def execute_query(self,conn,query):
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except DBError as e:
            print(f"Error:{str(e)}")
            return None

    def close_connection(self, conn):
        if conn:
            conn.close()
            print("Database connection closed.")


