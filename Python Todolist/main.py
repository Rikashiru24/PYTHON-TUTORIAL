from databasemanager import DatabaseManager
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
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

# name = input("Type your name: ")

# insert_query = "INSERT INTO names (name) VALUES (%s)"
# values = (name,)
# db.execute_query(insert_query, values)

@app.route('/names')
def get_names():
    get_query = "SELECT * FROM names"
    results = db.run_query(get_query)
    names = [row[1] for row in results] if results else []
    return jsonify({"names": names})


if __name__ == '__main__':
    app.run(debug=True)
