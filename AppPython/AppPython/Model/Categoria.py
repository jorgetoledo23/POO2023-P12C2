class Categoria:
    def __init__(self, cod, nombre) -> None:
        self.__Cod_Categoria = cod
        self.__Nombre = nombre

    def getCodCategoria(self) -> str:
        return self.__Cod_Categoria
    
    def getNombreCategoria(self) -> str:
        return self.__Nombre
    

class Producto:
    def __init__(self, cod, nombre, descripcion, valor_unitario, stock, cod_categoria) -> None:
        self.__Cod_Producto = cod
        self.__NombreProducto = nombre
        self.__Descripcion = descripcion
        self.__Valor = valor_unitario
        self.__Stock = stock
        self.__Cod_Categoria = cod_categoria

    def getCodigoProducto(self)-> str:
        return self.__Cod_Producto
    
    def getNombreProducto(self)->str:
        return self.__NombreProducto
    
    def getDescripcion(self) -> str:
        return self.__Descripcion
    
    def getValor(self) -> str:
        return self.__Valor
    
    def getStock(self)->str:
        return self.__Stock
    
    def getCodCategoria(self)-> str:
        return self.__Cod_Categoria