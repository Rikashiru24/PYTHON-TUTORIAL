from databasemanager import DatabaseManager

db = DatabaseManager(
    host="localhost",
    user="root",
    password="017HarVin20",
    database="student"
)
db.connect()

create_table = """CREATE TABLE IF NOT EXISTS names (
                            name_id INT PRIMARY KEY AUTO_INCREMENT,
                            name VARCHAR(50) NOT NULL
)"""
db.execute_query(create_table)

name = input("Type your name: ")

insert_query = "INSERT INTO names (name) VALUES (%s)"
values = (name,)
db.execute_query(insert_query, values)

