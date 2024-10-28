import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)


mydb1 = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Animali")


mycursor = mydb1.cursor()

mycursor.execute("CREATE TABLE Mammiferi (name VARCHAR(255), address VARCHAR(255))")
