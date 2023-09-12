#Determinen las Entidades Claves de la App 
#y algunas caracteristicas (atributos)

import datetime

class Usuario:

    def __init__(self, username, fotoPerfil, email, password):
        self.Username = username
        self.FotoPerfil = fotoPerfil
        self.Email = email
        self.Password = password
        self.Seguidores = []
        self.Seguidos = []
        self.Posts = []
        
    #Method
    def Postear(self, desc, imgvideo):
        P = Post(desc, imgvideo)
        self.Posts.append(P)

    def EliminarPost(self):
        pass

    def Seguir(self, user):
        self.Seguidos.append(user)
        user.Seguidores(self)

    def DejarSeguir(self):
        pass

    def DarLike(self, post):
        like = Like(self, post)
        post.Likes.append(like)

class Post:
    def __init__(self, descripcion, img_video, ):
        self.Descripcion = descripcion
        self.ImgVideo = img_video
        self.Likes = []
        self.Fecha = datetime.datetime.now()

class Like:
    def __init__(self, user, post):
        self.User = user
        self.Post = post
        self.Fecha = datetime.datetime.now()



