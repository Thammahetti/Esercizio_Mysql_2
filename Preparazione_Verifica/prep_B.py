import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (nome_Proprio, razzi, Peso, eta) VALUES (%s, %s,%s,%s)"
val = [( 'Rexoe', 'Panda', 32, 2),( 'Zani', 'Leone', 31, 3)]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.") 