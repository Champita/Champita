# Importamos el ModuMódulo
import bdb
from datetime import date, time, datetime
from time import sleep
from webbrowser import get
import pymongo
import pywhatkit

uri = "mongodb://admincakestore:0pmcsXpjfEgSpbXQuZBZVfkoZBAWx51q1tWc2Yx21yoa1ijrkUUxZPFHhvX1nT3qHDdXtlLCrBCPhB9pGv9nzA==@admincakestore.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@admincakestore@"
MONGO_TIEMPO_FUERA=1000
try:
    client = pymongo.MongoClient(uri)
    client.server_info()
    print("Coneccion a mongo exitosa")
    mydb = client["CakeStoreDB"]
    print(mydb.list_collection_names())
    mycol = mydb["birthDay"]
    dt = datetime.now()
    datetoday= str(dt.day)+"-"+str(dt.month)
    datehour=dt.hour
    dateminuto=dt.minute
    for x in mycol.find():
      fechadecumple=x["bdPerson"]
      fechadecumple=fechadecumple.split("-")
      fechadecumple=str(int(fechadecumple[2]))+"-"+str(int(fechadecumple[1]))
      print(fechadecumple)
      unasemanantesdias=abs((int(fechadecumple[2]))-(dt.day))
      unasemanaantesmes=abs((int(fechadecumple[1]))-(dt.month))
      nombrecliente=x["clientName"]
      telefono=x['clientPhone']
      telefono2="966669673"
      if (unasemanantesdias==7 and unasemanaantesmes==0) or (unasemanantesdias==7 and unasemanaantesmes==1):
        try: 

          # Enviamos el mensaje
          print("El mensaje esta siendo enviado")
          pywhatkit.sendwhatmsg("+56"+telefono2, "Holaaaaa "+nombrecliente+"!Queda una semana para tu cumpleaños 🍰🍰🍰 y en Cakestore🎂 queremos recomendarte lo mejor para celebrarlo,en el siguiente enlace podras ver algunas de nuestras ofertas para ti!:  https://cakestorestgo.cl/collections/tortas ", datehour==0,dateminuto==19,5,True,5)
          print("Mensaje Enviado") 

        except Exception as e:
          
          print("Ocurrio un Error: "+str(e))

          #Codigo extraido de https://blog.facialix.com/tutorial-enviar-mensajes-automaticos-de-whatsapp-desde-python/

      client.close()
except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo exedido "+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse a mongodb "+errorConexion)



'''Para enviar mensajes desde whatsapp web
import pywhatkit

# Send a WhatsApp Message to a Contact at 1:30 PM
pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")

# Play a Video on YouTube
pywhatkit.playonyt("PyWhatKit")'''