import os
from typing import List
from Model import Alumno

a=Alumno("1-1", "Jhon", "Snow")
b=Alumno("2-2", "Jack", "Sparrow")

listadoAlumnos:List[Alumno] = [a,b]

while 10>5:
    os.system("cls")
    print("[1] - Ingresar un Alumno")
    print("[2] - Ver listado de Alumnos")
    print("[3] - Ingresar una Nota")
    print("[4] - Ver Notas de un Alumno")
    print("[5] - Salir")
    opcion = input("Selecciona una Opcion: ")

    if(opcion == "1"):
        #Ingreso de Alumno
        r = input("Ingresa Rut del Alumno: ")
        n = input("Ingresa Nombre del Alumno: ")
        a = input("Ingresa Apellido del Alumno: ")
        alumno = Alumno(r,n,a)
        listadoAlumnos.append(alumno)
        input("Alumno Ingresado de manera Exitosa!")

    if(opcion == "2"):
        #Ver Listado de Alumnos
        for alumno in listadoAlumnos:
            print(alumno.getInfo())
        input()

    if(opcion == "3"):
        #Ingreso de Nota
        alumno = None
        rut = input("Ingresa el Rut del Alumno: ")
        for a in listadoAlumnos:
            if(a.getRut() == rut):
                alumno = a
        if(alumno != None):
            nota = float(input("Ingresa la Nota: "))
            alumno.AgregarNota(nota)
        else:
            input("Alumno con ese Rut no se encuentra!")
        
    if(opcion == "4"):
        #Ver Notas y Promedio
        alumno = None
        rut = input("Ingresa el Rut del Alumno: ")
        for a in listadoAlumnos:
            if(a.getRut() == rut):
                alumno = a
        if(alumno != None):
            alumno.VerNotas()
        else:
            input("Alumno con ese Rut no se encuentra!")
    if(opcion == "5"):
        break #Salir del Sistema
    
    
    
    
    