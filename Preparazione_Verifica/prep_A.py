import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)



mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE if not exists Animali")

mycursor.execute("USE Animali")
mycursor.execute("CREATE TABLE if not exists Mammiferi (id INT PRIMARY KEY AUTO_INCREMENT, nome_Proprio VARCHAR(255), razzi VARCHAR(255), Peso INT, eta INT)")