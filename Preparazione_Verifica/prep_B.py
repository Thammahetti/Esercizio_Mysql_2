import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)

mycursor = mydb.cursor()

sql = "INSERT INTO Mammiferi (id, nome_Proprio, razzi, Peso, eta) VALUES (%s, %s, %s, %s, %s)"
val = [(1, 'Rex', 'Cane', 31, 2),(2, 'Leon', 'Leone', 21, 2),(3, 'Jin', 'Panda', 33, 4),(4, 'Leo', 'Cane', 21, 5),(5, 'Yepr', 'Gatto', 31, 4)]
mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.") 