import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
    database="ServerData"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Milo", "Milan")
mycursor.execute(sql, val)

mydb.commit()

print( "record inserted.")