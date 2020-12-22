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
        print("Amigxs(", len(self.amigos), "):")
        for perrito in self.amigos:
            print("\t-", perrito.nombre)
    
    def cumpleanos(self):
        self.edad += 1
        print("Feliz cumpleaños!")
    
    def nuevxAmigx(self, obj):
        self.amigos.append(obj)
        print(self.nombre, " y ", obj.nombre, " son amigos!")

class Cachorro(Perro):  # Herencia
    def __init__(self, n):
        print("Nacio un cachorrito!")
        Perro.__init__(self, n, e = 0)  # Para llamar al constructor y cualquier metodo de la clase parte


p = Perro("Prince", 11) # instanciacion
g = Perro("Grego", 8)
C = Cachorro("Cliford")

p.ladrar()

p.placaInfo()
print()
p.cumpleanos()
p.nuevxAmigx(g)
print()
p.placaInfo()

print(Perro.patas)
print(p.patas)

Perro.ladrar(p)

print(Perro.ladrar)