class Alumno:

    def __init__(self, rut, nombre:str, apellido:str):
        self.Rut = rut
        self.Nombre = nombre.title() + " " + apellido.title()

    def getRut(self):
        return self.Rut
    
    def getInfo(self):
        return f"Alumno Rut: {self.Rut} Nombre: {self.Nombre}"