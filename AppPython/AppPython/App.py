import os
from Model.Clases import Categoria, Producto
from BDConnect import DAO

while True:
    os.system("cls")
    print("{1} - Insertar Categoria")
    print("{2} - Listar Categorias")

    print("{3} - Insertar Nuevo Producto")
    print("{4} - Listar Productos")


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
        input("Categorias Listadas... Presiona ENTER para continar!")
    
    if(op == "3"):
        os.system("cls")
        for cat in dao.LeerCategorias():
            print(f"{cat.getCodCategoria()} | {cat.getNombreCategoria()}")
        cat = input("Seleccione la Categoria a la cual se agregara el Producto: ")
        os.system("cls")
        n = input("Ingresa el Nombre del Producto: ")
        d = input("Ingresa la Descripcion detallada del Producto: ")
        precio = input("Ingresa el Valor Unitario del Producto: ")
        stock = input("Ingresa el Stock disponible del Producto: ")
        p = Producto(0,n,d,precio,stock,cat)
        dao.InsertarProducto(p)
        input("Producto Agregado! Presiona ENTER para Continuar...")

    if(op == "4"):
        for p in dao.LeerProductos():
            print(f"{p.getNombreProducto()} | {p.getDescripcion()} | {p.getValor()} | { p.getStock() } | {p.getCodCategoria()}")
        input("Productos Listados... Presiona ENTER para continar!")