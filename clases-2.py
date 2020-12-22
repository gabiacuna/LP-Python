#Herencia Múltiple - MRO
#http://www.srikanthtechnologies.com/blog/python/mro.aspx

class A:
    a = 0
    def cocinando(self):
        print("A está cocinando")
#[A] + merge(L[O], [O])
#[A, O]

class B:
    a = 1
    def cocinando(self):
        print("B está cocinando")

class C(B):
    a = 2
    def cocinando(self):
        print("C está cocinando")
#[C] + merge(L[B], B)
#[C] + merge([B, O], B)
#[C, B, O]

class D(A, B):
    pass
#[D] + merge(L[A], L[B], [A, B]) =
#[D] + merge([A, O], [B, O], [A, B]) =
#[D] + [A] + merge([O], [B, O], [B]) =
#[D, A] + [B] + merge([O], [O]) =
#[D, A], B] + [O] =
#[D, A, B, O]


class E(C, D):
    pass
#[E] + merge(L[C], L[D], [C, D])
#[E] + merge([C, B, O], [D, A, B, O], [C, D])
#[E] + [C] + merge([B, O], [D, A, B, O], [D])
#[E] + [C] + merge([B, O], [D, A, B, O], [D])
#[E] + [C] + [D] + merge([B, O], [A, B, O])
#[E] + [C] + [D] + [A] + merge([B, O], [B, O])
#[E] + [C] + [D] + [A] + [B] + merge([O], [O])
#[E] + [C] + [D] + [A] + [B] + [O]
#L[E] = [E, C, D, A, B, O]


# Ojito:
# En algunos casos no se podra generar una linearización.
# Esto ocurre en elcaso de que las cabezas de las listas se encuentren en las colas
# de las otras.
'''print(D().a)
print(D.mro())

print(E().a)
print(E.mro())'''

obj = D()
obj2 = E()

obj.cocinando()
obj2.cocinando()

print(E.mro())

# En python no existe la privacidad, así que se usa:
# nombres que comienzan con __ son privados (igual es posible acceder a ellos)