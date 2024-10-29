import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)
mycursor = mydb.cursor()
print("--------------------------------------------------")
print("Premi 1 per inserire un nuovo animale-------------")
print("Premi 2 per visualizzare tutti gli animale--------")
print("Premi 3 per eliminare un animale------------------")
print("Premi 4 per modificare un animale-----------------")
print("--------------------------------------------------")
x = input("Inserisci: ")

if x == 1:
    print("Inserisci un nuovo animale")
