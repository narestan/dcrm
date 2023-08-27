import mysql.connector

dataBase = mysql.connector.connect(
    host ='localhost',
    user = 'root',
    passwd = 'Iman@2222' ,           
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE NEWCRM")

print("ALL DONE")

