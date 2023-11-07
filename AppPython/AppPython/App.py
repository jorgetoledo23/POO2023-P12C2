import os
from Model.Categoria import Categoria
from BDConnect import DAO

while True:
    os.system("cls")
    print("{1} - Insertar Categoria")
    print("{2} - Listar Categorias")
    print("{0} - Salir")
    op = input("Selecciona una Opcion: ")

    dao = DAO()
    if(op == "1"):
        nombre = input("Nombre de la Categoria: ")
        category = Categoria(0, nombre)
        dao.InsertarCategoria(category)
        input("Categoria Insertada")

    if(op == "2"):
        for cat in dao.LeerCategorias():
            print(cat.getNombreCategoria())
        input("Categorias Listadas... Presiona ENTER para continar")