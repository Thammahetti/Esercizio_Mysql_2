from flask import Flask, jsonify
import mysql.connector
import json
import pymysql


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)

app = Flask(__name__)
mycursor = mydb.cursor(dictionary=True)
def fetch_table_data():
    mycursor.execute("SELECT * FROM Mammiferi")
    rows = mycursor.fetchall()
    return rows





@app.route("/")
def index():
    data = fetch_table_data()
    return jsonify({'Mammiferi':data})  


if __name__ == "__main__":
    app.run()