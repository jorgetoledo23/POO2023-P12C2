class Categoria:
    def __init__(self, cod, nombre) -> None:
        self.__Cod_Categoria = cod
        self.__Nombre = nombre

    def getCodCategoria(self) -> str:
        return self.__Cod_Categoria
    
    def getNombreCategoria(self) -> str:
        return self.__Nombre