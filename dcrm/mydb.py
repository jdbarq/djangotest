import mysql.connector

dataBase = mysql.connector.connect(

	host = 'localhost',
	user = 'root',
	password = 'admin'

	)

mycursor = dataBase.cursor()

mycursor.execute("CREATE DATABASE mydb")

print("Connected")
