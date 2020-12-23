# es un objeto que va recorriendo un conjunto de elementos oestructura
# retornando un elemento a la vez. Soporta dos metodos:

chin = iter([1, 2, 3])

print(chin)

# print(next(chin))
# print(next(chin))
# print(next(chin))
# print(next(chin)) Tira error pk se acaba


#print(sum(chin))

#print('_'.join(str(chin)))

# map aplica una funcion a todos los elementos de un iterable.
# Retorna un iterador


x = map(lambda x: x*x, chin)

for i in x:
    print(i)

# filter 
# retorna un iterador a los elementos de un iterable que cumplan concierta 
# condicion (una funcion que retorna verdadero o falso)

lista = filter(lambda x: x%2 != 0, [1, 2, 3, 4, 5, 6])

for i in lista: print(i)