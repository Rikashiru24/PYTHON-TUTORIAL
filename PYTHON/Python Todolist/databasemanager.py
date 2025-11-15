import mysql.connector
from mysql.connector import Error

class DatabaseManager:
    def __init__(self, host, user, password, database=None):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            print(f"Connected to database: {self.database or 'Mysql server'}")
        except Error as e:
            print(f"Error: {e}")

    def create_database(self, db_name):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"Database '{db_name}' ensured.")
        except Error as e:
            print(f"Failed to create database: {e}")
    
    def run_query(self, query, params=None):
        try:
            self.cursor.execute(query, params or ())
            self.connection.commit()
            return self.cursor.fetchall() if query.strip().upper().startswith("SELECT") else None
        except Error as e:
            print(f"Query failed: {e}")
            return None
    
    def execute_query(self, query, params=None):
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def show_database(self):
        self.cursor.execute("SHOW DATABASES")
        return self.cursor.fetchall()
    
        
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Connection closed.")
