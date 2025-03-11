import sqlite3
class Database_Manager:
    def __init__(self,name: str):
        self.connection=sqlite3.connect(name)
        self.cursor=self.connection.cursor()
    def search_one(self,query):
        result=self.cursor.execute(query).fetchone()
        return result
    def search_all(self,query):
        result=self.cursor.execute(query).fetchall()
        return result
    def close(self):
        self.connection.close()
    def run_save(self,query):
        self.cursor.execute(query)
        self.connection.commit()

class DatabaseManager:
    def __init__(self,db_name):
        self.db_name=db_name
    def __enter__(self):
        self.conn=sqlite3.connect(self.db_name)
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.conn.commit()
        self.conn.close()
    def execute(self,query,params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor
    def fetch_one(self, query, params=()):
        cursor=self.execute(query, params)
        return cursor.fetchone()
    def fetch_all(self,query,params=()):
        cursor=self.execute(query,params)
        return cursor.fetchall()

