class Personaje:
    #Atributos
    def __init__(self, nombre:str, vida:int, damage:int, oro:int, defenza:int):
        self.Nombre = nombre
        self.Vida = vida
        self.Damage = damage
        self.Oro = oro
        self.Defenza = defenza

    def getInfo(self):
        """Metodo que retorna un str con la Informacion del personaje"""
        return f"Nombre: {self.Nombre} \nVida: {self.Vida} \nAtaque: {self.Damage}\nOro: {self.Oro}\nDefenza: {self.Defenza}\n--------"

    def Atacar(self, personajeAtacado):
        damageRecibido = self.Damage - personajeAtacado.Defenza
        if(not damageRecibido < 0):   
            personajeAtacado.Vida = personajeAtacado.Vida - damageRecibido

class Item:
    def __init__(self, coste, nombre, damage, defenza, vida):
        self.Nombre = nombre
        self.Vida = vida
        self.Coste = coste
        self.Defenza = defenza
        self.Damage = damage



#Instancias
p1 = Personaje("Player 1", 100, 10, 1000, 0)
p2 = Personaje(nombre="Player 2", vida=200, damage=3, oro=1000, defenza=10)
p3 = Personaje("Player 3", 150, 5, 1000, 5)

print(p1.getInfo())
print(p2.getInfo())
print(p3.getInfo())

p1.Atacar(p2)
p2.Atacar(p3)
p3.Atacar(p1)

print(p1.getInfo())
print(p2.getInfo())
print(p3.getInfo())
