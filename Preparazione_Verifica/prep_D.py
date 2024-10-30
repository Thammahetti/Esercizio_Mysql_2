import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database= "Animali"
)
mycursor = mydb.cursor()
sil = True
while sil == True:

  print("--------------------------------------------------")
  print("Premi 1 per inserire un nuovo animale-------------")
  print("Premi 2 per visualizzare tutti gli animali--------")
  print("Premi 3 per eliminare un animale------------------")
  print("Premi 4 per modificare un animale-----------------")
  print("--------------------------------------------------")
  x = int(input("Inserisci:  "))

  if x == 1:
    nomeProprio = input("Inserisci Nome Del Animale:  ")
    razzaAnimali = input("Inserisci la Razza:  ")
    pesoAnimale = int(input("Inserisci il peso: "))
    etaAnimale = int(input("Inserisci l'eta: "))
    sql = "INSERT INTO Mammiferi (nome_Proprio, razzi, Peso, eta) VALUES (%s, %s, %s, %s)"
    val = ( nomeProprio, razzaAnimali, pesoAnimale, etaAnimale)
    mycursor.execute(sql, val)
    print("Animale Aggiunto")
  elif x==2:
    mycursor.execute("SELECT * FROM Mammiferi")

    myresult = mycursor.fetchall()

    for x in myresult:
      print(x)
  elif x== 3:
      print("Inserisci un nuovo animale")
  elif x==4:
    print("Inserisci un nuovo animale")
  elif x>4 or x<1:
    print("Numero non valido. Riprova")
    
notUsed= input("Premi Enter per continuare ") 
