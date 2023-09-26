from Main import Usuario
import os
listaUsuarios = []

user1 = Usuario("user1", "as", "user1","123")
user2 = Usuario("user2", "asd", "user2", "123")
user3 = Usuario("user3", "asd", "user3", "123")
user4 = Usuario("user4", "asd", "user4", "123")
user5 = Usuario("user5", "asd", "user5", "123")
listaUsuarios.append(user1)
listaUsuarios.append(user2)
listaUsuarios.append(user3)
listaUsuarios.append(user4)
listaUsuarios.append(user5)

while True:
    os.system("cls")
    print("[1] - Registrarse")
    print("[2] - Iniciar Sesion")
    opcion = input("Ingresa la Opcion: ")

    if(opcion == "1"):
        os.system("cls")
        username = input("Ingresa tu Username: ")
        foto = input("Ingresa tu Foto de Perfil: ")
        correo = input("Ingresa tu Correo: ")
        password = input("Ingresa tu Password: ")

        user = Usuario(username, foto, correo, password)
        listaUsuarios.append(user)
        # with open('usuarios.txt', "w") as f:
        #     f.writelines(f"{username}, {foto}, {correo}, {password}")
        os.system("cls")
        input("Usuario Registrado")

    if(opcion == "2"):
        os.system("cls")
        userLogueado = None
        correo = input("Ingresa tu Correo: ")
        for x in listaUsuarios:
            if(x.Email == correo):
                #Correo Correcto
                userLogueado = x
        if(userLogueado == None):
            os.system("cls")
            input("Usuario NO Encontrado!!!")
        else:
            os.system("cls")
            contador = 0
            while True:
                if(contador < 3):
                    password = input("Ingresa Password: ")
                    if(userLogueado.Password == password):
                        os.system("cls")
                        input("Inicio de Sesion Correcto")
                        while True:
                            print("[1] - Postear") #Task 1
                            print("[2] - Seguir")
                            print("[3] - Dar Like ") #Task 3
                            print("[4] - Ver mis Seguidores")
                            print("[5] - Ver Seguidos")
                            print("[6] - Ver mis Posts") #Task 2
                            print("[7] - Dejar de Seguir") #Task 4
                            print("[0] - Cerrar Sesion ")
                            opcion2 = input("Ingresa tu Opcion: ")
                            if(opcion2 == "1"):
                                userLogueado.Postear("Vacaciones", "img")

                            if(opcion2 == "2"):
                                num = 1
                                for u in listaUsuarios:
                                    print(f"[{num}] - {u.Username}")
                                    num+= 1
                                seguir = int(input("Ingresa numero del usuario a seguir: "))
                                calculo = seguir - 1
                                userLogueado.Seguir(listaUsuarios[calculo])


                            if(opcion2 == "5"): #Ver Seguidos
                                userLogueado.VerSeguidos()

                            if(opcion2 == "4"): #Ver Seguidores
                                userLogueado.VerSeguidores()
                                
                            if(opcion2 == "0"):
                                userLogueado = None
                                break        
                    else:
                        os.system("cls")
                        contador += 1
                        input("Password Incorrecta!")
                else:
                    input("Usuario Bloqueado!")
                    break
        
       