#Docs: https://docs.python.org/3/tutorial/classes.html#inheritance

class Perro:
    patas = 4   #Atributo
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e
        self.amigos = []
    def ladrar(self):   #Método
        print("Guau!")
    def placaInfo(self):
        print("Nombre:\t", self.nombre)
        print("Edad:\t", self.edad)
        print("Amigxs:")
        for perrito in self.amigos:
            print("\t-", perrito.nombre)
    def cumpleanos(self):
        self.edad += 1
        print("Feliz cumpleaños!")
    def nuevxAmigx(self, obj):
        self.amigos.append(obj)

class Cachorro(Perro):
    def __init__(self):
        print("Nacio un cachorrito!")


p = Perro("Prince", 11) #instanciacion
g = Perro("Grego", 8)

p.ladrar()
p.placaInfo()
p.cumpleanos()
p.nuevxAmigx(g)
p.placaInfo()

print(Perro.patas)
print(p.patas)

Perro.ladrar(p)

print(Perro.ladrar)