#pip install mysql-connector-python
import mysql.connector
from mysql.connector import errorcode
from Model.Categoria import Categoria
from typing import List

class DAO:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                user="root",
                password="root",
                host="localhost",
                database="test"
            )
            #print("Conexion Establecida")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error de Usuario o Contraseña")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("La base de datos NO existe")
            else:
                print(err)

    def InsertarCategoria(self, cat:Categoria):
        cursor = self.cnx.cursor()
        query = ("INSERT INTO tbl_categorias (nombre) VALUES (%s);")
        data = (cat.getNombreCategoria(),)
        cursor.execute(query, data)
        self.cnx.commit()

    def LeerCategorias(self) -> List[Categoria]:
        cursor = self.cnx.cursor()
        query = ("SELECT * FROM tbl_categorias")
        cursor.execute(query)
        categorias:List[Categoria] = []
        for (cod_categoria, nombre) in cursor:
            cat = Categoria(cod_categoria, nombre)
            categorias.append(cat)
        return categorias

    