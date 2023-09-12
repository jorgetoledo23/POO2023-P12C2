from Main import Usuario
import os
listaUsuarios = []
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
        with open('usuarios.txt', "w") as f:
            f.writelines(f"{username}, {foto}, {correo}, {password}")
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
                        break
                    else:
                        os.system("cls")
                        contador += 1
                        input("Password Incorrecta!")
                else:
                    input("Usuario Bloqueado!")
                    break

        print("[1] - Postear")
        print("[2] - Seguir")
        print("[3] - Dar Like ")
        print("[4] - Ver mis Seguidores")
        print("[5] - Ver Seguidos")
        print("[0] - Cerrar Sesion ")
        opcion2 = input("Ingresa tu Opcion: ")
        if(opcion2 == "1"):
            x.Postear("Vacaciones", "img")

        if(opcion2 == "2"):
            num = 1
            for u in listaUsuarios:
                print(f"[{num}] - {u.Username}")
                num+= 1
            int(input("Ingresa numero del usuario a seguir: "))
            
            x.Seguir(listaUsuarios[num - 1])
            

    