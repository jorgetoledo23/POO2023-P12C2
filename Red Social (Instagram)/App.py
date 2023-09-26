from Main import Usuario
import os
listaUsuarios = []

user1 = Usuario("user1", "as", "user1","123")
user2 = Usuario("user2", "asd", "user2", "123")
listaUsuarios.append(user1)
listaUsuarios.append(user2)

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
        user = None
        correo = input("Ingresa tu Correo: ")
        for x in listaUsuarios:
            if(x.Email == correo):
                #Correo Correcto
                user = x
        if(user == None):
            os.system("cls")
            input("Usuario NO Encontrado!!!")
        else:
            os.system("cls")
            contador = 0
            while True:
                if(contador < 3):
                    password = input("Ingresa Password: ")
                    if(user.Password == password):
                        os.system("cls")
                        input("Inicio de Sesion Correcto")
                        while True:
                            print("[1] - Postear") #Task 1
                            print("[2] - Seguir")
                            print("[3] - Dar Like ")
                            print("[4] - Ver mis Seguidores")
                            print("[5] - Ver Seguidos")
                            print("[6] - Ver mis Posts") #Task 2
                            print("[0] - Cerrar Sesion ")
                            opcion2 = input("Ingresa tu Opcion: ")
                            if(opcion2 == "1"):
                                x.Postear("Vacaciones", "img")

                            if(opcion2 == "2"):
                                num = 1
                                for u in listaUsuarios:
                                    print(f"[{num}] - {u.Username}")
                                    num+= 1
                                seguir = int(input("Ingresa numero del usuario a seguir: "))
                                calculo = seguir - 1
                                x.Seguir(listaUsuarios[calculo])


                            if(opcion2 == "5"): #Ver Seguidos
                                x.VerSeguidos()

                            if(opcion2 == "4"): #Ver Seguidores
                                x.VerSeguidores()
                                
                            if(opcion2 == "0"):
                                x = None
                                break        
                    else:
                        os.system("cls")
                        contador += 1
                        input("Password Incorrecta!")
                else:
                    input("Usuario Bloqueado!")
                    break
        
       