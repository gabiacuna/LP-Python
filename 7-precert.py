class A:
    def metodo(self):
        print("soy A")

class B(A):
    def metodo(self):
        print("soy B")

class C(A):
    def metodo(self):
        print("soy C")

class D(B):
    def metodo(self):
        print("soy D")

class E(D, B):
    pass

x = E()

x.metodo()
print(E.mro())
