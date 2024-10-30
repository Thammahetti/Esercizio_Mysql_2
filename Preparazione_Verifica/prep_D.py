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
      deldata= input("Inserisci ID del Animale per eliminarlo: ")
      mycursor.execute("DELETE FROM Mammiferi WHERE id='" + deldata+ "';")
      print("Eliminato Correttamente")
  elif x==4:
    iddata= input("Inserisci ID del Animale che vuoi modificare: ")
    nomeProprio = input("Inserisci Nome Del Animale:  ")
    razzaAnimali = input("Inserisci la Razza:  ")
    pesoAnimale = int(input("Inserisci il peso: "))
    etaAnimale = int(input("Inserisci l'eta: "))
    
    sql = "UPDATE Mammiferi SET  nome_Proprio= %s,razzi = %s, Peso = %s , eta = %s WHERE id = %s"
    val = (nomeProprio, razzaAnimali,pesoAnimale, etaAnimale , iddata)
    print("Modificato Correttamente")

    mycursor.execute(sql, val)
  elif x>4 or x<1:
    print("Numero non valido. Riprova")
    notUsed= input("Premi Enter per continuare ") 
    

