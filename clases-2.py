#Herencia Múltiple

class A:
    a = 0

class B:
    a = 1

class C:
    a = 2

class D(A, B, C):
    pass

print(D().a)