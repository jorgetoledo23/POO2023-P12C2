import mysql.connector

class DAO: #DATA ACCESS OBJECT

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user="root",
                password="root",
                host="localhost",
                database="noviembre"
                )
            print("Coneccion Establecida!")
        except:
            print("Error de Coneccion!")

dao = DAO()


