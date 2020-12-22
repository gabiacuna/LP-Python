#funciones an onimas en tiempo de ejecucion usando expresiones lambda
#https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions

#no incluyen return y solo pueden tener una sentencia

print((lambda x: x**3) (4))

squares = []
for x in range(5):
    squares.append(lambda n = x : n**2)

print(squares[4])
print(squares[4]())

def make_elevador(n):
    return lambda x : x**n

f = make_elevador(5)

print(f(2))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'a')]
pairs.sort(key=lambda pair: pair[1])

print(pairs)