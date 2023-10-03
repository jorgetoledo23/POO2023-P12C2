from typing import List
class Alumno:

    def __init__(self, rut, nombre:str, apellido:str):
        self.Rut = rut
        self.Nombre = nombre.title() + " " + apellido.title()
        self.LibroNotas:List[float] = []

    def getRut(self):
        return self.Rut
    
    def getInfo(self):
        return f"Alumno Rut: {self.Rut} Nombre: {self.Nombre}"
    
    def AgregarNota(self, nota:float):
        self.LibroNotas.append(nota)
        input("Nota Insertada de manera Correcta!")

    def VerNotas(self):
        for nota in self.LibroNotas:
            print(nota)

        input("Promedio: ")