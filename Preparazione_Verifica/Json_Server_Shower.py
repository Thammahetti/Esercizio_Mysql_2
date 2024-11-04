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

def fetch_table_data_Panda(razza):
    query = "SELECT * FROM Mammiferi WHERE razzi = %s"
    mycursor.execute(query, (razza,))
    rows = mycursor.fetchall()
    return rows

def fetch_table_data_Peso(peso):
    query = "SELECT * FROM Mammiferi WHERE pes = %s"
    mycursor.execute(query, (razza,))
    rows = mycursor.fetchall()
    return rows


@app.route("/")
def index():
    data = fetch_table_data()
    return jsonify({'Mammiferi':data})  


@app.route("/<razza>")
def Panda(razza):
    data = fetch_table_data_Panda(razza)
    return jsonify({razza:data})  


if __name__ == "__main__":
    app.run()