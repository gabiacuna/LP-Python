class Perro:
    patas = 4   #Atributo
    def __init__(self, n):
        self.nombre = n
    def ladrar(self):   #Método
        print("Guau!")
    def placaInfo(self):
        print("Nombre: ", self.nombre)

p = Perro("Prince") #instanciacion

p.ladrar()
p.placaInfo()

print(Perro.patas)
print(p.patas)

Perro.ladrar(p)

print(Perro.ladrar)