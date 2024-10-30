import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
    database="Animali"
)

mycursor = mydb.cursor()




m